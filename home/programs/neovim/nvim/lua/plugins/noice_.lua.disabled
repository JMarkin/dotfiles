return {
    "folke/noice.nvim",
    event = "VeryLazy",
    -- commit = "d9328ef",
    opts = {
        cmdline = {
            enabled = true, -- enables the Noice cmdline UI
            view = "cmdline", -- view for rendering the cmdline. Change to `cmdline` to get a classic cmdline at the bottom
            opts = {}, -- global options for the cmdline. See section on views
            format = {
                -- conceal: (default=true) This will hide the text in the cmdline that matches the pattern.
                -- view: (default is cmdline view)
                -- opts: any options passed to the view
                -- icon_hl_group: optional hl_group for the icon
                -- title: set to anything or empty string to hide
                cmdline = { pattern = "^:", icon = "", lang = "vim" },
                search_down = { kind = "search", pattern = "^/", icon = " ", lang = "regex" },
                search_up = { kind = "search", pattern = "^%?", icon = " ", lang = "regex" },
                filter = { pattern = "^:%s*!", icon = "$", lang = "bash" },
                lua = { pattern = { "^:%s*lua%s+", "^:%s*lua%s*=%s*", "^:%s*=%s*" }, icon = "", lang = "lua" },
                help = { pattern = "^:%s*he?l?p?%s+", icon = "" },
                input = {}, -- Used by input()
                -- lua = false, -- to disable a format, set to `false`
            },
        },
        lsp = {
            -- override markdown rendering so that **cmp** and other plugins use **Treesitter**
            override = {
                ["vim.lsp.util.convert_input_to_markdown_lines"] = true,
                ["vim.lsp.util.stylize_markdown"] = true,
                ["cmp.entry.get_documentation"] = true, -- requires hrsh7th/nvim-cmp
            },
            signature = {
                enabled = true,
                auto_open = {
                    enabled = false,
                    trigger = true, -- Automatically show signature help when typing a trigger character from the LSP
                    luasnip = true, -- Will open signature help when jumping to Luasnip insert nodes
                    throttle = 50, -- Debounce lsp signature help request by 50ms
                },
                view = nil, -- when nil, use defaults from documentation
                ---@type NoiceViewOptions
                opts = {}, -- merged with defaults from documentation
            },
        },
        -- you can enable a preset for easier configuration
        presets = {
            bottom_search = true, -- use a classic bottom cmdline for search
            command_palette = true, -- position the cmdline and popupmenu together
            long_message_to_split = true, -- long messages will be sent to a split
            inc_rename = false, -- enables an input dialog for inc-rename.nvim
            lsp_doc_border = true, -- add a border to hover docs and signature help
        },
        popupmenu = {
            backend = "cmp",
        },
        routes = {
            {
                filter = {
                    event = "msg_show",
                    kind = "lua_error",
                    find = "written",
                },
                opts = { skip = true },
            },
            {
                filter = {
                    event = "msg_show",
                    kind = "",
                    any = {

                        { find = "no lines in buffer" },
                        -- Edit
                        { find = "%d+ less lines" },
                        { find = "%d+ fewer lines" },
                        { find = "%d+ more lines" },
                        { find = "%d+ change;" },
                        { find = "%d+ line less;" },
                        { find = "%d+ more lines?;" },
                        { find = "%d+ fewer lines;?" },
                        { find = '".+" %d+L, %d+B' },
                        { find = "%d+ lines yanked" },
                        { find = "^Hunk %d+ of %d+$" },
                        { find = "%d+L, %d+B$" },
                        { find = "^[/?].*" }, -- Searching up/down
                        { find = "E486: Pattern not found:" }, -- Searcingh not found
                        { find = "%d+ changes?;" }, -- Undoing/redoing
                        { find = "%d+ fewer lines" }, -- Deleting multiple lines
                        { find = "%d+ more lines" }, -- Undoing deletion of multiple lines
                        { find = "%d+ lines " }, -- Performing some other verb on multiple lines
                        { find = "Already at newest change" }, -- Redoing
                        { find = '"[^"]+" %d+L, %d+B' }, -- Saving

                        -- Save
                        { find = " bytes written" },

                        -- Redo/Undo
                        { find = " changes; before #" },
                        { find = " changes; after #" },
                        { find = "1 change; before #" },
                        { find = "1 change; after #" },

                        -- Yank
                        { find = " lines yanked" },

                        -- Move lines
                        { find = " lines moved" },
                        { find = " lines indented" },

                        -- Bulk edit
                        { find = " fewer lines" },
                        { find = " more lines" },
                        { find = "1 more line" },
                        { find = "1 line less" },

                        -- General messages
                        { find = "Already at newest change" }, -- Redoing
                        { find = "Already at oldest change" },
                    },
                },
                opts = { skip = true },
            },
        },
    },
}
