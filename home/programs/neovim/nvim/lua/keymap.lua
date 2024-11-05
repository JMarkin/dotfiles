local is_not_mini = require("funcs").is_not_mini
--
-- system clipboard
vim.keymap.set({ "n", "v" }, "<leader>y", '"+y')
vim.keymap.set({ "n" }, "<leader>Y", '"+y$')

vim.keymap.set({ "n", "v" }, "<leader>p", '"+p')
vim.keymap.set({ "n", "v" }, "<leader>P", '"+P')

vim.keymap.set({ "n" }, { "<leader>q", "<space>q" }, ":q<cr>", { desc = "Quit", silent = true })
vim.keymap.set({ "n", "v" }, "<C-e>", "<C-u>")

vim.keymap.set({ "n" }, "o", "o<Esc>", { desc = "Add line under" })
vim.keymap.set({ "n" }, "O", "O<Esc>", { desc = "Add line prev" })
vim.keymap.set({ "v" }, "p", "pgvy", { desc = "Disable yank on paste" })

vim.keymap.set({ "n" }, { "<leader>w", "<leader>'" }, ":w<CR>", { silent = true, desc = "normal mode: save" })
vim.keymap.set(
    { "v" },
    { "<leader>w", "<leader>'" },
    "<Esc>:w<CR>",
    { desc = "visual mode: escape to normal and save", silent = true }
)

vim.keymap.set({ "n" }, { "<leader>W" }, ":wa<CR>", { silent = true, desc = "normal mode: save" })
vim.keymap.set(
    { "v" },
    { "<leader>W" },
    "<Esc>:wa<CR>",
    { silent = true, desc = "visual mode: escape to normal and save" }
)

vim.api.nvim_create_user_command("InstallDefault", function(_)
    vim.cmd.TSInstallDefault()
    vim.cmd.ExternalInstallDefault()
end, {})

vim.api.nvim_create_user_command("UpdateDefault", function(_)
    vim.cmd.TSInstallDefault()
    vim.cmd.ExternalUpdateDefault()
end, {})

vim.api.nvim_create_user_command("UnicodeUndoEscape", function(_)
    vim.cmd([[:%s/\\u\(\x\{4\}\)/\=nr2char('0x'.submatch(1),1)/g]])
end, {})

-- Tabpages
---@param tab_action function
---@param default_count number?
---@return function
local function tabswitch(tab_action, default_count)
    return function()
        local count = default_count or vim.v.count
        local num_tabs = vim.fn.tabpagenr("$")
        if num_tabs >= count then
            tab_action(count ~= 0 and count or nil)
            return
        end
        vim.cmd.tablast()
    end
end
vim.keymap.set({ "n", "x" }, "gt", tabswitch(vim.cmd.tabnext), { desc = "Tabs: next" })
vim.keymap.set({ "n", "x" }, "gT", tabswitch(vim.cmd.tabprev), { desc = "Tabs: prev" })
vim.keymap.set({ "n", "x" }, "gy", tabswitch(vim.cmd.tabprev), { desc = "Tabs: prev" }) -- gT is too hard to press

vim.keymap.set("n", "<space>t", ":$tabnew<CR>", { desc = "Tabs: new" })
vim.keymap.set("n", "<space>d", ":tabclose<CR>", { desc = "Tabs: close" })
vim.keymap.set("n", "<space>D", ":tabonly<CR>", { desc = "Tabs: close other tabs" })
vim.keymap.set("n", "<space>[", ":-tabmove<CR>", { desc = "Tabs: move to prev" })
vim.keymap.set("n", "<space>]", ":+tabmove<CR>", { desc = "Tabs: move to next" })

for i = 1, 9, 1 do
    vim.keymap.set({ "n", "x" }, "<space>" .. i, tabswitch(vim.cmd.tabnext, i), { desc = "Tabs: go to " .. i })
end

vim.keymap.set("n", "<space>f", "<cmd>Explore<cr>", { noremap = true, desc = "Netrw: open" })
vim.keymap.set("n", "<leader>f", "<cmd>Explore %:p:h<cr>", { noremap = true, desc = "Netrw: open current file" })

vim.keymap.set("n", "<leader>lcl", function()
    local s = string.format("%s:%s", vim.fn.expand("%"), vim.fn.line("."))
    vim.notify(string.format("Copied reference: %s", s))
    vim.fn.setreg("+", s)
end, { noremap = true, desc = "Copy as: line" })

vim.cmd([[command CDC lcd %:p:h]])
