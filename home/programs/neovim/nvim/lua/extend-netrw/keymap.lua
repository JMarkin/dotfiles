local funcs = require("extend-netrw.funcs")

local M = {}

M.init = function(buffer)
    if vim.fn.mapcheck("<c-l>") == funcs.reload then
        vim.keymap.del("n", "<c-l>", { buffer = buffer })
        vim.keymap.del("n", "p", { buffer = buffer })
        vim.keymap.del("n", "P", { buffer = buffer })
    end

    vim.keymap.set("n", "<c-r>", funcs.reload, { silent = true, nowait = true, buffer = buffer })
    vim.keymap.set("n", "q", funcs.close, { silent = true, nowait = true, buffer = buffer })
    vim.keymap.set("n", "<space>f", funcs.close, { silent = true, nowait = true, buffer = buffer })
    vim.keymap.set("n", "<leader>f", funcs.close, { silent = true, nowait = true, buffer = buffer })
    vim.keymap.set("n", "<tab>", funcs.open, { silent = true, nowait = true, buffer = buffer })
    vim.keymap.set("n", "<s-tab>", funcs.prev, { silent = true, nowait = true, buffer = buffer })

    vim.keymap.set("n", "I", funcs.debug, { silent = true, nowait = true, buffer = buffer })
end

return M
