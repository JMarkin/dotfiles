local M = {}

M.is_not_mini = function()
    return vim.env.NVIM_MINI == nil
end

M.doau = function(pattern, data)
    vim.api.nvim_exec_autocmds("User", {
        pattern = pattern,
        data = data,
    })
end

function M.maxline(path, break_after)
    if break_after == nil then
        break_after = vim.o.synmaxcol + 1
    end
    local max = 0
    local fd = vim.uv.fs_open(path, "r", 1)
    if not fd then
        return max
    end
    local stat = vim.uv.fs_fstat(fd)
    local data = vim.uv.fs_read(fd, stat.size, nil)
    vim.uv.fs_close(fd)
    if not data then
        return max
    end

    local lines = vim.split(data, "[\r]?\n")

    for _, line in pairs(lines) do
        if max < #line then
            max = #line
        end
        if max >= break_after then
            return max
        end
    end
    return max
end

function M.get_visual()
    local start_pos = vim.fn.getpos("v")
    local end_pos = vim.fn.getpos(".")

    if start_pos == nil or end_pos == nil then
        return ""
    end

    local start_row, start_col = start_pos[2], start_pos[3]
    local end_row, end_col = end_pos[2], end_pos[3]

    if end_row < start_row then
        start_row, end_row = end_row, start_row
    end
    if end_col < start_col then
        start_col, end_col = end_col, start_col
    end

    local lines = vim.api.nvim_buf_get_text(0, start_row - 1, start_col - 1, end_row - 1, end_col, {})

    return table.concat(lines, "\n"), start_row, end_row
end

function M.get_previous_visual()
    local vstart = vim.fn.getpos("'<")
    local vend = vim.fn.getpos("'>")

    if vstart == nil or vend == nil or vend[2] == 0 then
        return ""
    end

    local start_row = vstart[2]
    local end_row = vend[2]
    local select_start_line = start_row

    if select_start_line ~= 0 then
        select_start_line = select_start_line - 1
    end

    local lines = vim.api.nvim_buf_get_lines(0, select_start_line, end_row, true)
    return table.concat(lines, "\n"), start_row, end_row
end

function M.in_visual_mode()
    local modes = {
        Rv = true,
        Rvc = true,
        Rvx = true,
        V = true,
        Vs = true,
        niV = true,
        noV = true,
        nov = true,
        v = true,
        vs = true,
    }
    local current_mode = vim.api.nvim_get_mode()["mode"]
    return modes[current_mode] or false
end

function M.exit_visual()
    vim.api.nvim_feedkeys(vim.api.nvim_replace_termcodes("<ESC>", true, false, true), "i", true)
end

-- https://github.com/mobily/.nvim/blob/main/lua/utils/fn.lua
--
M.switch = function(param, t)
    local case = t[param]
    if case then
        return case()
    end
    local defaultFn = t["default"]
    return defaultFn and defaultFn() or nil
end

-- Executes a user-supplied "reducer" callback function on each element of the table indexed with a numeric key, in order, passing in the return value from the calculation on the preceding element
M.ireduce = function(tbl, func, acc)
    for i, v in ipairs(tbl) do
        acc = func(acc, v, i)
    end
    return acc
end

M.ieach = function(tbl, func)
    for index, element in ipairs(tbl) do
        func(element, index)
    end
end

M.always = function(value)
    return function()
        return value
    end
end

-- Returns the first element in the array that satisfies the provided testing function
M.ifind = function(tbl, func)
    for index, item in ipairs(tbl) do
        if func(item, index) then
            return item
        end
    end

    return nil
end

M.isome = function(tbl, func)
    for index, item in ipairs(tbl) do
        if func(item, index) then
            return true
        end
    end

    return false
end

M.trim = function(str)
    return (str:gsub("^%s*(.-)%s*$", "%1"))
end

M.ifilter = function(tbl, func)
    return vim.tbl_filter(func, tbl)
end

-- Creates a new table populated with the results of calling a provided functions on every numeric indexed element in the calling table
M.imap = function(tbl, func)
    return M.ireduce(tbl, function(new_tbl, value, index)
        table.insert(new_tbl, func(value, index))
        return new_tbl
    end, {})
end

M.to_macos_keys = function(keymap)
    return keymap
        :gsub("CR", "↩")
        :gsub("<", "")
        :gsub(">", "")
        :gsub("-", " ")
        :gsub("D", "⌘")
        :gsub("A", "⌥")
        :gsub("C", "⌃")
        :gsub("BS", "⌫")
        :gsub("leader", vim.g.mapleader .. " ")
end

vim.api.nvim_create_user_command("Jaq", function(opts)
    local bufnr = vim.api.nvim_get_current_buf()
    local path = vim.api.nvim_buf_get_name(bufnr)

    if #opts.fargs > 0 then
        path = path
    end

    local fzflua = require("fzf-lua")

    local function jaq_fzf(jaq_query)
        fzflua.fzf_exec(string.format("jaq -c '%s' %s", jaq_query, path), {
            multiprocess = true,
            prompt = string.format("%s > ", jaq_query),
            fzf_opts = {
                ["--preview"] = "echo -e {} | fixjson | bat --style numbers",
            },
            actions = {
                ---@diagnostic disable-next-line: unused-local
                ["default"] = function(selected, _opts)
                    fzflua.grep_curbuf({
                        multiprocess = true,
                        search = selected[1],
                    })
                end,
            },
            fn_transform = function(x)
                if x == "null" then
                    return
                end
                return x
            end,
        })
    end

    fzflua.fzf_live(string.format("jaq -c '<query>' %s", path), {
        multiprocess = true,
        prompt = "jaq> ",
        fzf_opts = {
            ["--preview"] = "echo -e {} | fixjson | bat --style numbers",
        },
        actions = {
            ---@diagnostic disable-next-line: unused-local
            ["default"] = function(_selected, _opts)
                jaq_fzf(fzflua.get_last_query())
            end,
        },
        fn_transform = function(x)
            if x == "null" then
                return
            end
            return x
        end,
    })
end, {
    nargs = "*",
})

--- Debounces a function on the trailing edge. Automatically
--- `schedule_wrap()`s.
---
--@param fn (function) Function to debounce
--@param timeout (number) Timeout in ms
--@param first (boolean, optional) Whether to use the arguments of the first
---call to `fn` within the timeframe. Default: Use arguments of the last call.
--@returns (function, timer) Debounced function and timer. Remember to call
---`timer:close()` at the end or you will leak memory!
function M.debounce_trailing(fn, ms, first)
    local timer = vim.uv.new_timer()
    local wrapped_fn

    if not first then
        function wrapped_fn(...)
            local argv = { ... }
            local argc = select("#", ...)

            timer:start(ms, 0, function()
                pcall(vim.schedule_wrap(fn), unpack(argv, 1, argc))
            end)
        end
    else
        local argv, argc
        function wrapped_fn(...)
            argv = argv or { ... }
            argc = argc or select("#", ...)

            timer:start(ms, 0, function()
                pcall(vim.schedule_wrap(fn), unpack(argv, 1, argc))
            end)
        end
    end
    return wrapped_fn, timer
end

return M
