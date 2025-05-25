return {
  "yetone/avante.nvim",
  event = "VeryLazy",
  -- from nix
  dev = true,
  dir = vim.fn.stdpath("data") .. "/nix/avante.nvim",
  pin = true,
  opts = {
    debug = false,
    ---@alias Provider "claude" | "openai" | "azure" | "gemini" | "cohere" | "copilot" | string
    provider = "x5qwen", -- The provider used in Aider mode or in the planning phase of Cursor Planning Mode
    ollama = {
      endpoint = vim.g.ollama_url,
      model = "hf.co/unsloth/Qwen2.5-Coder-3B-Instruct-128K-GGUF:Q4_K_M",
    },
    vendors = {
      ["x5qwen"] = {
        __inherited_from = "openai",
        endpoint = "http://proxy-kafka.k8s.airun-dev-1.salt.x5.ru/v1",
        api_key_name = "X5_QWEN_API",
        model = "x5-airun-medium-coder-prod",
      },
    },
    ---@alias Mode "agentic" | "legacy"
    mode = "agentic", -- The default mode for interaction. "agentic" uses tools to automatically generate code, "legacy" uses the old planning method to generate code.
    -- WARNING: Since auto-suggestions are a high-frequency operation and therefore expensive,
    -- currently designating it as `copilot` provider is dangerous because: https://github.com/yetone/avante.nvim/issues/1048
    -- Of course, you can reduce the request frequency by increasing `suggestion.debounce`.
    auto_suggestions_provider = "ollama",
    cursor_applying_provider = nil, -- The provider used in the applying phase of Cursor Planning Mode, defaults to nil, when nil uses Config.provider as the provider for the applying phase
    rag_service = {
      enabled = true,
      provider = "ollama",
      runner = "nix",
    },
    dual_boost = {
      enabled = false,
      first_provider = "x5qwen",
      second_provider = "ollama",
      timeout = 60000, -- Timeout in milliseconds
    },
    behaviour = {
      auto_focus_sidebar = false,
      auto_suggestions = true, -- Experimental stage
      auto_suggestions_respect_ignore = false,
      auto_set_highlight_group = true,
      auto_set_keymaps = true,
      auto_apply_diff_after_generation = false,
      jump_result_buffer_on_finish = false,
      support_paste_from_clipboard = false,
      minimize_diff = true,
      enable_token_counting = true,
      use_cwd_as_project_root = true,
      auto_focus_on_diff_view = true,
    },
    hints = { enabled = true },
  },
  dependencies = {
    "nvim-treesitter/nvim-treesitter",
    "stevearc/dressing.nvim",
    "nvim-lua/plenary.nvim",
    "MunifTanjim/nui.nvim",
    "ibhagwan/fzf-lua", -- for file_selector provider fzf
  },
}
