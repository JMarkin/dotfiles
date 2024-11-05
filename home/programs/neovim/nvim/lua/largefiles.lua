local doau = require("funcs").doau
local maxline = require("funcs").maxline
local ifind = require("funcs").ifind

local max_file_size = 2
local max_file_size_readonly = 100

local ignore_ft = {
    "help",
    "man",
    "lspinfo",
    "trouble",
    "null-ls-info",
    "qf",
    "notify",
    "startuptime",
    "checkhealth",
    "netrw",
    "neotest-output",
    "neotest-output-panel",
    "neotest-summary",
    "vista_kind",
    "sagaoutline",
    "httpResult",
}

local function get_buf_size(path)
    local ok, stats = pcall(function()
        return vim.uv.fs_stat(path)
    end)
    if not (ok and stats) then
        return 0
    end
    return math.floor(0.5 + (stats.size / (1024 * 1024)))
end

local FILE_TYPE = {
    NORMAL = 0,
    LONG_LINE = 1,
    LARGE_SIZE = 2,
    READ_ONLY = 3,
}

local function is_large_file(bufnr, as_bool, path)
    local function wrap()
        if not bufnr then
            return false
        end
        local ok, large_buf = pcall(vim.api.nvim_buf_get_var, bufnr, "large_buf")
        if not ok then
            large_buf = nil
        end

        if large_buf ~= nil then
            return large_buf
        end

        local _type = FILE_TYPE.NORMAL
        vim.api.nvim_buf_set_var(bufnr, "large_buf", _type)

        if ifind(ignore_ft, function(item, _)
            return vim.bo.ft == item
        end) then
            return _type
        end

        bufnr = bufnr or vim.api.nvim_get_current_buf()
        path = path or vim.api.nvim_buf_get_name(bufnr)
        local size = get_buf_size(path)

        if size > max_file_size_readonly then
            vim.notify("LARGE FILE SIZE: READONLY " .. size, vim.log.levels.INFO)
            _type = FILE_TYPE.READ_ONLY
        elseif size > max_file_size then
            vim.notify("LARGE FILE SIZE " .. size, vim.log.levels.INFO)
            _type = FILE_TYPE.LARGE_SIZE
        else
            local _m = maxline(path)
            if _m > vim.o.synmaxcol then
                vim.notify("LONG LINE " .. _m, vim.log.levels.INFO)
                _type = FILE_TYPE.LONG_LINE
            end
        end

        if _type ~= FILE_TYPE.NORMAL then
            vim.api.nvim_buf_set_var(bufnr, "large_buf", _type)
            doau("LargeFile", {})
        end

        return _type
    end

    local _t = wrap()

    if not as_bool then
        return _t
    end

    return _t ~= FILE_TYPE.NORMAL
end

local function optimize_buffer(args)
    local bufnr = args.buf

    local status_ok, _ = pcall(vim.api.nvim_buf_get_var, bufnr, "large_buf")
    if status_ok then
        return
    end

    local _type = is_large_file(bufnr, false, args.match)

    if _type == FILE_TYPE.NORMAL then
        return
    end

    vim.opt_local.cursorline = false
    vim.opt_local.linebreak = false
    vim.opt_local.wrap = false
    vim.opt_local.spell = false
    vim.opt_local.hlsearch = false
    vim.opt_local.incsearch = false
    vim.opt_local.foldmethod = "manual"
    vim.opt_local.swapfile = false
    vim.opt_local.bufhidden = "unload"
    if _type == FILE_TYPE.LONG_LINE then
        vim.cmd("syntax clear")
        vim.opt_local.syntax = "off"
        vim.opt_local.list = false
        vim.opt_local.undolevels = -1
        vim.opt_local.undofile = false
    end

    pcall(function()
        require("rainbow-delimiters").disable(bufnr)
    end)
    pcall(vim.api.nvim_command, "UfoDisable")
    pcall(vim.api.nvim_command, "NoMatchParen")
    -- if vim.opt_local.eventignore == nil then
    --     vim.opt_local.eventignore = {}
    -- end
    -- vim.opt_local.eventignore:append(EVENTS)

    if _type == FILE_TYPE.READ_ONLY then
        vim.opt_local.buftype = "nowrite"
    end
end

return {
    is_large_file = is_large_file,
    FILE_TYPE = FILE_TYPE,
    optimize_buffer = optimize_buffer,
}
