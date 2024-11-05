local is_not_mini = require("funcs").is_not_mini

return {
    "danymat/neogen",
    cond = is_not_mini,
    dependencies = "nvim-treesitter/nvim-treesitter",
    config = function()
        require("neogen").setup({
            enabled = true,
            input_after_comment = true,
            snippet_engine = "luasnip",
        })
    end,
    cmd = "Neogen",
    keys = {
        {
            "<leader>lD",
            "<cmd>Neogen<cr>",
            desc = "Lang: generate docs",
        },
    },
}
