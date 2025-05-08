return {
  "yetone/avante.nvim",
  event = "VeryLazy",
  dev = true,
  -- from nix
  dir = vim.fn.stdpath("data") .. "/nix/avante.nvim",
  opts = {
    ---@alias Provider "claude" | "openai" | "azure" | "gemini" | "cohere" | "copilot" | string
    provider = "ollama", -- The provider used in Aider mode or in the planning phase of Cursor Planning Mode
    ollama = {
      endpoint = vim.g.ollama_url,
      model = "hf.co/unsloth/Qwen2.5-Coder-7B-Instruct-128K-GGUF:Q4_K_M",
    },
    vendors = {
      ollama = {
        __inherited_from = "openai",
        api_key_name = "",
        endpoint = vim.g.ollama_url,
        model = "hf.co/unsloth/Qwen2.5-Coder-7B-Instruct-128K-GGUF:Q4_K_M",
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
      enabled = false,
      provider = "ollama",
      llm_model = "hf.co/unsloth/Qwen2.5-Coder-7B-Instruct-128K-GGUF:Q4_K_M",
    },
    behaviour = {
      auto_suggestions = false, -- Experimental stage
      auto_set_highlight_group = true,
      auto_set_keymaps = true,
      auto_apply_diff_after_generation = false,
      support_paste_from_clipboard = false,
      minimize_diff = true, -- Whether to remove unchanged lines when applying a code block
      enable_token_counting = true, -- Whether to enable token counting. Default to true.
    },
    mappings = {
      --- @class AvanteConflictMappings
      diff = {
        ours = "co",
        theirs = "ct",
        all_theirs = "ca",
        both = "cb",
        cursor = "cc",
        next = "]x",
        prev = "[x",
      },
      suggestion = {
        accept = "<M-l>",
        next = "<M-]>",
        prev = "<M-[>",
        dismiss = "<C-]>",
      },
      jump = {
        next = "]]",
        prev = "[[",
      },
      submit = {
        normal = "<CR>",
        insert = "<C-s>",
      },
      cancel = {
        normal = { "<C-c>", "<Esc>", "q" },
        insert = { "<C-c>" },
      },
      sidebar = {
        apply_all = "A",
        apply_cursor = "a",
        retry_user_request = "r",
        edit_user_request = "e",
        switch_windows = "<Tab>",
        reverse_switch_windows = "<S-Tab>",
        remove_file = "d",
        add_file = "@",
        close = { "<Esc>", "q" },
        close_from_input = nil, -- e.g., { normal = "<Esc>", insert = "<C-d>" }
      },
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
