local vectorcode_cacher = nil
local has_vc = nil

local vectorcacher = function()
  if has_vc ~= nil then
    return has_vc, vectorcode_cacher
  end

  local vectorcode_config
  has_vc, vectorcode_config = pcall(require, "vectorcode.config")
  if has_vc then
    vectorcode_cacher = vectorcode_config.get_cacher_backend()
  end

  return has_vc, vectorcode_cacher
end

local get_prompt = function(get_prompt_message, file_sep)
  get_prompt_message = get_prompt_message or function()
    return ""
  end
  return function(pref, suff)
    local prompt_message = get_prompt_message()

    local h_vc, vc = vectorcacher()
    if h_vc and vc then
      for _, file in ipairs(vc.query_from_cache(0)) do
        prompt_message = file_sep .. file.path .. "\n" .. file.document
      end
    end
    local msg = prompt_message .. "<|fim_prefix|>" .. pref .. "<|fim_suffix|>" .. suff .. "<|fim_middle|>"
    return msg
  end
end

local X5Qwen = {
  api_key = "X5_QWEN_API",
  name = "X5Qwen",
  stream = true,
  end_point = "http://proxy-kafka.k8s.airun-dev-1.salt.x5.ru/v1/completions",
  model = "x5-airun-small-coder-prod",
  template = {
    prompt = function(pref, suff)
      local prompt_message = ""

      local h_vc, vc = vectorcacher()
      if h_vc and vc then
        for _, file in ipairs(vc.query_from_cache(0)) do
          prompt_message = "<|file-sep|>" .. file.path .. "\n" .. file.document
        end
      end
      local msg = prompt_message .. "<[fim-suffix]>" .. suff .. "<[fim-prefix]>" .. pref .. "<[fim-middle]>"
      return msg
    end,
    suffix = false,
  },
  optional = {
    stop = {
      "<|endoftext|>",
      "<|fim-prefix|>",
      "<|fim-middle|>",
      "<|fim-suffix|>",
      "<|fim_pad|>",
      "<|repo_name|>",
      "<|file_sep|>",
      "<|im_start|>",
      "<|im_end|>",
      "/src/",
      "#- coding: utf-8",
      "# Path:",
    },
    max_tokens = 300,
  },
}

local OPENCODER = {
  api_key = "TERM",
  name = "OPENCODER",
  stream = true,
  end_point = vim.g.ollama_completions_endpoint,
  model = "opencoder:8b",
  template = {
    prompt = get_prompt(function()
      return ([[Perform fill-in-middle from the following snippet of a %s code. Respond with only the filled-in code.]]):format(
        vim.bo.filetype
      )
    end, "<|file_sep|>"),
    suffix = false,
  },
  optional = {
    max_tokens = 300,
  },
}

local CODEGEMMA = {
  api_key = "TERM",
  name = "CODEGEMMA",
  stream = true,
  end_point = vim.g.ollama_completions_endpoint,
  model = "codegemma:2b-code",
  template = {
    prompt = get_prompt(nil, "<|file_separator|>"),
    suffix = false,
  },
  optional = {
    max_tokens = 300,
    num_predict = 128,
    temperature = 0,
    top_p = 0.9,
    stop = { "<|file_separator|>" },
  },
}

local attach = function(bufnr)
  local lsps = vim.lsp.get_clients({ name = "minuet", bufnr = bufnr })

  if #lsps and #lsps > 0 then
    vim.notify("Minuet LSP already attached to current buffer", vim.log.levels.INFO)
    return
  end

  require("minuet.lsp").start_server({ buf = bufnr })
end

local detach = function(bufnr)
  local lsps = vim.lsp.get_clients({ name = "minuet", bufnr = bufnr })

  if #lsps == 0 then
    vim.notify("Minuet LSP not attached to current buffer", vim.log.levels.INFO)
    return
  end

  for _, client in ipairs(lsps) do
    vim.lsp.buf_detach_client(bufnr, client.id)
  end

  vim.notify("Minuet LSP detached from current buffer", vim.log.levels.INFO)
end

local enable_auto_trigger = function(bufnr)
  local lsps = vim.lsp.get_clients({ name = "minuet", bufnr = bufnr })

  if #lsps == 0 then
    vim.b[bufnr].minuet_lsp_enable_auto_trigger = true
    attach()
    return
  end

  for _, client in ipairs(lsps) do
    vim.lsp.completion.enable(true, client.id, bufnr, { autotrigger = true })
  end

  vim.notify("Minuet LSP is enabled for auto triggering", vim.log.levels.INFO)
end

local disable_auto_trigger = function(bufnr)
  vim.b[bufnr].minuet_lsp_enable_auto_trigger = nil
  local lsps = vim.lsp.get_clients({ name = "minuet", bufnr = bufnr })

  if #lsps == 0 then
    return
  end

  for _, client in ipairs(lsps) do
    vim.lsp.completion.enable(false, client.id, bufnr)
    vim.notify("Minuet LSP is disabled for auto triggering", vim.log.levels.INFO)
  end
end

return {
  {
    "Davidyz/VectorCode",
    enabled = false,
    -- lazy = true,
    dev = true,
    dir = vim.fn.stdpath("data") .. "/nix/VectorCode",
    dependencies = { "nvim-lua/plenary.nvim" },
    opts = {
      -- async_backend = "lsp",
      n_query = 1,
      async_opts = {
        notify = true,
      },
    },
    init = function()
      vim.api.nvim_create_autocmd("LspAttach", {
        callback = function()
          local cacher = require("vectorcode.config").get_cacher_backend()
          local bufnr = vim.api.nvim_get_current_buf()
          cacher.async_check("config", function()
            cacher.register_buffer(bufnr, {
              n_query = 1,
            })
          end, nil)
        end,
        desc = "Register buffer for VectorCode",
      })
    end,
    config = function(_, opts)
      require("vectorcode").setup(opts)
    end,
  },
  {
    "milanglacier/minuet-ai.nvim",
    cmd = { "Minuet" },
    keys = {
      {
        "<C-_>",
        function()
          local bufnr = vim.api.nvim_get_current_buf()
          attach(bufnr)
          enable_auto_trigger(bufnr)
          vim.api.nvim_create_autocmd({ "InsertLeave", "BufLeave", "BufWinLeave" }, {
            once = true,
            callback = function()
              if vim.b[bufnr].minuet_lsp_enable_auto_trigger then
                disable_auto_trigger(bufnr)
                detach(bufnr)
              end
            end,
          })
        end,
        mode = "i",
      },
    },
    config = function()
      -- This uses the async cache to accelerate the prompt construction.
      -- There's also the require('vectorcode').query API, which provides
      -- more up-to-date information, but at the cost of blocking the main UI.
      require("minuet").setup({
        add_single_line_entry = true,
        n_completions = 1,
        -- I recommend you start with a small context window firstly, and gradually
        -- increase it based on your local computing power.
        context_window = 4096,
        after_cursor_filter_length = 30,
        notify = "debug",
        provider = "openai_fim_compatible",
        provider_options = {
          openai_fim_compatible = X5Qwen,
          -- openai_fim_compatible = CODEGEMMA,
        },
        request_timeout = 10,
        -- virtualtext = {
        --     auto_trigger_ft = {},
        --     keymap = {
        --         -- accept whole completion
        --         accept = '<A-a>',
        --         -- accept one line
        --         accept_line = '<A-a>',
        --         -- accept n lines (prompts for number)
        --         -- e.g. "A-z 2 CR" will accept 2 lines
        --         accept_n_lines = '<A-z>',
        --         -- Cycle to prev completion item, or manually invoke completion
        --         prev = '<A-[>',
        --         -- Cycle to next completion item, or manually invoke completion
        --         next = '<A-]>',
        --         dismiss = '<A-e>',
        --     },
        -- },
        -- lsp = {
        --   enabled_ft = { "lua", "python" },
        -- },
      })
    end,
  },
}
