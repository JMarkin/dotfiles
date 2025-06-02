return {
  {
    "folke/which-key.nvim",
    event = "VeryLazy",
    enabled = true,
    opts_extend = { "spec" },
    opts = {
      defaults = {},
      preset = "helix",
      keys = {
        scroll_down = "<c-d>", -- binding to scroll down inside the popup
        scroll_up = "<c-e>", -- binding to scroll up inside the popup
      },
      spec = {
        {
          mode = { "n", "v" },
          { "<leader>d", group = "dap" },
          { "<leader>g", group = "git" },
          { "<leader>s", group = "search" },
          { "<leader>l", group = "lang", icon = { icon = "󱖫 ", color = "green" } },
          { "[", group = "prev" },
          { "]", group = "next" },
          { "g", group = "goto" },
          { "gz", group = "surround" },
          { "z", group = "fold" },
          { "m", group = "mark" },
          { "M", group = "mark" },
          { "dm", group = "mark" },
          { "<Leader>lc", group = "copy_as" },
          { "<Leader>lt", group = "tests" },
          { "<Leader>h", group = "http" },
          {
            "<space>b",
            group = "buffer",
            expand = function()
              return require("which-key.extras").expand.buf()
            end,
          },
        },
      },
      triggers = {
        { "<auto>", mode = "nixsotc" },
      },
    },
    keys = {
      {
        "<leader>?",
        function()
          require("which-key").show({ global = false })
        end,
        desc = "Buffer Keymaps (which-key)",
      },
      {
        "<c-w><space>",
        function()
          require("which-key").show({ keys = "<c-w>", loop = true })
        end,
        desc = "Window Hydra Mode (which-key)",
      },
    },
    config = function(_, opts)
      local wk = require("which-key")
      wk.setup(opts)
    end,
  },
  {
    "max397574/better-escape.nvim",
    enabled = false,
    config = function()
      require("better_escape").setup({
        default_mappings = false,
        mappings = {
          i = {
            j = {
              k = "<Esc>",
              j = "<Esc>",
            },
          },
          c = {
            j = {
              k = "<C-c>",
              j = "<C-c>",
            },
          },
          t = {
            j = {
              k = "<C-\\><C-n>",
            },
          },
          v = {
            j = {
              k = "<Esc>",
            },
          },
          s = {
            j = {
              k = "<Esc>",
            },
          },
        },
      })
    end,
  },
}
