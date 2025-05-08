local is_not_mini = require("funcs").is_not_mini
local autocmd = vim.api.nvim_create_autocmd

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
    init = function()
      vim.g.dbext_default_usermaps = 0
    end,
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
    init = function(event)
      vim.g.db_ui_execute_on_save = 0
      vim.g.db_ui_win_position = "right"
      vim.g.db_ui_show_database_icon = 1
      vim.g.db_ui_use_nerd_fonts = 1
      vim.g.db_ui_env_variable_url = "DATABASE_URL"
      vim.g.db_ui_use_nvim_notify = true
      vim.g.db_ui_auto_execute_table_helpers = 1

      autocmd("FileType", {
        pattern = { "dbui" },
        callback = function()
          vim.keymap.set("n", "<tab>", "<Plug>(DBUI_SelectLine)", { buffer = event.buffer, silent = true })
        end,
      })
    end,
    cmd = { "DBUI", "DBUIToggle" },
  },
}
