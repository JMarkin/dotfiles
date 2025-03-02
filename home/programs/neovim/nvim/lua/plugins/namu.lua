return {
    {
        "bassamsdata/namu.nvim",
        -- dev = true,
        keys = { { "<space>T", ":Namu ctags<cr>", desc = "Tagbar" } },
        cmd = { "Namu" },
        config = function()
            require("namu").setup({
                -- Enable the modules you want
                namu_symbols = {
                    enable = true,
                    options = {
                        row_position = "bottom10_right",
                    },
                },
                namu_ctags = {
                    enable = true,
                    options = {
                        row_position = "bottom10_right",
                    },
                },
                -- Optional: Enable other modules if needed
                colorscheme = {
                    enable = false,
                },
                ui_select = { enable = false }, -- vim.ui.select() wrapper
            })
        end,
    },
}
