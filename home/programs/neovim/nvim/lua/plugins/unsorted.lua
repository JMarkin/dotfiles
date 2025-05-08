return {
  "antoinemadec/FixCursorHold.nvim",

  {
    "dstein64/vim-startuptime",
    cmd = { "StartupTime" },
    init = function()
      vim.g.startuptime_tries = 10
    end,
  },
  -- sudo
  {
    "lambdalisue/suda.vim",
    cmd = { "SudaRead", "SudaWrite" },
  },
  {
    "gbprod/stay-in-place.nvim",
    opts = {
      set_keymaps = true,
      preserve_visual_selection = true,
    },
    event = "ModeChanged",
  },

  {
    "m4xshen/hardtime.nvim",
    event = "VeryLazy",
    enabled = false,
    dependencies = { "MunifTanjim/nui.nvim", "nvim-lua/plenary.nvim" },
    opts = {
      disabled_filetypes = { "qf", "netrw", "NvimTree", "lazy", "mason", "dashboard", "vista", "vista_kind" },
      disable_mouse = true,
      restriction_mode = "hint",
      disabled_keys = {
        ["<Up>"] = { "n" },
        ["<Left>"] = { "n" },
        ["<Right>"] = { "n" },
        ["<Down>"] = { "n" },
      },
    },
  },
}
