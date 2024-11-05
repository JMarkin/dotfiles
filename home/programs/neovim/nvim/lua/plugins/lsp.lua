local is_not_mini = require("funcs").is_not_mini

return {
    {
        "neovim/nvim-lspconfig",
        cond = is_not_mini,
        event = vim.g.post_load_events,
        -- event = "VeryLazy",
        config = function()
            require("lsp").setup()

            vim.diagnostic.config({
                underline = true,
                signs = true,
                virtual_text = false,
                -- virtual_lines = { only_current_line = true },
                float = true,
                update_in_insert = false,
                severity_sort = true,
            })
        end,
    },
    {
        "glepnir/lspsaga.nvim",
        dependencies = { "nvim-tree/nvim-web-devicons" },
        lazy = true,
        event = "LspAttach",
        keys = {
            {
                "[d",
                "<cmd>Lspsaga diagnostic_jump_prev<CR>",
                desc = "Jump: prev diag",
            },
            {
                "]d",
                "<cmd>Lspsaga diagnostic_jump_next<CR>",
                desc = "Jump: next diag",
            },
            {
                "[e",
                function()
                    require("lspsaga.diagnostic"):goto_prev({ severity = vim.diagnostic.severity.ERROR })
                end,
                desc = "Jump: prev Error",
            },
            {
                "]e",
                function()
                    require("lspsaga.diagnostic"):goto_next({ severity = vim.diagnostic.severity.ERROR })
                end,
                desc = "Jump: next Error",
            },
        },
        config = function()
            local opts = {
                finder = {
                    keys = {
                        toggle_or_open = { "o", "<CR>" },
                        vsplit = "<C-v>",
                        split = "<C-s>",
                        quit = { "q", "<ESC>" },
                    },
                },
                definition = {
                    keys = {
                        edit = "<C-c>o",
                        vsplit = "<C-v>",
                        split = "<C-s>",
                        quit = "q",
                        close = "<Esc>",
                    },
                },
                rename = {
                    keys = {
                        quit = "<C-c>",
                    },
                },
                callhierarchy = {
                    show_detail = true,
                    keys = {
                        vsplit = "<C-v>",
                        split = "<C-s>",
                    },
                },
                symbol_in_winbar = {
                    enable = false,
                },
                lightbulb = {
                    enable = false,
                },
                diagnostic = {
                    keys = {
                        exec_action = "o",
                        quit = "q",
                        go_action = "g",
                        expand_or_jump = "<CR>",
                    },
                },
            }
            if vim.g.lspsaga_colors then
                opts.ui = { colors = vim.g.lspsaga_colors }
            end

            require("lspsaga").setup(opts)
        end,
    },
    { "folke/neodev.nvim", lazy = true, opts = {
        lspconfig = false,
    } },
    {
        "j-hui/fidget.nvim",
        event = "LspAttach",
        opts = {
            -- options
        },
    },
}
