local function diff_source()
    local gitsigns = vim.b.gitsigns_status_dict
    if gitsigns then
        return {
            added = gitsigns.added,
            modified = gitsigns.changed,
            removed = gitsigns.removed,
        }
    end
end

return {
    {
        "nanozuki/tabby.nvim",
        event = "TabNew", -- if you want lazy load, see below
        dependencies = "nvim-tree/nvim-web-devicons",
        config = function()
            require("tabby").setup({
                option = {
                    lualine_theme = vim.g.lualine_theme or nil,
                    buf_name = { mode = "unique" },
                },
            })
        end,
    },
    {
        "nvim-lualine/lualine.nvim",
        event = vim.g.post_load_events,
        config = function()
            local lualine = require("lualine")

            lualine.setup({
                extensions = { "quickfix", "nvim-tree", "fzf", "lazy", "symbols-outline", "nvim-dap-ui", "toggleterm" },
                options = {
                    disabled_filetypes = { "Trouble", "Vista", "dashboard" },
                    theme = vim.g.lualine_theme or "auto",
                    component_separators = { left = " ", right = " " },
                    globalstatus = true,
                },
                sections = {
                    lualine_a = { { "mode", icon = "" } },
                    lualine_b = {
                        { "branch", icon = "" },
                    },
                    lualine_c = {
                        { "diff", source = diff_source },
                        -- {
                        --     require("noice").api.status.command.get,
                        --     cond = require("noice").api.status.command.has,
                        -- },

                        -- { "filetype", icon_only = true, separator = "", padding = { left = 1, right = 0 } },
                        -- { "filename", path = 1, symbols = { modified = "  ", readonly = "", unnamed = "" } },
                    },
                    lualine_x = {
                        -- {
                        --     require("noice").api.status.message.get_hl,
                        --     cond = require("noice").api.status.message.has,
                        -- },
                        {
                            require("lazy.status").updates,
                            cond = require("lazy.status").has_updates,
                        },
                        {
                            "diagnostics",
                            symbols = {
                                error = " ",
                                warn = " ",
                                info = " ",
                                hint = "󰝶 ",
                            },
                        },
                    },
                    lualine_y = {
                        "encoding",
                        "filesize",
                        {
                            "fileformat",
                            icons_enabled = true,
                            symbols = {
                                unix = "LF",
                                dos = "CRLF",
                                mac = "CR",
                            },
                        },
                    },
                    lualine_z = { "location", "hostname" },
                },
                -- tabline = {
                --     lualine_a = {
                --         -- {
                --         --     "windows",
                --         --     mode = 2,
                --         --     disabled_buftypes = { "prompt" },
                --         -- },
                --     },
                --     lualine_b = {},
                --     lualine_c = {},
                --     lualine_x = {},
                --     lualine_y = {},
                --     lualine_z = {
                --         {
                --             "tabs",
                --             mode = 2,
                --         },
                --     },
                -- },
            })
        end,
    },
}
