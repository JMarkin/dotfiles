local is_not_mini = require("funcs").is_not_mini

return {
    {
        "neovim/nvim-lspconfig",
        cond = is_not_mini,
        event = vim.g.pre_load_events,
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
        "folke/lazydev.nvim",
        opts = {
            library = {
                { path = "luvit-meta/library", words = { "vim%.uv" } },
            },
        },
        lazy = true,
        ft = "lua",
    },
    {
        "j-hui/fidget.nvim",
        event = "LspAttach",
        opts = {
            -- options
        },
    },
}
