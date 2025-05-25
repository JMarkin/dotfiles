return {
  {
    "rest-nvim/rest.nvim",
    cmd = "Rest",
    ft = "http",
    enabled = false,
    -- dev = true,
    keys = {
      {
        "<leader>hr",
        "<cmd>Rest run<cr>",
        silent = true,
        desc = "run the request under the cursor",
        ft = "http",
      },
      {
        "<leader>hp",
        "<Plug>RestNvimPreview",
        silent = true,
        desc = "preview the request cURL command",
        ft = "http",
      },
      {
        "<leader>hl",
        "<cmd>Rest run last<cr>",
        silent = true,
        desc = "re-run the last request",
        ft = "http",
      },
    },
    -- enabled = false,
    config = function()
      vim.g.rest_nvim = {
        clients = {
          curl = {
            statistics = {
              { id = "remote_ip", winbar = "ip", title = "Remote IP" },
              { id = "time_total", winbar = "time", title = "Time" },
              { id = "time_namelookup", title = "Time dns" },
              { id = "time_connect", title = "Time connect" },
              { id = "time_pretransfer", title = "Time pretransfer" },
              { id = "time_redirect", title = "Time redirect" },
              { id = "time_starttransfer", title = "Time starttransfer" },
              { id = "size_download", title = "Download size", winbar = false },
              { id = "speed_download", title = "Download speed" },
              { id = "size_upload", title = "Upload size" },
              { id = "speed_upload", title = "Upload speed" },
            },
          },
        },
      }
    end,
  },
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
