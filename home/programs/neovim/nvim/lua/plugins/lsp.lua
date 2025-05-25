local is_not_mini = require("funcs").is_not_mini

return {
  {
    "neovim/nvim-lspconfig",
    cond = is_not_mini,
    event = vim.g.pre_load_events,
    lazy = true,
  },
  {
    "folke/lazydev.nvim",
    opts = {
      library = {
        { path = "luvit-meta/library", words = { "vim%.uv" } },
      },
    },
    ft = "lua",
  },
  {
    "j-hui/fidget.nvim",
    event = "LspAttach",
    opts = {
      -- options
    },
  },
}
