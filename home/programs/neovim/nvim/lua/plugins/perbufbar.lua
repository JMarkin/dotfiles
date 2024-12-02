return {
    {
        "ramilito/winbar.nvim",
        -- event = "VeryLazy",
        dependencies = { "nvim-tree/nvim-web-devicons" },
        config = function()
            require("winbar").setup({
                -- your configuration comes here, for example:
                icons = true,
                filetype_exclude = {
                    "vista",
                    "dbui",
                    "help",
                    "startify",
                    "dashboard",
                    "packer",
                    "neo-tree",
                    "neogitstatus",
                    "NvimTree",
                    "Trouble",
                    "alpha",
                    "lir",
                    "Outline",
                    "spectre_panel",
                    "toggleterm",
                    "TelescopePrompt",
                    "prompt",
                    "httpResult",
                    "http",
                    "rest_nvim_result",
                    "netrw",
                },
                diagnostics = true,
                buf_modified = true,
                dir_levels = 2,
                -- buf_modified_symbol = "M",
                -- or use an icon
                buf_modified_symbol = "●",
                dim_inactive = {
                    enabled = true,
                    highlight = "WinbarNC",
                    icons = true, -- whether to dim the icons
                    name = true, -- whether to dim the name
                },
            })
        end,
    },
}
