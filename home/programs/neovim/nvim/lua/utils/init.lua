local M = {}

local uv = vim.uv or vim.loop

M.is_win = function()
    return vim.fn.has("win32") == 1 or vim.fn.has("win64") == 1
end

function M.is_darwin()
    return uv.os_uname().sysname == "Darwin"
end

return M
