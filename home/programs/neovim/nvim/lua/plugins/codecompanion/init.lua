local adapters = require("plugins.codecompanion.adapters")

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
            enabled = true,
            -- from nix
            dir = vim.fn.stdpath("data") .. "/nix/mchub.nvim",
            dev = true,
            dependencies = {
                "nvim-lua/plenary.nvim", -- Required for Job and HTTP requests
            },
            cmd = "MCPHub",              -- lazy load by default
            config = function()
                require("mcphub").setup()
            end,
        },
    },
    init = function()
        require("plugins.codecompanion.fidget-spinner"):init()
    end,
    config = function()
        local opts = {
            adapters = adapters,
            strategies = {
                chat = {
                    adapter = "default_adapter",
                    slash_commands = require("plugins.codecompanion.slash_commands"),
                    keymaps = require("plugins.codecompanion.keymaps"),
                    tools = require("plugins.codecompanion.tools"),
                },
                inline = { adapter = "default_adapter" },
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
                    show_settings = true,
                },
            },
            -- opts = {
            --     system_prompt = require("plugins.codecompanion.system_prompt"),
            -- },
            prompt_library = require("plugins.codecompanion.prompts"),
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
