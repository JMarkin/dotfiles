local autocmd = vim.api.nvim_create_autocmd
local groupid = vim.api.nvim_create_augroup


local M = {}
-- copy from https://github.com/Bekaboo/nvim/blob/master/lua/core/autocmds.lua
---@param group string
---@vararg { [1]: string|string[], [2]: vim.api.keyset.create_autocmd }
---@return nil
M.augroup = function(group, ...)
    local id = groupid(group, { clear = true })
    for _, a in ipairs({ ... }) do
        a[2].group = id
        autocmd(unpack(a))
    end
end

M.pcall_notify = function(func)
    local ok, out = pcall(func)
    if not ok then
        vim.notify_once(string.format("%s", out), vim.log.levels.DEBUG)
    end
    return out
end

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

-- Executes a user-supplied "reducer" callback function on each element of the table indexed with a numeric key, in order, passing in the return value from the calculation on the preceding element
M.ireduce = function(tbl, func, acc)
    for i, v in ipairs(tbl) do
        acc = func(acc, v, i)
    end
    return acc
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

-- Function to merge two tables in Lua using Neovim.
function M.merge_tables(table1, table2)
    local merged_table = table1 or {} -- Ensure a valid table, even if nil
    for k, _ in pairs(table2) do
        merged_table[k] = table2[k]
    end

    -- Return the merged table.
    return merged_table
end

function M.debounce(ms, func)
    local entry = { timer = nil, cancel = nil }

    entry.timer = vim.uv.new_timer()
    entry.timer:start(
        ms,
        0,
        vim.schedule_wrap(function()
            entry.cancel = func()
        end)
    )

    return entry
end

return M
