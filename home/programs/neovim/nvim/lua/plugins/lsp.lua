local is_not_mini = require("funcs").is_not_mini

return {
    {
        "neovim/nvim-lspconfig",
        cond = is_not_mini,
        -- event = vim.g.post_load_events,
        event = "VeryLazy",
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

            vim.cmd("LspStart")
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
    {
        "m4ttm/lsp-lens-lite.nvim",
        event = "LspAttach",
        opts = {},
    },
}
