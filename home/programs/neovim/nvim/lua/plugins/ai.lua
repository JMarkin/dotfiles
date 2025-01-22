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
        keys = {
            { "<leader>cc", ":CodeCompanionChat<cr>", desc = "CodeCompanionChat", mode = { "n", "v" } },
            { "<leader>ca", ":CodeCompanionAction<cr>", desc = "CodeCompanionActions", mode = { "n", "v" } },
        },
        opts = {
            display = {
                chat = {
                    window = {
                        -- layout = "vertical", -- float|vertical|horizontal|buffer
                        opts = {
                            spell = true,
                        },
                    },
                    show_header_separator = true,
                    show_settings = true,
                },
            },
            opts = {
                log_level = "ERROR",
                ---@param opts table
                ---@return string
                system_prompt = function(opts)
                    local language = opts.language or "English"
                    return string.format(
                        [[You are an AI programming assistant named "CodeCompanion".
You are currently plugged in to the Neovim text editor on a user's machine.

Your core tasks include:
- Answering general programming questions.
- Explaining how the code in a Neovim buffer works.
- Reviewing the selected code in a Neovim buffer.
- Generating unit tests for the selected code.
- Proposing fixes for problems in the selected code.
- Scaffolding code for a new workspace.
- Finding relevant code to the user's query.
- Proposing fixes for test failures.
- Answering questions about Neovim.
- Running tools.

You must:
- Follow the user's requirements carefully and to the letter.
- Keep your answers short and impersonal, especially if the user responds with context outside of your tasks.
- Minimize other prose.
- Use Markdown formatting in your answers.
- Include the programming language name at the start of the Markdown code blocks.
- Avoid including line numbers in code blocks.
- Avoid wrapping the whole response in triple backticks.
- Only return code that's relevant to the task at hand. You may not need to return all of the code that the user has shared.
- Use actual line breaks instead of '\n' in your response to begin new lines.
- Use '\n' only when you want a literal backslash followed by a character 'n'.
- All non-code responses must be in %s.

When given a task:
1. Answer short as possible without explain, unless asked explain.
2. Output the code in a single code block, being careful to only return relevant code.
3. You should always generate short suggestions for the next user turns that are relevant to the conversation without testing and review.
4. You can only give one reply for each conversation turn.]],
                        language
                    )
                end,
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
                                n = "za",
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
                cmd = { adapter = "ollama" },
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
                        name = "deepseek-r1",
                        schema = {
                            model = {
                                default = "deepseek-r1:14b",
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
        config = function(_, opts)
            require("codecompanion").setup(opts)

            local group = vim.api.nvim_create_augroup("CodeCompanionHooks", {})

            local progress = {}

            local companion_progress = function(request)
                if request.match == "CodeCompanionRequestStarted" then
                    progress.in_progress = true

                    progress.handle = require("fidget.progress").handle.create({
                        title = "CodeCompanionChat",
                        message = "Start completion",
                        lsp_client = { name = "codecompanion" },
                    })
                    progress.poller = require("fidget.poll").Poller({
                        name = "codecompanion",
                        poll = function()
                            return not progress.in_progress
                        end,
                    })
                    progress.poller:start_polling(1)
                elseif request.match == "CodeCompanionRequestFinished" then
                    progress.in_progress = false
                    progress.handle:finish()
                end
            end

            vim.api.nvim_create_autocmd({ "User" }, {
                pattern = "CodeCompanionRequest*",
                group = group,
                callback = companion_progress,
            })
        end,
    },
}
