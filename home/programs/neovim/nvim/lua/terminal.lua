local Terminal = {}

Terminal.close_augroup = "close_augroup"

Terminal.set_keymaps = function(winnr, bufnr)
  local opts = { buffer = bufnr }

  vim.keymap.set("t", "<c-\\><c-\\>", [[<C-\><C-n>]], opts)
  vim.keymap.set("t", "<C-h>", [[<C-\><C-N><C-w>h]], opts)
  vim.keymap.set("t", "<C-j>", [[<C-\><C-N><C-w>j]], opts)
  vim.keymap.set("t", "<C-k>", [[<C-\><C-N><C-w>k]], opts)
  vim.keymap.set("t", "<C-l>", [[<C-\><C-N><C-w>l]], opts)

  vim.keymap.set("t", "<C-w>", [[<C-\><C-n><C-w>]], opts)

  vim.keymap.set({ "n" }, { "<A-q>", "<leader>q", "<space>q" }, function()
    vim.api.nvim_win_close(winnr, true)
  end, opts)
  vim.keymap.set({ "t" }, { "<A-q>" }, function()
    vim.api.nvim_win_close(winnr, true)
  end, opts)
end

Terminal.configure = function()
  -- vim.bo[bufnr].buflisted = false
  -- vim.opt_local.bufhidden = "wipe"
  vim.opt_local.swapfile = false
  vim.opt_local.number = false
  vim.opt_local.relativenumber = false
  vim.opt_local.winfixbuf = false
  vim.opt_local.winfixheight = true
  vim.opt_local.winfixwidth = true
end

local au_id = vim.api.nvim_create_augroup("terminal_nvim", { clear = true })

vim.api.nvim_create_autocmd({ "WinEnter", "BufWinEnter", "TermOpen" }, {
  group = au_id,
  callback = function(args)
    if vim.startswith(vim.api.nvim_buf_get_name(args.buf), "term://") then
      vim.cmd("startinsert!")
    end
  end,
})

vim.api.nvim_create_autocmd({ "TermClose" }, {
  callback = function(params)
    vim.schedule(function()
      vim.api.nvim_buf_delete(params.buf, { force = true })
    end)
    vim.cmd("let &stl = &stl") -- redrawstatus | redrawtabline
  end,
  group = au_id,
  desc = "on_term_close",
})

vim.api.nvim_create_autocmd({ "TermOpen" }, {
  callback = function(params)
    if vim.b[params.buf]["term_ignore"] == true then
      return
    end
    Terminal.configure()
    local winnr = vim.api.nvim_get_current_win()
    Terminal.set_keymaps(winnr, params.buf)
  end,
  group = au_id,
  desc = "on_term_open",
})

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

  return bufnr
end

return Terminal
