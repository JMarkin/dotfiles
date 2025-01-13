return {
    {
        "jinh0/eyeliner.nvim",
        keys = { "t", "f", "T", "F" },
        opts = {
            highlight_on_key = true,
            dim = true,
            default_keymaps = false,
        },
    },
    {
        "mawkler/demicolon.nvim",
        -- stylua: ignore start
        keys = {
            -- plugin
            ";", ",",
            --  t/T/f/F key mappings
            "t", "f", "T", "F",
            --  lezy load key mappings
            "]", "[",
            -- key mappings to jump to diganostics. See demicolon.keymaps.create_default_diagnostic_keymaps
            "]d", "[d",
            -- quickfix
            "]q", "[q", "]<C-q>", "[<C-q>",
            -- local list
            "]l", "[l", "]<C-l>", "]<C-l>",
            -- spell
            "]s", "[s",
            -- fold
            "]z", "[z",
            -- gitsign
            "]c", "[c",
            -- neotest
            "]t", "[t", "]T", "[T",
            -- textobject
            "]f", "[f", "]a", "[a", "]m", "[m"
        },
        -- stylua: ignore end
        dependencies = {
            "jinh0/eyeliner.nvim",
            "nvim-treesitter/nvim-treesitter",
            "nvim-treesitter/nvim-treesitter-textobjects",
        },
        opts = {
            -- Create default keymaps
            keymaps = {
                -- Create t/T/f/F key mappings
                horizontal_motions = false,
                -- Create ]d/[d, etc. key mappings to jump to diganostics. See demicolon.keymaps.create_default_diagnostic_keymaps
                diagnostic_motions = true,
                -- Create ; and , key mappings
                repeat_motions = true,
                -- Create ]q/[q/]<C-q>/[<C-q> and ]l/[l/]<C-l>/[<C-l> quickfix and location list mappings
                list_motions = true,
                -- Create `]s`/`[s` key mappings for jumping to spelling mistakes
                spell_motions = true,
                -- Create `]z`/`[z` key mappings for jumping to folds
                fold_motions = true,
            },
            integrations = {
                -- Integration with https://github.com/lewis6991/gitsigns.nvim
                gitsigns = {
                    enabled = true,
                    keymaps = {
                        next = "]c",
                        prev = "[c",
                    },
                },
                -- Integration with https://github.com/nvim-neotest/neotest
                neotest = {
                    enabled = true,
                    keymaps = {
                        test = {
                            next = "]t",
                            prev = "[t",
                        },
                        failed_test = {
                            next = "]T",
                            prev = "[T",
                        },
                    },
                },
            },
        },
        config = function(_, opts)
            require("demicolon").setup(opts)

            local function eyeliner_jump(key)
                local forward = vim.list_contains({ "t", "f" }, key)
                return function()
                    require("eyeliner").highlight({ forward = forward })
                    return require("demicolon.jump").horizontal_jump(key)()
                end
            end

            local nxo = { "n", "x", "o" }
            local key_opts = { expr = true }

            vim.keymap.set(nxo, "f", eyeliner_jump("f"), key_opts)
            vim.keymap.set(nxo, "F", eyeliner_jump("F"), key_opts)
            vim.keymap.set(nxo, "t", eyeliner_jump("t"), key_opts)
            vim.keymap.set(nxo, "T", eyeliner_jump("T"), key_opts)
        end,
        -- event = vim.g.post_load_events,
    },
    {
        "folke/flash.nvim",
        enabled = true,
        -- event = "VeryLazy",
        ---@type Flash.Config
        opts = {
            modes = {
                search = {
                    enabled = false,
                },
                char = {
                    enabled = false,
                },
            },
            label = {
                rainbow = {
                    enabled = false,
                },
            },
        },
        keys = {
            {
                "s",
                mode = { "n", "x", "o" },
                function()
                    require("flash").jump()
                end,
                desc = "Flash",
            },
            {
                "S",
                mode = { "n", "o", "x" },
                function()
                    require("flash").treesitter()
                end,
                desc = "Flash Treesitter",
            },
            {
                "r",
                mode = "o",
                function()
                    require("flash").remote()
                end,
                desc = "Remote Flash",
            },
            {
                "R",
                mode = { "o", "x" },
                function()
                    require("flash").treesitter_search()
                end,
                desc = "Flash Treesitter Search",
            },
        },
    },
}
