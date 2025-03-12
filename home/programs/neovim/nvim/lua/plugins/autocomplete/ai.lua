return {
    {
        "Davidyz/VectorCode",
        lazy = true,
        version = "0.4.5",
        dependencies = { "nvim-lua/plenary.nvim" },
        opts = {
            n_query = 1,
        },
        config = function(_, opts)
            require("vectorcode").setup(opts)
            local cacher = require("vectorcode.config").get_cacher_backend()
            vim.api.nvim_create_autocmd("LspAttach", {
                callback = function()
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
    },
    {
        "milanglacier/minuet-ai.nvim",
        lazy = true,
        config = function()
            -- This uses the async cache to accelerate the prompt construction.
            -- There's also the require('vectorcode').query API, which provides
            -- more up-to-date information, but at the cost of blocking the main UI.
            local has_vc, vectorcode_config = pcall(require, "vectorcode.config")
            local vectorcode_cacher = nil
            if has_vc then
                vectorcode_cacher = vectorcode_config.get_cacher_backend()
            end
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
                    openai_fim_compatible = {
                        api_key = "X5_QWEN_API",
                        name = "X5Qwen",
                        stream = true,
                        end_point = "http://proxy-kafka.k8s.airun-dev-1.salt.x5.ru/v1/completions",
                        model = "x5-airun-medium-coder-prod",
                        template = {
                            prompt = function(pref, suff)
                                local prompt_message = ""
                                if has_vc then
                                    for _, file in ipairs(vectorcode_cacher.query_from_cache(0)) do
                                        prompt_message = "<|file_sep|>" .. file.path .. "\n" .. file.document
                                    end
                                end
                                return prompt_message
                                    .. "<|fim_prefix|>"
                                    .. pref
                                    .. "<|fim_suffix|>"
                                    .. suff
                                    .. "<|fim_middle|>"
                            end,
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
                    },
                },
            })
        end,
    },
}
