local adapters = require("plugins.ai.codecompanion.adapters")

return {
  "olimorris/codecompanion.nvim",
  cmd = {
    "CodeCompanionChat",
    "CodeCompanion",
    "CodeCompanionCmd",
    "CodeCompanionActions",
  },
  keys = {
    {
      "<leader>cc",
      function()
        require("codecompanion").toggle()
      end,
      desc = "Code Companion",
      silent = true,
    },
    {
      "<leader>cc",
      ":'<,'>CodeCompanionChat Add<cr>",
      desc = "Code Companion Add",
      silent = true,
      mode = "x",
      noremap = true,
    },
    {
      "<C-?>",
      function()
        require("codecompanion").toggle()
      end,
      desc = "Code Companion",
      silent = true,
    },
    {
      "<C-?>",
      ":'<,'>CodeCompanionChat Add<cr>",
      desc = "Code Companion Add",
      silent = true,
      mode = "x",
      noremap = true,
    },
    {
      "<leader>ci",
      ":CodeCompanion<cr>",
      desc = "Code Companion inline",
      silent = true,
      mode = "n",
      noremap = true,
    },
    {
      "<leader>ci",
      ":'<,'>CodeCompanion<cr>",
      desc = "Code Companion inline",
      silent = true,
      mode = "x",
      noremap = true,
    },
    {
      "<leader>ca",
      ":'<,'>CodeCompanionActions<cr>",
      desc = "Code Companion Actions",
      silent = true,
      mode = "x",
      noremap = true,
    },
    {
      "<leader>ca",
      ":CodeCompanionActions<cr>",
      desc = "Code Companion Actions",
      silent = true,
      mode = "n",
      noremap = true,
    },
  },
  dependencies = {
    "nvim-lua/plenary.nvim",
    "nvim-treesitter/nvim-treesitter",
    "j-hui/fidget.nvim",
    {
      "ravitemer/mcphub.nvim",
      enabled = true,
      -- from nix
      dir = vim.fn.stdpath("data") .. "/nix/mchub.nvim",
      dev = true,
      dependencies = {
        "nvim-lua/plenary.nvim", -- Required for Job and HTTP requests
      },
      cmd = "MCPHub", -- lazy load by default
      config = function()
        require("mcphub").setup()
      end,
    },
  },
  init = function()
    require("plugins.ai.codecompanion.fidget-spinner"):init()
  end,
  config = function()
    local opts = {
      adapters = adapters,
      strategies = {
        chat = {
          adapter = "default_adapter",
          slash_commands = require("plugins.ai.codecompanion.slash_commands"),
          keymaps = require("plugins.ai.codecompanion.keymaps"),
          tools = require("plugins.ai.codecompanion.tools"),
        },
        inline = {
          adapter = "default_adapter",
          keymaps = {
            accept_change = {
              modes = { n = "gh" },
              description = "Accept the suggested change",
            },
            reject_change = {
              modes = { n = "gH" },
              description = "Reject the suggested change",
            },
          },
        },
        agent = { adapter = "default_adapter" },
      },
      display = {
        chat = {
          -- window = {
          --     layout = "float",
          -- },
          icons = {
            pinned_buffer = "📌 ",
            watched_buffer = "👀 ",
          },
          show_header_separator = true,
          show_settings = false,
        },
      },
      -- opts = {
      --     system_prompt = require("plugins.ai.codecompanion.system_prompt"),
      -- },
      prompt_library = require("plugins.ai.codecompanion.prompts"),
    }

    local ok, _ = pcall(require, "mchup")
    if ok then
      opts.extensions = {
        mcphub = {
          callback = "mcphub.extensions.codecompanion",
          opts = {
            make_vars = true,
            make_slash_commands = true,
            show_result_in_chat = true,
          },
        },
      }
    end

    require("codecompanion").setup(opts)

    local group = vim.api.nvim_create_augroup("CodeCompanionHooks", {})

    vim.api.nvim_create_autocmd({ "User" }, {
      pattern = "CodeCompanionChatOpened",
      group = group,
      callback = function()
        vim.wo.number = false
        vim.wo.relativenumber = false
      end,
    })
  end,
}
