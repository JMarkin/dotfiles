local Terminal = {}

Terminal.close_augroup = "close_augroup"

Terminal.set_keymaps = function(winnr, bufnr, command)
    local opts = { buffer = bufnr }

    if not string.find(command, "fish") then
        vim.keymap.set("t", "<esc>", [[<C-\><C-n>]], opts)
    end

    vim.keymap.set("t", "<C-h>", [[<C-\><C-N><C-w>h]], opts)
    vim.keymap.set("t", "<C-j>", [[<C-\><C-N><C-w>j]], opts)
    vim.keymap.set("t", "<C-k>", [[<C-\><C-N><C-w>k]], opts)
    vim.keymap.set("t", "<C-l>", [[<C-\><C-N><C-w>l]], opts)

    vim.keymap.set("t", "<C-w>", [[<C-\><C-n><C-w>]], opts)

    local close = function()
        require("bufdel").delete_buffer_expr(nil, true)
        vim.api.nvim_win_close(winnr, true)
    end

    vim.keymap.set({ "n" }, { "<A-q>", "<leader>q", "<space>q" }, close, opts)
    vim.keymap.set({ "t" }, { "<A-q>" }, close, opts)
end

Terminal.configure = function(winnr, bufnr)
    -- vim.bo[bufnr].buflisted = false
    -- vim.opt_local.bufhidden = "wipe"
    vim.opt_local.swapfile = false
    vim.opt_local.number = false
    vim.opt_local.relativenumber = false
    vim.opt_local.winfixbuf = false
    vim.opt_local.winfixheight = true
    vim.opt_local.winfixwidth = true
    vim.cmd("startinsert!")

    -- vim.api.nvim_create_autocmd({ "TermLeave" }, {
    --     callback = function(event)
    --         vim.schedule(function()
    --             vim.api.nvim_win_set_cursor(winnr, { 1, 0 })
    --         end)
    --     end,
    --     buffer = bufnr,
    -- })
end

Terminal.open = function(command, split_dir)
    if command == "" or command == nil then
        local shell = vim.o.shell

        command = shell
    end

    if split_dir == "" or split_dir == nil then
        split_dir = "tabnew"
    end

    vim.cmd(split_dir .. " | redraw! | terminal " .. command)

    local bufnr = vim.api.nvim_get_current_buf()
    local winnr = vim.api.nvim_get_current_win()

    Terminal.set_keymaps(winnr, bufnr, command)
    Terminal.configure(winnr, bufnr)

    return bufnr
end

return Terminal
