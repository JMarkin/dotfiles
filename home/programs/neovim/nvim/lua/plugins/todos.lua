local is_not_mini = require("funcs").is_not_mini

return {
    "folke/todo-comments.nvim",
    keys = {
        {
            "]t",
            function()
                require("todo-comments").jump_next()
            end,
            desc = "Next todo comment",
        },
        {
            "[t",
            function()
                require("todo-comments").jump_prev()
            end,
            desc = "Previous todo comment",
        },
    },
    dependencies = { "nvim-lua/plenary.nvim", "nvim-treesitter" },
    opts = {},
    cond = is_not_mini,
    event = vim.g.post_load_events,
}
