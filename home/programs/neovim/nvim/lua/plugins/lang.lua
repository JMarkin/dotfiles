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
    init = function()
      ---Default configuration values for Phoenix
      ---@type PhoenixConfig
      vim.g.phoenix = {
        -- Enable for all filetypes by default
        filetypes = { "*" },

        -- Dictionary settings control word storage
        dict = {
          capacity = 50000, -- Store up to 50k words
          min_word_length = 2, -- Ignore single-letter words
          word_pattern = "[^%s%.%_:%p%d]+", -- Word pattern
        },

        -- Completion control the scoring
        completion = {
          max_items = 100, -- Max result items
          decay_minutes = 30, -- Time period for decay calculation
          weights = {
            recency = 0.3, -- 30% weight to recent usage
            frequency = 0.7, -- 70% weight to frequency
          },
          priority = {
            base = 20, -- Base priority score (0-999)
            position = "after", -- Position relative to other LSP results: 'before' or 'after'
          },
        },

        -- Cleanup settings control dictionary maintenance
        cleanup = {
          cleanup_batch_size = 1000, -- Process 1000 words per batch
          frequency_threshold = 0.1, -- Keep words used >10% of max frequency
          collection_batch_size = 100, -- Collect 100 words before yielding
          rebuild_batch_size = 100, -- Rebuild 100 words before yielding
          idle_timeout_ms = 1000, -- Wait 1s before cleanup
          cleanup_ratio = 0.9, -- Cleanup at 90% capacity
          enable_notify = false, -- Enable notify when cleanup dictionary
        },

        -- Scanner settings control filesystem interaction
        scanner = {
          scan_batch_size = 1000, -- Scan 1000 items per batch
          cache_duration_ms = 5000, -- Cache results for 5s
          throttle_delay_ms = 200, -- Wait 200ms between updates
          ignore_patterns = {}, -- Dictionary or file ignored when path completion
        },
        -- path of snippet json file like c.json/zig.json/go.json
        snippet = vim.fn.stdpath("config") .. "/snippets",
      }
    end,
  },
  {
    "JMarkin/gentags.lua",
    -- enabled = false,
    dev = true,
    cond = vim.fn.executable("ctags") == 1,
    opts = {
      autostart = false,
      async = false,
      args = {
        "--extras=+r+q",
        "--exclude=\\.*",
        "--exclude=.mypy_cache",
        "--exclude=.ruff_cache",
        "--exclude=.pytest_cache",
        "--exclude=dist",
        "--exclude=.git",
        "--exclude=node_modules*",
        "--exclude=BUILD",
        "--exclude=vendor*",
        "--exclude=*.min.*",
        "--exclude=__file__",
      },
    },
    cmd = {
      "GenCTags",
      "GenTagsEnable",
      "GenTagsDisable",
    },
  },
}
