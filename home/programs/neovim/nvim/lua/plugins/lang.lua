local fn = require("funcs")
local is_not_mini = require("funcs").is_not_mini

return {
  {
    "mfussenegger/nvim-lint",
    lazy = true,
    enabled = true,
    config = function()
      require("lint").linters_by_ft = vim.g.linter_by_ft
    end,
    init = function()
      fn.augroup("linting", {
        { "BufWritePost", table.unpack(vim.g.post_load_events) },
        {
          pattern = { "*" },
          callback = function(data)
            if not require("largefiles").is_large_file(data.buf, true) then
              require("lint").try_lint(nil, { ignore_errors = true })
            end
          end,
        },
      })
    end,
  },
  {
    "stevearc/conform.nvim",
    -- event = vim.g.pre_load_events,
    -- event = "VeryLazy",
    cmd = { "ConformInfo" },
    keys = {
      {
        -- Customize or remove this keymap to your liking
        "gqb",
        function()
          local buf = vim.api.nvim_get_current_buf()
          if require("largefiles").is_large_file(buf, true) then
            vim.notify_once("Large buf can't format", vim.log.levels.WARN)
            return
          end
          require("conform").format({ async = true })
        end,
        mode = "",
        desc = "Format buffer",
      },
    },
    -- This will provide type hinting with LuaLS
    ---@module "conform"
    ---@type conform.setupOpts
    opts = {
      formatters_by_ft = vim.g.formatters_by_ft,
      default_format_opts = {
        lsp_format = "fallback",
      },
      -- Customize formatters
      formatters = {
        sqlfluff = {
          prepend_args = { "--dialect", "postgres" },
        },
      },
    },
    init = function()
      vim.o.formatexpr = "v:lua.require'conform'.formatexpr()"
    end,
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
    "mrcjkb/rustaceanvim",
    cond = is_not_mini,
    -- version = "^5", -- Recommended
    lazy = false,
    -- enabled = false,
  },
  {
    name = "clangd_extenstions",
    url = "https://git.sr.ht/~p00f/clangd_extensions.nvim",
    cond = is_not_mini,
    lazy = true,
  },
  { "b0o/schemastore.nvim", cond = is_not_mini, lazy = true },
  {
    "ranelpadon/python-copy-reference.vim",
    cond = is_not_mini,
    ft = { "python" },
    init = function()
      vim.g.python_remove_prefixes = { "src" }
    end,
    keys = {
      {
        "<leader>lcd",
        ":PythonCopyReferenceDotted<CR>",
        desc = "Copy as: Python Dotted",
      },
      {
        "<leader>lcp",
        ":PythonCopyReferencePytest<CR>",
        desc = "Copy as: Pytest",
      },
      {
        "<leader>lci",
        ":PythonCopyReferenceImport<CR>",
        desc = "Copy as: Python Import",
      },
    },
  },
  {
    "cuducos/yaml.nvim",
    ft = { "yaml" }, -- optional
    dependencies = {
      "nvim-treesitter",
    },
  },
  -- uncompiler
  {
    "p00f/godbolt.nvim",
    config = function()
      require("godbolt").setup()
    end,
    cmd = { "Godbolt", "GodboltCompiler" },
  },
  {
    "nvimdev/phoenix.nvim",
    enabled = false,
    init = function()
      ---Default configuration values for Phoenix
      ---@type PhoenixConfig
      vim.g.phoenix = {
        filetypes = { "*" },
      }
    end,
  },
  {
    "JMarkin/gentags.lua",
    -- enabled = false,
    dev = true,
    dir = "~/projects/jmarkin/gentags.lua",
    branch = "feat/neovim-0.10",
    cond = vim.fn.executable("ctags") == 1,
    event = "VeryLazy",
    opts = {
      autostart = true,
      async = true,
      args = {
        "--extras=+r+q",
        "--exclude=\\.*",
        "--exclude=.mypy_cache",
        "--exclude=.ruff_cache",
        "--exclude=.pytest_cache",
        "--exclude=dist",
        "--exclude=target",
        "--exclude=.git",
        "--exclude=node_modules*",
        "--exclude=BUILD",
        "--exclude=vendor*",
        "--exclude=*.min.*",
        "--exclude=__file__",
        "--exclude=.devenv",
      },
    },
    cmd = {
      "GenCTags",
      "GenTagsEnable",
      "GenTagsDisable",
    },
  },

  {
    "Vigemus/iron.nvim",
    cmd = {
      "IronRepl",
      "IronReplHere",
      "IronRestart",
      "IronSend",
      "IronFocus",
      "IronHide",
      "IronWatch",
      "IronAttach",
    },
    keys = {
      "<space>sc",
      "<space>sc",
      "<space>sf",
      "<space>sl",
      "<space>su",
      "<space>sm",
      "<space>mc",
      "<space>mc",
      "<space>md",
      "<space>s<cr>",
      "<space>s<space>",
      "<space>sq",
      "<space>cl",

      { "<space>rs", "<cmd>IronRepl<cr>" },
      { "<space>rr", "<cmd>IronRestart<cr>" },
      { "<space>rf", "<cmd>IronFocus<cr>" },
      { "<space>rh", "<cmd>IronHide<cr>" },
    },
    config = function()
      local iron = require("iron")
      local view = require("iron.view")
      local executable = function(exe)
        return vim.api.nvim_call_function("executable", { exe }) == 1
      end
      local opts = {
        config = {
          -- Whether a repl should be discarded or not
          scratch_repl = true,
          -- Your repl definitions come here
          repl_definition = {
            sh = {
              command = { "bash" },
            },
            python = executable("ipython") and require("iron.fts.python").ipython or require("iron.fts.python").python,
          },
          repl_open_cmd = view.split.vertical.botright(50),
        },
        keymaps = {
          send_motion = "<space>sc",
          visual_send = "<space>sc",
          send_file = "<space>sf",
          send_line = "<space>sl",
          send_until_cursor = "<space>su",
          send_mark = "<space>sm",
          mark_motion = "<space>mc",
          mark_visual = "<space>mc",
          remove_mark = "<space>md",
          cr = "<space>s<cr>",
          interrupt = "<space>si",
          exit = "<space>sq",
          clear = "<space>scl",
        },
        highlight = { italic = true },
        ignore_blank_lines = true, -- ignore blank lines when sending visual select lines
      }
      iron.setup(opts)
    end,
  },
}
