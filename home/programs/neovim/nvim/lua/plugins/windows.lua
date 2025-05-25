return {
  {
    "yorickpeterse/nvim-window",
    keys = {
      {
        "<space>w",
        function()
          require("nvim-window").pick()
        end,
        silent = true,
        desc = "Windows: pick",
        mode = { "n", "v" },
      },
    },
  },
  {
    "ycdzj/win-mover.nvim",
    keys = {
      {
        "<space>m",
        function(ev)
          return require("win-mover").enter_move_mode(ev)
        end,
        desc = "Window: mover",
      },
    },
    config = function()
      local win_mover = require("win-mover")
      win_mover.setup({
        ignore = {
          enable = true,
          filetypes = { "vista" },
        },
        move_mode = {
          keymap = {
            h = win_mover.ops.move_left,
            j = win_mover.ops.move_down,
            k = win_mover.ops.move_up,
            l = win_mover.ops.move_right,

            H = win_mover.ops.move_far_left,
            J = win_mover.ops.move_far_down,
            K = win_mover.ops.move_far_up,
            L = win_mover.ops.move_far_right,

            q = win_mover.ops.quit,
            ["<Esc>"] = win_mover.ops.quit,
          },
        },
      })
    end,
  },
}
