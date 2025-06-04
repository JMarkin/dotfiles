return {
  {
    {
      "mistweaverco/kulala.nvim",
      -- from nix
      dir = vim.fn.stdpath("data") .. "/nix/kulala.nvim",
      dev = true,
      pin = true,
      keys = {
        { "<leader>hr", desc = "Send request" },
        { "<leader>ha", desc = "Send all requests" },
        { "<leader>hb", desc = "Open scratchpad" },
      },
      ft = { "http", "rest" },
      opts = {
        -- your configuration comes here
        global_keymaps = {
          ["Send request"] = { -- sets global mapping
            "<leader>hr",
            function()
              require("kulala").run()
            end,
            mode = { "n", "v" }, -- optional mode, default is n
            desc = "Send request", -- optional description, otherwise inferred from the key
          },
          ["Send all requests"] = {
            "<leader>ha",
            function()
              require("kulala").run_all()
            end,
            mode = { "n", "v" },
            ft = "http", -- sets mapping for *.http files only
          },
          ["Replay the last request"] = {
            "<leader>hl",
            function()
              require("kulala").replay()
            end,
            ft = { "http", "rest" }, -- sets mapping for specified file types
          },
          ["Find request"] = false, -- set to false to disable
        },
      },
    },
  },
}
