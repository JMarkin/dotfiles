local M = {}

local close = ":Rexplore<cr>"
local reload = "<Plug>NetrwRefresh"
local open = "<Plug>NetrwLocalBrowseCheck"
local prev = "<Plug>NetrwBrowseUpDir"

M.init = function(buffer)
    if vim.fn.mapcheck("<c-l>") == reload then
        vim.keymap.del("n", "<c-l>", { buffer = buffer })
        vim.keymap.del("n", "p", { buffer = buffer })
        vim.keymap.del("n", "P", { buffer = buffer })
    end

    vim.keymap.set("n", "<c-r>", reload, { silent = true, nowait = true, buffer = buffer })
    vim.keymap.set("n", "q", close, { silent = true, nowait = true, buffer = buffer })
    vim.keymap.set("n", "<space>f", close, { silent = true, nowait = true, buffer = buffer })
    vim.keymap.set("n", "<leader>f", close, { silent = true, nowait = true, buffer = buffer })
    vim.keymap.set("n", "<tab>", open, { silent = true, nowait = true, buffer = buffer })
    vim.keymap.set("n", "<s-tab>", prev, { silent = true, nowait = true, buffer = buffer })
end

return M
