local Terminal = {}

Terminal.close_augroup = "close_augroup"

Terminal.set_keymaps = function(bufnr, command)
    local opts = { buffer = bufnr }

    if command ~= "fish" then
        vim.keymap.set("t", "<esc>", [[<C-\><C-n>]], opts)
    end
    vim.keymap.set("t", "<C-h>", [[<Cmd>wincmd h<CR>]], opts)
    vim.keymap.set("t", "<C-j>", [[<Cmd>wincmd j<CR>]], opts)
    vim.keymap.set("t", "<C-k>", [[<Cmd>wincmd k<CR>]], opts)
    vim.keymap.set("t", "<C-l>", [[<Cmd>wincmd l<CR>]], opts)
    vim.keymap.set("t", "<C-w>", [[<C-\><C-n><C-w>]], opts)
end

Terminal.configure = function(bufnr)
    vim.bo[bufnr].buflisted = false
    vim.opt_local.bufhidden = "unload"
    vim.opt_local.swapfile = false
    vim.opt_local.number = false
    vim.opt_local.relativenumber = false
    vim.opt_local.winfixbuf = true
    vim.opt_local.winfixheight = true
    vim.opt_local.winfixwidth = true
    vim.cmd("startinsert!")
end

Terminal.open = function(command, split_dir)
    if command == "" or command == nil then
        local shell = vim.o.shell

        if vim.fn.executable("fish") then
            shell = "fish"
        end
        command = shell
    end

    if split_dir == "" or split_dir == nil then
        split_dir = "tabnew"
    end

    vim.cmd(split_dir .. " | redraw! | terminal " .. command)

    local bufnr = vim.api.nvim_get_current_buf()

    vim.api.nvim_create_autocmd({ "TermClose" }, {
        callback = function()
            pcall(vim.cmd, "quit")
        end,
        buffer = bufnr,
    })

    Terminal.set_keymaps(bufnr, command)
    Terminal.configure(bufnr)

    return bufnr
end

return Terminal
