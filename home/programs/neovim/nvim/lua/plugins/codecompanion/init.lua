local adapter = "ollama_gemma3"

local function ollama_params(model_name, model)
    return function()
        return require("codecompanion.adapters").extend("ollama", {
            env = {
                url = vim.g.ollama_url,
            },
            headers = {
                ["Content-Type"] = "application/json",
            },
            parameters = {
                sync = true,
                keep_alive = "30m",
            },
            name = model_name,
            schema = {
                model = {
                    default = model,
                },
                num_ctx = {
                    default = 16384,
                },
            },
        })
    end
end

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
            "<leader>ce",
            ":CodeCompanion<cr>",
            desc = "Code Companion",
            silent = true,
            mode = "n",
            noremap = true,
        },
        {
            "<leader>ce",
            ":'<,'>CodeCompanion<cr>",
            desc = "Code Companion",
            silent = true,
            mode = "x",
            noremap = true,
        },
        {
            "<C-CR>",
            ":CodeCompanion<cr>",
            desc = "Code Companion",
            silent = true,
            mode = "n",
            noremap = true,
        },
        {
            "<C-CR>",
            ":'<,'>CodeCompanion<cr>",
            desc = "Code Companion",
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
            dependencies = {
                "nvim-lua/plenary.nvim", -- Required for Job and HTTP requests
            },
            -- comment the following line to ensure hub will be ready at the earliest
            cmd = "MCPHub", -- lazy load by default
            -- uncomment this if you don't want mcp-hub to be available globally or can't use -g
            -- build = "bundled_build.lua",  -- Use this and set use_bundled_binary = true in opts  (see Advanced configuration)
            config = function()
                require("mcphub").setup({
                    extensions = {
                        codecompanion = {
                            -- Show the mcp tool result in the chat buffer
                            show_result_in_chat = true,
                            -- Make chat #variables from MCP server resources
                            make_vars = true,
                        }
                    }
                })
            end,
        },
    },
    init = function()
        require("plugins.codecompanion.fidget-spinner"):init()
    end,
    config = function()
        require("codecompanion").setup({
            adapters = {
                opts = {
                    show_defaults = false,
                },
                gemini = function()
                    return require("codecompanion.adapters").extend("gemini", {
                        env = {
                            api_key = "GEMINI_API",
                        },
                    })
                end,
                x5qwen = function()
                    return require("codecompanion.adapters").extend("openai_compatible", {
                        env = {
                            url = "http://proxy-kafka.k8s.airun-dev-1.salt.x5.ru",
                            api_key = "X5_QWEN_API",           -- optional: if your endpoint is authenticated
                            chat_url = "/v1/chat/completions", -- optional: default value, override if different
                            -- models_endpoint = "/v1/models", -- optional: attaches to the end of the URL to form the endpoint to retrieve models
                        },
                        schema = {
                            model = {
                                default = "x5-airun-medium-coder-prod",
                                choices = function(self)
                                    return {}
                                end,
                            },
                            num_ctx = {
                                default = 32768,
                            },
                        },
                    })
                end,
                ollama_deepseek = ollama_params("deepseek-r1", "hf.co/unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF:Q4_K_M"),
                ollama_qwencoder = ollama_params("qwen2.5", "qwen2.5-coder:14b-instruct-q4_K_M"),
                ollama_gemma3 = ollama_params("gemma3", "hf.co/unsloth/gemma-3-12b-it-GGUF:Q4_K_M"),
                ollama_phimini = ollama_params("phimini", "phi4-mini:latest"),
            },
            strategies = {
                chat = {
                    adapter = adapter,
                    slash_commands = require("plugins.codecompanion.slash_commands"),
                    keymaps = require("plugins.codecompanion.keymaps"),
                    tools = require("plugins.codecompanion.tools"),
                },
                inline = { adapter = adapter },
                agent = { adapter = adapter },
            },
            display = {
                chat = {
                    icons = {
                        pinned_buffer = "📌 ",
                        watched_buffer = "👀 ",
                    },
                    window = {
                        position = "right",
                    },
                    show_header_separator = true,
                    show_settings = true,
                },
            },
            opts = {
                system_prompt = require("plugins.codecompanion.system_prompt"),
            },
            prompt_library = require("plugins.codecompanion.prompts"),
        })

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
