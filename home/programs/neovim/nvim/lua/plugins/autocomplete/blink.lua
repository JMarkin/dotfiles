local funcs = require("funcs")
local lf = require("largefiles")

local blink = {
  "saghen/blink.cmp",
  lazy = true,
  -- from nix
  dev = true,
  dir = vim.fn.stdpath("data") .. "/nix/blink.cmp",
  pin = true,
  event = { "InsertEnter", "CmdlineEnter" },
  -- optional: provides snippets for the snippet source
  dependencies = {
    "rafamadriz/friendly-snippets",
    "danymat/neogen",
    "xzbdmw/colorful-menu.nvim",

    -- {
    --   dev = true,
    --   dir = vim.fn.stdpath("data") .. "/nix/blink-cmp-avante",
    --   pin = true,
    --   "Kaiser-Yang/blink-cmp-avante",
    -- },

    -- cmp compact
    {
      dev = true,
      dir = vim.fn.stdpath("data") .. "/nix/blink.compat",
      pin = true,
      "saghen/blink.compat",
      opts = { impersonate_nvim_cmp = true },
    },
    "JMarkin/cmp-diag-codes",
    "quangnguyen30192/cmp-nvim-tags",
  },
  opts = {
    cmdline = {
      enabled = true,
      completion = { menu = { auto_show = false } },
      keymap = {
        ["<CR>"] = { "accept_and_enter", "fallback" },
      },
    },
    keymap = {
      preset = "default",
      ["<C-a>"] = { "hide" },
      ["<C-k>"] = { "show_documentation", "hide_documentation" },
      ["<c-b>"] = {},
      -- ["<CR>"] = { "accept", "fallback" },
      ["<C-e>"] = { "scroll_documentation_up", "fallback" },
      ["<C-d>"] = { "scroll_documentation_down", "fallback" },
      ["<C-p>"] = { "select_prev" },
      ["<C-n>"] = { "select_next" },
      ["<S-Tab>"] = {
        function(cmp)
          local neogen = require("neogen")
          if neogen.jumpable(true) then
            vim.schedule(neogen.jump_prev)
            return true
          end
        end,
        "snippet_backward",
        "fallback",
      },
      ["<Tab>"] = {
        function(cmp)
          local neogen = require("neogen")
          if neogen.jumpable() then
            vim.schedule(neogen.jump_next)
            return true
          end
        end,
        "snippet_forward",
        "fallback",
      },
      ["<c-x><c-f>"] = {
        function()
          require("blink-cmp").show({ providers = { "path" } })
        end,
      },
      ["<c-x><c-]>"] = {
        function()
          require("blink-cmp").show({ providers = { "tags" } })
        end,
      },
      ["<c-x><c-o>"] = {
        function()
          require("blink-cmp").show({ providers = { "lsp" } })
        end,
      },
    },
    completion = {
      keyword = { range = "full" },
      accept = {
        auto_brackets = {
          enabled = false,
        },
      },
      ghost_text = {
        enabled = true,
      },
      trigger = {
        prefetch_on_insert = true,
        show_in_snippet = true,
        show_on_keyword = true,
        show_on_trigger_character = true,
        show_on_insert_on_trigger_character = true,
        show_on_accept_on_trigger_character = true,
      },
      list = {
        selection = {
          preselect = false,
          auto_insert = true,
        },
      },
    },

    sources = {
      default = function(ctx)
        if vim.bo.filetype == "sql" then
          return { "dadbod" }
        elseif lf.is_large_file(vim.api.nvim_get_current_buf(), true) then
          return { "tags", "omni" }
        elseif vim.bo.filetype == "codecompanion" then
          return { "codecompanion", "tags", "lsp" }
        elseif vim.bo.filetype == "AvanteInput" then
          return { "avante", "tags", "lsp" }
        elseif funcs.in_treesitter_capture("comment") or funcs.in_syntax_group("Comment") then
          return { "diag-codes", "snippets", "lsp" }
        end
        return { "lazydev", "lsp", "tags", "snippets" }
      end,
      providers = {
        lazydev = {
          name = "LazyDev",
          module = "lazydev.integrations.blink",
          -- make lazydev completions top priority (see `:h blink.cmp`)
          score_offset = 100,
        },
        -- avante = {
        --   module = "blink-cmp-avante",
        --   name = "Avante",
        --   opts = {
        --     -- options for blink-cmp-avante
        --   },
        -- },
        dadbod = { name = "Dadbod", module = "vim_dadbod_completion.blink" },
        tags = {
          name = "tags",
          module = "blink.compat.source",
          score_offset = -2,
          opts = {
            exact_match = true,
            current_buffer_only = false,
          },
        },
        ["diag-codes"] = {
          name = "diag-codes",
          module = "blink.compat.source",
          score_offset = 100,
          opts = {
            in_comment = false,
          },
        },
      },
    },
    fuzzy = {
      prebuilt_binaries = {
        download = false,
      },
    },
  },
  config = function(_, opts)
    opts.completion.menu = {
      draw = {
        -- We don't need label_description now because label and label_description are already
        -- conbined together in label by colorful-menu.nvim.
        columns = { { "kind_icon" }, { "label", gap = 1 } },
        components = {
          label = {
            text = function(ctx)
              return require("colorful-menu").blink_components_text(ctx)
            end,
            highlight = function(ctx)
              return require("colorful-menu").blink_components_highlight(ctx)
            end,
          },
        },
      },
    }
    require("blink.cmp").setup(opts)
  end,
}

return blink
