return {
  {
    "nanozuki/tabby.nvim",
    event = "TabNew",
    config = function()
      require("tabby").setup({
        option = {
          lualine_theme = vim.g.lualine_theme or nil,
          buf_name = { mode = "unique" },
        },
      })
    end,
  },
  {
    "echasnovski/mini.statusline",
    event = vim.g.post_load_events,
    config = function()
      require("mini.statusline").setup()
    end,
  },
}
