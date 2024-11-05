local CFG = require("extend-netrw.float-preview.config")
local get_node = require("extend-netrw.funcs").get_node
local maxline = require("funcs").maxline

local FloatPreview = {}
FloatPreview.__index = FloatPreview

local preview_au = "float_preview_au"
vim.api.nvim_create_augroup(preview_au, { clear = true })

local st = {}
local all_floats = {}
local disabled = false

-- original fzf lua
local read_file_async = function(filepath, callback)
    vim.loop.fs_open(filepath, "r", 438, function(err_open, fd)
        if err_open then
            -- we must schedule this or we get
            -- E5560: nvim_exec must not be called in a lua loop callback
            vim.schedule(function()
                vim.notify(("Unable to open file '%s', error: %s"):format(filepath, err_open), vim.log.levels.WARN)
            end)
            return
        end
        vim.loop.fs_fstat(fd, function(err_fstat, stat)
            assert(not err_fstat, err_fstat)
            if stat.type ~= "file" then
                return callback("")
            end
            vim.loop.fs_read(fd, stat.size, 0, function(err_read, data)
                assert(not err_read, err_read)
                vim.loop.fs_close(fd, function(err_close)
                    assert(not err_close, err_close)
                    return callback(data)
                end)
            end)
        end)
    end)
end

function FloatPreview.is_float(bufnr, path)
    if path then
        return st[path] ~= nil
    end
    if not bufnr then
        bufnr = vim.api.nvim_get_current_buf()
    end

    return st[bufnr] ~= nil
end

local function all_close()
    for _, fl in pairs(all_floats) do
        fl:_close("all_close")
    end
end

FloatPreview.close = all_close

local function all_open()
    for _, fl in pairs(all_floats) do
        fl:preview_under_cursor()
    end
end

function FloatPreview.attach_netrw(bufnr)
    local exists = all_floats[bufnr]
    if exists ~= nil then
        return
    end
    -- vim.notify(string.format("attached: %s", bufnr))
    local prev = FloatPreview:new()
    prev:attach(bufnr)
    all_open()
    return prev
end

function FloatPreview.toggle()
    disabled = not disabled
    if disabled then
        all_close()
    else
        all_open()
    end
end

function FloatPreview:new(cfg)
    local prev = {}
    setmetatable(prev, FloatPreview)

    cfg = cfg or CFG.config()
    prev.buf = nil
    prev.win = nil
    prev.path = nil
    prev.current_line = 1
    prev.max_line = 999999
    prev.disabled = false
    prev.cfg = cfg
    return prev
end

function FloatPreview:_close(reason)
    if self.path ~= nil and self.buf ~= nil then
        if reason then
            -- vim.notify(string.format("fp close %s", reason))
        end
        vim.api.nvim_win_close(self.win, true)
        self.win = nil
        st[self.buf] = nil
        st[self.path] = nil
        self.buf = nil
        self.path = nil
        self.current_line = 1
        self.max_line = 999999
    end
end

function FloatPreview:preview(path)
    if disabled then
        return
    end

    if not self.cfg.hooks.pre_open(path) then
        return
    end

    self.path = path
    self.buf = vim.api.nvim_create_buf(false, false)
    st[self.path] = 1
    st[self.buf] = 1

    vim.api.nvim_set_option_value("bufhidden", "wipe", { buf = self.buf })
    vim.api.nvim_set_option_value("buftype", "nofile", { buf = self.buf })
    vim.api.nvim_set_option_value("buflisted", false, { buf = self.buf })

    local width = vim.api.nvim_get_option_value("columns", {})
    local max_ = maxline(path)
    local height = vim.api.nvim_get_option_value("lines", {})
    local prev_height = math.ceil(height / 3)
    local prev_width = math.ceil(width / 2)
    if prev_width > max_ then
        prev_width = max_ + 1
    end

    local f_len = #vim.fn.getline(".")

    local ra = "N"
    if vim.fn.winline() > vim.fn.winheight(0) - prev_height then
        ra = "S"
    end
    local ca = "W"
    if vim.fn.wincol() > vim.fn.winwidth(0) - prev_width then
        ca = "E"
    end
    local anchor = ra .. ca

    local row, col = 0, f_len + 1
    if ca == "E" then
        col = col * -1
    end

    local opts = {
        width = prev_width,
        height = prev_height,
        row = row,
        col = col,
        anchor = anchor,
        focusable = false,
        noautocmd = true,
        style = self.cfg.window.style,
        relative = self.cfg.window.relative,
        border = self.cfg.window.border,
    }

    local open_win_config = self.cfg.window.open_win_config
    if type(open_win_config) == "function" then
        open_win_config = open_win_config()
    end

    if open_win_config then
        for k, v in pairs(open_win_config) do
            opts[k] = v
        end
    end

    self.win = vim.api.nvim_open_win(self.buf, true, opts)
    vim.api.nvim_set_option_value("wrap", self.cfg.window.wrap, { win = self.win })

    read_file_async(
        path,
        vim.schedule_wrap(function(data)
            if not self.buf then
                return
            end
            local lines = vim.split(data, "[\r]?\n")

            -- if file ends in new line, don't write an empty string as the last
            -- line.
            if data:sub(#data, #data) == "\n" or data:sub(#data - 1, #data) == "\r\n" then
                table.remove(lines)
            end
            self.max_line = #lines
            if self.cfg.window.trim_height then
                if self.max_line < prev_height then
                    opts.height = self.max_line + 1
                    opts.noautocmd = nil
                    vim.api.nvim_win_set_config(self.win, opts)
                end
            end
            vim.api.nvim_buf_set_lines(self.buf, 0, -1, false, lines)
            vim.b[self.buf]._float_preview = 1

            local ft = vim.filetype.match({ buf = self.buf, filename = path })
            if not ft then
                return
            end
            vim.bo[self.buf].ft = ft

            local has_ts, lang = pcall(vim.treesitter.language.get_lang, ft)
            if has_ts then
                has_ts, _ = pcall(vim.treesitter.start, self.buf, has_ts and lang or ft)
            end

            local syntax_ = vim.g.syntax_on or vim.g.syntax_manual

            if not has_ts and syntax_ then
                vim.bo[self.buf].syntax = ft
            end
        end)
    )
    if not self.cfg.hooks.post_open(self.buf) then
        self:_close("post open")
    end
end

function FloatPreview:preview_under_cursor(rewrite)
    if rewrite == nil then
        rewrite = false
    end
    local _, node = pcall(get_node)

    if not node then
        return
    end

    if node.absolute_path == self.path and not rewrite then
        -- print(node.absolute_path, self.path)
        return
    end
    self:_close("change file")

    if node.type ~= "file" then
        return
    end

    local win = vim.api.nvim_get_current_win()
    self:preview(node.absolute_path)

    local ok, _ = pcall(vim.api.nvim_set_current_win, win)
    if not ok then
        self:_close("can't set win")
    end
end

function FloatPreview:scroll(line)
    if self.win then
        vim.api.nvim_win_set_cursor(self.win, { line, 0 })
        self.current_line = line
        -- print(line)
        -- print(vim.api.nvim_win_get_cursor(self.win))
    end
end

function FloatPreview:scroll_down()
    if self.buf then
        local next_line = math.min(self.current_line + self.cfg.scroll_lines, self.max_line)
        self:scroll(next_line)
    end
end

function FloatPreview:scroll_up()
    if self.buf then
        local next_line = math.max(self.current_line - self.cfg.scroll_lines, 1)
        self:scroll(next_line)
    end
end

function FloatPreview:attach(bufnr)
    for _, key in ipairs(self.cfg.mapping.up) do
        vim.keymap.set("n", key, function()
            self:scroll_up()
        end, { buffer = bufnr })
    end

    for _, key in ipairs(self.cfg.mapping.down) do
        vim.keymap.set("n", key, function()
            self:scroll_down()
        end, { buffer = bufnr })
    end

    for _, key in ipairs(self.cfg.mapping.toggle) do
        vim.keymap.set("n", key, function()
            FloatPreview.toggle()
        end, { buffer = bufnr })
    end
    local au = {}

    table.insert(
        au,
        vim.api.nvim_create_autocmd({ "CursorHold" }, {
            group = preview_au,
            callback = function()
                if bufnr == vim.api.nvim_get_current_buf() then
                    self:preview_under_cursor()
                else
                    self:_close("changed buffer")
                end
            end,
        })
    )

    vim.api.nvim_create_autocmd({ "BufWipeout" }, {
        buffer = bufnr,
        group = preview_au,
        callback = function()
            self:_close("wipe")
            if all_floats[bufnr] ~= nil then
                all_floats[bufnr] = nil
            end
            for _, au_id in pairs(au) do
                vim.api.nvim_del_autocmd(au_id)
            end
            self = nil
        end,
    })

    all_floats[bufnr] = self
end

return FloatPreview
