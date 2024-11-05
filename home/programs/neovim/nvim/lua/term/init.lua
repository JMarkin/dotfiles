local term = require("term.terminal")

vim.api.nvim_create_user_command("Tterm", function(input)
    term.open(input.args)
end, { nargs = "*" })

vim.api.nvim_create_user_command("Sterm", function(input)
    term.open(input.args, "split")
end, { nargs = "*" })

vim.api.nvim_create_user_command("Vterm", function(input)
    term.open(input.args, "vsplit")
end, { nargs = "*" })

function term_open()
    local bufnr = vim.api.nvim_get_current_buf()
    if string.find(vim.fn.bufname(bufnr), "term://") ~= nil then
        term.open(nil, "vsplit")
        vim.cmd("vertical resize +15")
    else
        term.open(nil, "split")
        vim.cmd("horizontal resize -15")
    end
end

vim.keymap.set("n", "<A-t>", term_open, { desc = "Open terminal" })
vim.keymap.set("t", "<A-t>", term_open, { desc = "Open terminal" })

vim.keymap.set("n", "<A-g>", function()
    local bufnr = term.open("lazygit", nil)
    vim.keymap.del("t", "<esc>", { buffer = bufnr })
end, { desc = "Lazygit" })

vim.keymap.set("n", "<A-a>", function()
    local bufnr = term.open("oatmeal -e neovim --model phi3:14b-medium-128k-instruct-q4_1", nil)
    vim.keymap.del("t", "<esc>", { buffer = bufnr })
end, { desc = "Oatmeal" })
