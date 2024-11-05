local is_not_mini = require("funcs").is_not_mini
local autocmd = vim.api.nvim_create_autocmd
local augroup = vim.api.nvim_create_augroup

-- autocmd("FileType", {
--     pattern = "sql",
--     callback = function()
--         vim.bo.omnifunc = "vim_dadbod_completion#omni"
--     end,
-- })

return {
    {
        "tpope/vim-dadbod",
        lazy = true,
        ft = { "sql", "mssql", "plsql" },
    },
    {
        "kristijanhusak/vim-dadbod-completion",
        lazy = true,
        ft = { "sql", "mssql", "plsql" },
    },
    {
        "vim-scripts/dbext.vim",
        lazy = true,
        ft = { "sql", "mssql", "plsql" },
    },
    {
        "kristijanhusak/vim-dadbod-ui",
        enabled = true,
        cond = is_not_mini,
        dependencies = {
            "tpope/vim-dadbod",
            "kristijanhusak/vim-dadbod-completion",
            "vim-scripts/dbext.vim",
        },
        init = function()
            vim.g.db_ui_execute_on_save = 0
            vim.g.db_ui_win_position = "right"
            vim.g.db_ui_show_database_icon = 1
            vim.g.db_ui_use_nerd_fonts = 1
            vim.g.db_ui_env_variable_url = "DATABASE_URL"
            vim.g.db_ui_use_nvim_notify = true
            vim.g.db_ui_auto_execute_table_helpers = 1
        end,
        cmd = { "DBUI" },
    },
}
