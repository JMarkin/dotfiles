vim.g.rainbow_delimiters_highlight = {
    "RainbowDelimiterRed",
    "RainbowDelimiterYellow",
    "RainbowDelimiterBlue",
    "RainbowDelimiterOrange",
    "RainbowDelimiterGreen",
    "RainbowDelimiterViolet",
    "RainbowDelimiterCyan",
}

vim.api.nvim_create_autocmd("ColorScheme", {
    pattern = "*",
    callback = function()
        vim.api.nvim_set_hl(0, "LocalHighlight", { link = "Debug" })
        vim.api.nvim_set_hl(0, "DiffAdd", { link = "Added" })
        vim.api.nvim_set_hl(0, "DiffDelete", { link = "Removed" })
        vim.api.nvim_set_hl(0, "DiffChange", { link = "Changed" })

        vim.api.nvim_set_hl(0, "CursorLine", { bg = "#202020" })
        vim.api.nvim_set_hl(0, "CursorLineNr", { fg = "#b0b0b0", bg = "#202020" })

        vim.api.nvim_set_hl(0, "ColorColumn", { fg = "#b0b0b0", bg = "#202020" })
    end,
})

if vim.g.modern_ui then
    return {
        {
            "sekke276/dark_flat.nvim",
            enabled = false,
            lazy = false,
            priority = math.huge,
            config = function()
                require("dark_flat").setup({
                    -- transparent = true,
                    italics = true,
                })
                vim.api.nvim_command("colorscheme dark_flat")
                vim.g.lualine_theme = "dark_flat"
            end,
        },
        {
            "ribru17/bamboo.nvim",
            enabled = true,
            lazy = false,
            priority = math.huge,
            config = function()
                require("bamboo").setup({
                    code_style = {
                        comments = { italic = true },
                        conditionals = { italic = true },
                        keywords = { bold = true },
                        functions = { bold = true },
                        namespaces = { italic = true },
                        parameters = { italic = true },
                        strings = {},
                        variables = {},
                    },
                    dim_inactive = true,
                    -- style = "multiplex",
                    transparent = false,
                    lualine = {
                        transparent = true, -- lualine center bar transparency
                    },
                    diagnostics = {
                        darker = true, -- darker colors for diagnostic
                        undercurl = true, -- use undercurl instead of underline for diagnostics
                        background = true, -- use background color for virtual text
                    },
                })
                require("bamboo").load()
            end,
        },
        {
            "Iron-E/nvim-highlite",
            enabled = false,
            lazy = false,
            priority = math.huge,
            config = function(_, opts)
                -- OPTIONAL: setup the plugin. See "Configuration" for information
                require("highlite").setup({
                    generator = {
                        terminal_palette = true,
                        plugins = {
                            nvim = {
                                aerial = false,
                                barbar = false,
                                bqf = true,
                                cmp = true,
                                fzf = false,
                                gitsigns = true,
                                indent_blankline = false,
                                lazy = true,
                                leap = false,
                                lspconfig = true,
                                lspsaga = true,
                                lsp_signature = false,
                                mini = true,
                                neo_tree = false,
                                neotest = true,
                                nvim_tree = false,
                                packer = false,
                                registers = false,
                                symbols_outline = false,
                                telescope = false,
                                todo_comments = true,
                                treesitter_context = true,
                                trouble = true,
                            },
                            vim = {
                                dadbod_ui = true,
                                ale = false,
                                coc = false,
                                easymotion = false,
                                fern = false,
                                gitgutter = false,
                                indent_guides = false,
                                jumpmotion = false,
                                nerdtree = false,
                                sandwich = false,
                                signify = false,
                                swap = false,
                                undotree = false,
                                win = false,
                            },
                        },
                        syntax = true,
                    },
                })

                -- or one of the alternate colorschemes (see the "Built-in Colorschemes" section)
                vim.api.nvim_command("colorscheme highlite")
            end,
            version = "^4.0.0",
        },
        {
            "ramojus/mellifluous.nvim",
            enabled = false,
            lazy = false,
            priority = math.huge,
            config = function(_, opts)
                require("mellifluous").setup({
                    dim_inactive = true,
                    colorset = "tender",
                    styles = { -- see :h attr-list for options. set {} for NONE, { option = true } for option
                        main_keywords = { bold = true },
                        other_keywords = {},
                        types = { italic = true },
                        operators = {},
                        strings = {},
                        functions = { bold = true },
                        constants = {},
                        comments = { italic = true },
                        markup = {
                            headings = { bold = true },
                        },
                        folds = {},
                    },
                    transparent_background = {
                        enabled = false,
                        floating_windows = true,
                        telescope = true,
                        file_tree = true,
                        cursor_line = true,
                        status_line = false,
                    },
                    flat_background = {
                        line_numbers = false,
                        floating_windows = false,
                        file_tree = false,
                        cursor_line_number = false,
                    },
                    plugins = {
                        cmp = true,
                        gitsigns = true,
                        indent_blankline = false,
                        nvim_tree = {
                            enabled = false,
                            show_root = false,
                        },
                        neo_tree = {
                            enabled = false,
                        },
                        telescope = {
                            enabled = false,
                            nvchad_like = true,
                        },
                        startify = false,
                    },
                })
                vim.cmd("colorscheme mellifluous")
            end,
        },
    }
else
    vim.api.nvim_command("colorscheme default")
    return {}
end
