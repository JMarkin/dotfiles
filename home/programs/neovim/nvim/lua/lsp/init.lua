--
-- https://github.com/neovim/nvim-lspconfig/blob/master/doc/configs.md

if vim.env.NVIM_MINI ~= nil then
  return
end

local lsps = {
  "nginx_language_server",
  "nil_ls",
  "lua_ls",
  "rust_analyzer",
  "bashls",
  "vimls",
  "html",
  "cssls",
  "jedi_language_server",
  "ruff",
  "basedpyright",
  "taplo",
  "ts_ls",
  "neocmake",
  "docker_compose_language_service",
  "dockerls",
  "biome",
  "jinja_lsp",
  "gopls",
  "golangci_lint_ls",
  "vacuum",
  "yamlls",
  "jsonls",
  "clangd",
}

for _, lsp in ipairs(lsps) do
  local cmd = vim.lsp.config[lsp].cmd[1]

  if vim.fn.executable(cmd) == 1 then
    vim.lsp.enable(lsp, vim.g.lsp_autostart)
  end
end

-- vim.lsp.handlers["workspace/diagnostic/refresh"] = function(_, _, ctx)
--   local ns = vim.lsp.diagnostic.get_namespace(ctx.client_id)
--   local bufnr = vim.api.nvim_get_current_buf()
--   vim.diagnostic.reset(ns, bufnr)
--   return true
-- end

vim.diagnostic.config({
  underline = true,
  signs = true,
  virtual_text = false,
  -- virtual_lines = { only_current_line = true },
  float = true,
  update_in_insert = false,
  severity_sort = true,
})

require("lsp.utils")
