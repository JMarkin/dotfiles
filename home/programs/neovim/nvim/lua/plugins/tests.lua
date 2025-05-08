local is_not_mini = require("funcs").is_not_mini
return {
  "nvim-neotest/neotest",
  cond = is_not_mini,
  dependencies = {
    "nvim-neotest/nvim-nio",
    "nvim-lua/plenary.nvim",
    "nvim-treesitter/nvim-treesitter",
    "antoinemadec/FixCursorHold.nvim",
    "nvim-neotest/neotest-python",
    "nvim-dap-ui",
    "fredrikaverpil/neotest-golang",
  },
  keys = {
    {
      "<leader>lt",
      function()
        require("neotest").summary.toggle()
      end,
      desc = "Tests",
    },
    {
      "<leader>lr",
      function()
        require("neotest").summary.run()
      end,
      desc = "Tests run nearest",
    },
  },
  opts = {
    output_panel = {
      enabled = true,
      open = "botright split | resize 15",
    },
    summary = {
      animated = true,
      count = true,
      enabled = true,
      expand_errors = true,
      follow = true,
      mappings = {
        attach = "a",
        clear_marked = "M",
        clear_target = "T",
        debug = "d",
        debug_marked = "D",
        expand = { "<CR>", "<2-LeftMouse>", "za" },
        expand_all = { "zA" },
        help = "?",
        jumpto = "i",
        mark = "m",
        next_failed = "]f",
        output = "o",
        prev_failed = "[f",
        run = "r",
        run_marked = "R",
        short = "O",
        stop = "u",
        target = "t",
        watch = "w",
      },
      open = "botright vsplit | vertical resize 50",
    },
    consumers = {
      always_open_output = function(client)
        local async = require("neotest.async")

        client.listeners.results = function(adapter_id, results)
          require("neotest").output_panel.open()
        end
      end,
    },
  },
  config = function(_, opts)
    opts.adapters = {
      require("neotest-python")({
        args = { "-vv" },
      }),
      require("rustaceanvim.neotest"),
      require("neotest-golang"),
    }
    require("neotest").setup(opts)
  end,
  cmd = { "Neotest" },
}
