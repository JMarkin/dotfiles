return {
    {
        "olimorris/codecompanion.nvim",
        dependencies = {
            "nvim-lua/plenary.nvim",
            "nvim-treesitter/nvim-treesitter",
            "stevearc/dressing.nvim", -- Optional: Improves `vim.ui.select`
        },
        cmd = {
            "CodeCompanion",
            "CodeCompanionChat",
            "CodeCompanionActions",
        },
        opts = {
            opts = {
                log_level = "ERROR",
            },
            strategies = {
                chat = {
                    adapter = "ollama",
                    keymaps = {
                        options = {
                            modes = {
                                n = "?",
                            },
                            callback = "keymaps.options",
                            description = "Options",
                            hide = true,
                        },
                        completion = {
                            modes = {
                                i = "<C-_>",
                            },
                            index = 1,
                            callback = "keymaps.completion",
                            description = "Completion Menu",
                        },
                        send = {
                            modes = {
                                n = { "<CR>", "<C-s>" },
                                i = "<C-s>",
                            },
                            index = 1,
                            callback = "keymaps.send",
                            description = "Send",
                        },
                        regenerate = {
                            modes = {
                                n = "gr",
                            },
                            index = 2,
                            callback = "keymaps.regenerate",
                            description = "Regenerate the last response",
                        },
                        close = {
                            modes = {
                                n = "<C-c>",
                                i = "<C-c>",
                            },
                            index = 3,
                            callback = "keymaps.stop",
                            description = "Stop Chat",
                        },
                        stop = {
                            modes = {
                                n = "q",
                            },
                            index = 4,
                            callback = "keymaps.stop",
                            description = "Stop Request",
                        },
                        clear = {
                            modes = {
                                n = "gx",
                            },
                            index = 5,
                            callback = "keymaps.clear",
                            description = "Clear Chat",
                        },
                        codeblock = {
                            modes = {
                                n = "gc",
                            },
                            index = 6,
                            callback = "keymaps.codeblock",
                            description = "Insert Codeblock",
                        },
                        yank_code = {
                            modes = {
                                n = "gy",
                            },
                            index = 7,
                            callback = "keymaps.yank_code",
                            description = "Yank Code",
                        },
                        next_chat = {
                            modes = {
                                n = "}",
                            },
                            index = 8,
                            callback = "keymaps.next_chat",
                            description = "Next Chat",
                        },
                        previous_chat = {
                            modes = {
                                n = "{",
                            },
                            index = 9,
                            callback = "keymaps.previous_chat",
                            description = "Previous Chat",
                        },
                        next_header = {
                            modes = {
                                n = "]]",
                            },
                            index = 10,
                            callback = "keymaps.next_header",
                            description = "Next Header",
                        },
                        previous_header = {
                            modes = {
                                n = "[[",
                            },
                            index = 11,
                            callback = "keymaps.previous_header",
                            description = "Previous Header",
                        },
                        change_adapter = {
                            modes = {
                                n = "ga",
                            },
                            index = 12,
                            callback = "keymaps.change_adapter",
                            description = "Change adapter",
                        },
                        fold_code = {
                            modes = {
                                n = "gf",
                            },
                            index = 13,
                            callback = "keymaps.fold_code",
                            description = "Fold code",
                        },
                        debug = {
                            modes = {
                                n = "gd",
                            },
                            index = 14,
                            callback = "keymaps.debug",
                            description = "View debug info",
                        },
                        system_prompt = {
                            modes = {
                                n = "gs",
                            },
                            index = 15,
                            callback = "keymaps.toggle_system_prompt",
                            description = "Toggle the system prompt",
                        },
                    },
                },
                inline = { adapter = "ollama" },
                agent = { adapter = "ollama" },
            },
            adapters = {
                ollama = function()
                    return require("codecompanion.adapters").extend("ollama", {
                        env = {
                            url = vim.g.ollama_url,
                        },
                        headers = {
                            ["Content-Type"] = "application/json",
                        },
                        parameters = {
                            sync = true,
                        },
                        name = "qwen2.5", -- Give this adapter a different name to differentiate it from the default ollama adapter
                        schema = {
                            model = {
                                default = "qwen2.5-coder:latest",
                            },
                            num_ctx = {
                                default = 16384,
                            },
                            num_predict = {
                                default = -1,
                            },
                        },
                    })
                end,
            },
            prompt_library = {
                ["Code Expert"] = {
                    strategy = "chat",
                    description = "Get some special advice from an LLM",
                    opts = {
                        modes = { "v" },
                        short_name = "expert",
                        auto_submit = true,
                        stop_context_insertion = true,
                        user_prompt = true,
                    },
                    prompts = {
                        {
                            role = "system",
                            content = function(context)
                                return "I want you to act as a senior "
                                    .. context.filetype
                                    .. " developer. I will ask you specific questions and I want you to return concise explanations and codeblock examples."
                            end,
                        },
                        {
                            role = "user",
                            content = function(context)
                                local text = require("codecompanion.helpers.actions").get_code(
                                    context.start_line,
                                    context.end_line
                                )

                                return "I have the following code:\n\n```"
                                    .. context.filetype
                                    .. "\n"
                                    .. text
                                    .. "\n```\n\n"
                            end,
                            opts = {
                                contains_code = true,
                            },
                        },
                    },
                },
            },
        },
    },
}
