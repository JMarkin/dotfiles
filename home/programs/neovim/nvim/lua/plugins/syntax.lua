return {
    {
        "sheerun/vim-polyglot",
        event = vim.g.pre_load_events,
        init = function()
            vim.cmd([[
                syntax on
            ]])
            vim.g.polyglot_disabled = { "ftdetect" }
        end,
    },
}
