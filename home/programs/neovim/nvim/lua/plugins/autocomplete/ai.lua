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

local get_prompt = function(pref, suff)
    local prompt_message = ""
    local h_vc, vc = vectorcacher()
    if h_vc and vc then
        for _, file in ipairs(vc.query_from_cache(0)) do
            prompt_message = "<|file_sep|>" .. file.path .. "\n" .. file.document
        end
    end
    return prompt_message .. "<|fim_prefix|>" .. pref .. "<|fim_suffix|>" .. suff .. "<|fim_middle|>"
end

local X5Qwen = {
    api_key = "X5_QWEN_API",
    name = "X5Qwen",
    stream = true,
    end_point = "http://proxy-kafka.k8s.airun-dev-1.salt.x5.ru/v1/completions",
    model = "x5-airun-medium-coder-prod",
    template = {
        prompt = get_prompt,
        suffix = false,
    },
    optional = {
        stop = {
            "<|endoftext|>",
            "<|fim_prefix|>",
            "<|fim_middle|>",
            "<|fim_suffix|>",
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
        prompt = get_prompt,
        suffix = false,
    },
    optional = {
        stop = {
            "<|endoftext|>",
            "<|fim_prefix|>",
            "<|fim_middle|>",
            "<|fim_suffix|>",
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

local CODEGEMMA = {
    api_key = "TERM",
    name = "CODEGEMMA",
    stream = true,
    end_point = vim.g.ollama_completions_endpoint,
    model = "codegemma:latest",
    template = {
        prompt = function(pref, suff)
            local prompt_message = ([[Perform fill-in-middle from the following snippet of a %s code. Respond with only the filled-in code.]])
                :format(vim.bo.filetype)

            local h_vc, vc = vectorcacher()
            if h_vc and vc then
                local cache_result = vectorcode_cacher.query_from_cache(0)
                for _, file in ipairs(cache_result) do
                    prompt_message = "<|file_separator|>" .. file.path .. "\n" .. file.document
                end
            end
            return prompt_message .. "<|fim_prefix|>" .. pref .. "<|fim_suffix|>" .. suff .. "<|fim_middle|>"
        end,
        suffix = false,
    },
}

return {
    {
        "Davidyz/VectorCode",
        lazy = true,
        version = "0.5.5",
        enabled = false,
        dependencies = { "nvim-lua/plenary.nvim" },
        opts = {
            async_backend = "lsp",
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
                            n_query = 10,
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
        lazy = true,
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
            })
        end,
    },
}
