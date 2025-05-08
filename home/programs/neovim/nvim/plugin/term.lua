local term = require("terminal")

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

-- vim.keymap.set("n", "<space>o", function()
--     local bufnr = term.open("oatmeal -e neovim --model phi4:latest", nil)
--     vim.keymap.del("t", "<esc>", { buffer = bufnr })
-- end, { desc = "Oatmeal" })

vim.keymap.set("n", "<space>k", function()
  local out = vim.system({ "fd", "-a", "--glob", "*yaml", vim.env.HOME .. "/.kube/configs" }, { text = true }):wait()
  local selects = {}
  for segment in string.gmatch(out.stdout, "[^\n]+") do
    table.insert(selects, segment)
  end

  vim.ui.select(selects, {
    prompt = "Select kubeconfig:",
    format_item = function(item)
      return item
    end,
  }, function(choice)
    if not choice then
      return
    end
    term.open(string.format("k9s --insecure-skip-tls-verify --all-namespaces --kubeconfig %s", choice), nil)
  end)
end, { desc = "K9S" })
