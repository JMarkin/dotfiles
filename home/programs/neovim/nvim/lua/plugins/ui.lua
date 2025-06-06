return {
  -- ui components
  { "MunifTanjim/nui.nvim", lazy = true },

  {
    "ibhagwan/smartyank.nvim",
    -- enabled = false,
    event = "ModeChanged",
    opts = {
      highlight = {
        enabled = true, -- highlight yanked text
        timeout = 100,
      },
    },
    config = function(_, opts)
      require("smartyank").setup(opts)
      vim.api.nvim_create_autocmd("FocusGained", {
        callback = function()
          local loaded_content = vim.fn.getreg("+")
          if loaded_content ~= "" then
            vim.fn.setreg('"', loaded_content)
          end
        end,
      })
    end,
  },

  {
    "brenoprata10/nvim-highlight-colors",
    -- enabled = false,
    -- event = vim.g.post_load_events,
    -- event = "VeryLazy",
    opts = {
      render = "foreground",
      exclude_filetypes = { "log" },
    },
    cmd = { "HighlightColors" },
    config = function(_, opts)
      require("nvim-highlight-colors").setup(opts)
    end,
  },

  {
    "DanilaMihailov/beacon.nvim",
    -- enabled = false,
    cond = function()
      return not vim.g.neovide
    end,
    opts = {
      enabled = function()
        local line_count = vim.api.nvim_buf_line_count(vim.api.nvim_get_current_buf())
        if line_count > 1000 then
          return false
        end
        return true
      end, --- (boolean | fun():boolean) check if enabled
      speed = 2, --- integer speed at wich animation goes
      width = 40, --- integer width of the beacon window
      winblend = 70, --- integer starting transparency of beacon window :h winblend
      fps = 60, --- integer how smooth the animation going to be
      min_jump = 10, --- integer what is considered a jump. Number of lines
      cursor_events = { "CursorMoved" }, -- table<string> what events trigger check for cursor moves
      window_events = { "WinEnter", "FocusGained" }, -- table<string> what events trigger cursor highlight
      highlight = { bg = "white", ctermbg = 15 }, -- vim.api.keyset.highlight table passed to vim.api.nvim_set_hl
    },
    event = { "BufAdd" },
  },
  {
    "tzachar/local-highlight.nvim",
    lazy = true,
    -- enabled = false,
    opts = {
      insert_mode = false,
      file_types = {},
    },
  },
  {
    "lewis6991/whatthejump.nvim",
    -- enabled = false,
    keys = { "<C-i>", "<C-o>" },
  },
  {
    "MeanderingProgrammer/render-markdown.nvim",
    ft = { "markdown", "codecompanion", "Avante" },
    opts = {
      file_types = { "markdown", "Avante", "codecompanion" },
    },
  },
  {
    "ramilito/winbar.nvim",
    event = "BufAdd",
    config = function()
      MiniIcons.mock_nvim_web_devicons()

      require("winbar").setup({
        -- your configuration comes here, for example:
        icons = true,
        filetype_exclude = {
          "vista",
          "dbui",
          "help",
          "startify",
          "dashboard",
          "packer",
          "neo-tree",
          "neogitstatus",
          "NvimTree",
          "Trouble",
          "alpha",
          "lir",
          "Outline",
          "spectre_panel",
          "toggleterm",
          "TelescopePrompt",
          "prompt",
          "httpResult",
          "rest_nvim_result",
          "netrw",
          "kulala_ui",
          "AvanteInput",
          "AvanteSelectedFiles",
          "Avante",
          "better_term",
          "oil"
        },
        diagnostics = true,
        buf_modified = true,
        dir_levels = 2,
        -- buf_modified_symbol = "M",
        -- or use an icon
        buf_modified_symbol = "●",
        dim_inactive = {
          enabled = true,
          highlight = "WinbarNC",
          icons = true, -- whether to dim the icons
          name = true, -- whether to dim the name
        },
      })
    end,
  },
}
