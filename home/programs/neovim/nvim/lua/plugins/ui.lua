return {
    -- Better `vim.notify()`
    {
        "rcarriga/nvim-notify",
        enabled = false,
        keys = {
            {
                "<leader>un",
                function()
                    require("notify").dismiss({ silent = true, pending = true })
                end,
                desc = "Dismiss all Notifications",
            },
        },
        opts = {
            timeout = 1000,
            stages = "static",
            level = vim.log.levels.INFO,
            top_down = true,
        },
        config = function(args)
            args.opts.background_colour = vim.g.notify_background_color
            require("notify").setup(args.opts)
            vim.notify = require("notify")
        end,
        init = function()
            vim.notify = function(...)
                require("lazy").load({ plugins = { "nvim-notify" } })
                return vim.notify(...)
            end
        end,
    },

    -- better vim.ui
    -- icons
    { "nvim-tree/nvim-web-devicons", lazy = true },

    -- ui components
    { "MunifTanjim/nui.nvim",        lazy = true },

    {
        "ibhagwan/smartyank.nvim",
        -- enabled = false,
        event = "ModeChanged",
        opts = {
            highlight = {
                enabled = true, -- highlight yanked text
                timeout = 100,
            },
        },
        config = function(_, opts)
            require("smartyank").setup(opts)
            vim.api.nvim_create_autocmd("FocusGained", {
                callback = function()
                    local loaded_content = vim.fn.getreg("+")
                    if loaded_content ~= "" then
                        vim.fn.setreg('"', loaded_content)
                    end
                end,
            })
        end,
    },

    {
        "brenoprata10/nvim-highlight-colors",
        -- enabled = false,
        -- event = vim.g.post_load_events,
        -- event = "VeryLazy",
        opts = {
            render = "foreground",
            exclude_filetypes = { "log" },
        },
        cmd = { "HighlightColors" },
        config = function(_, opts)
            require("nvim-highlight-colors").setup(opts)
        end,
    },

    {
        "DanilaMihailov/beacon.nvim",
        -- enabled = false,
        cond = function()
            return not vim.g.neovide
        end,
        opts = {
            enabled = true,                                --- (boolean | fun():boolean) check if enabled
            speed = 2,                                     --- integer speed at wich animation goes
            width = 40,                                    --- integer width of the beacon window
            winblend = 70,                                 --- integer starting transparency of beacon window :h winblend
            fps = 60,                                      --- integer how smooth the animation going to be
            min_jump = 10,                                 --- integer what is considered a jump. Number of lines
            cursor_events = { "CursorMoved" },             -- table<string> what events trigger check for cursor moves
            window_events = { "WinEnter", "FocusGained" }, -- table<string> what events trigger cursor highlight
            highlight = { bg = "white", ctermbg = 15 },    -- vim.api.keyset.highlight table passed to vim.api.nvim_set_hl
        },
        event = { "BufAdd" },
    },
    {
        "tzachar/local-highlight.nvim",
        lazy = true,
        -- enabled = false,
        opts = {
            insert_mode = false,
            file_types = {},
        },
    },
    {
        "prichrd/netrw.nvim",
        -- enabled = false,
        config = function()
            require("netrw").setup({
                -- File icons to use when `use_devicons` is false or if
                -- no icon is found for the given file type.
                icons = {
                    symlink = "",
                    directory = "",
                    file = "",
                },
                -- Uses mini.icon or nvim-web-devicons if true, otherwise use the file icon specified above
                use_devicons = true,
            })
        end,
    },
    {
        "lewis6991/whatthejump.nvim",
        -- enabled = false,
        keys = { "<C-i>", "<C-o>" },
    },
    {
        "MeanderingProgrammer/render-markdown.nvim",
        ft = { "markdown", "codecompanion" }
    },
    -- { "xzbdmw/colorful-menu.nvim", config = true },
}
