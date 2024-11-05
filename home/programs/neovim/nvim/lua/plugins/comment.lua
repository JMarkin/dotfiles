local is_large_file = require("largefiles").is_large_file
vim.g.skip_ts_context_commentstring_module = true

return {
    {
        "JoosepAlviste/nvim-ts-context-commentstring",
        lazy = true,
        enabled = false,
    },
    {
        "numToStr/Comment.nvim",
        config = function()
            require("Comment").setup({
                -- pre_hook = require("ts_context_commentstring.integrations.comment_nvim").create_pre_hook(),
                ignore = function()
                    return is_large_file(vim.api.nvim_get_current_buf(), true)
                end,
                mappings = {
                    ---Operator-pending mapping; `gcc` `gbc` `gc[count]{motion}` `gb[count]{motion}`
                    basic = false,
                    ---Extra mapping; `gco`, `gcO`, `gcA`
                    extra = false,
                },
            })
        end,
        keys = {

            {
                "gcc",
                function()
                    local vvar = vim.api.nvim_get_vvar
                    return vvar("count") == 0 and "<Plug>(comment_toggle_linewise_current)"
                        or "<Plug>(comment_toggle_linewise_count)"
                end,
                expr = true,
                desc = "Comment toggle current line",
            },
            {
                "gbc",
                function()
                    local vvar = vim.api.nvim_get_vvar
                    return vvar("count") == 0 and "<Plug>(comment_toggle_blockwise_current)"
                        or "<Plug>(comment_toggle_blockwise_count)"
                end,
                expr = true,
                desc = "Comment toggle current block",
            },

            { "gc", "<Plug>(comment_toggle_linewise)", desc = "Comment toggle linewise" },
            { "gb", "<Plug>(comment_toggle_blockwise)", desc = "Comment toggle linewise" },

            {
                "gc",
                "<Plug>(comment_toggle_linewise_visual)",
                mode = { "x" },
                desc = "Comment toggle linewise (visual)",
            },
            {
                "gb",
                "<Plug>(comment_toggle_blockwise_visual)",
                mode = { "x" },
                desc = "Comment toggle blockwise (visual)",
            },
        },
    },
}
