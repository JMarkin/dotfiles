return {
    {
        "folke/which-key.nvim",
        event = "VeryLazy",
        enabled = true,
        opts_extend = { "spec" },
        opts = {
            defaults = {},
            preset = "helix",
            keys = {
                scroll_down = "<c-d>", -- binding to scroll down inside the popup
                scroll_up = "<c-e>", -- binding to scroll up inside the popup
            },
            spec = {
                {
                    mode = { "n", "v" },
                    { "<leader>d", group = "dap" },
                    { "<leader>g", group = "git" },
                    { "<leader>s", group = "search" },
                    { "<leader>l", group = "lang", icon = { icon = "󱖫 ", color = "green" } },
                    { "[", group = "prev" },
                    { "]", group = "next" },
                    { "g", group = "goto" },
                    { "gz", group = "surround" },
                    { "z", group = "fold" },
                    { "m", group = "mark" },
                    { "M", group = "mark" },
                    { "dm", group = "mark" },
                    { "<Leader>lc", group = "copy_as" },
                    { "<Leader>lt", group = "tests" },
                    { "<Leader>h", group = "http" },
                    {
                        "<space>b",
                        group = "buffer",
                        expand = function()
                            return require("which-key.extras").expand.buf()
                        end,
                    },
                },
            },
            triggers = {
                { "<auto>", mode = "nixsotc" },
            },
        },
        keys = {
            {
                "<leader>?",
                function()
                    require("which-key").show({ global = false })
                end,
                desc = "Buffer Keymaps (which-key)",
            },
            {
                "<c-w><space>",
                function()
                    require("which-key").show({ keys = "<c-w>", loop = true })
                end,
                desc = "Window Hydra Mode (which-key)",
            },
        },
        config = function(_, opts)
            local wk = require("which-key")
            wk.setup(opts)
        end,
    },
    {
        "echasnovski/mini.clue",
        event = "VimEnter",
        enabled = false,
        config = function()
            local miniclue = require("mini.clue")
            miniclue.setup({
                window = {
                    delay = 200,
                },
                triggers = {

                    -- motion triggers
                    { mode = "n", keys = "[" },
                    { mode = "n", keys = "]" },

                    -- space triggers
                    { mode = "n", keys = "<space>" },

                    -- Leader triggers
                    { mode = "n", keys = "<Leader>" },
                    { mode = "x", keys = "<Leader>" },

                    -- Built-in completion
                    { mode = "i", keys = "<C-x>" },

                    -- `g` key
                    { mode = "n", keys = "g" },
                    { mode = "x", keys = "g" },

                    -- Marks
                    { mode = "n", keys = "'" },
                    { mode = "n", keys = "`" },
                    { mode = "x", keys = "'" },
                    { mode = "x", keys = "`" },

                    -- Registers
                    { mode = "n", keys = '"' },
                    { mode = "x", keys = '"' },
                    { mode = "i", keys = "<C-r>" },
                    { mode = "c", keys = "<C-r>" },

                    -- Window commands
                    { mode = "n", keys = "<C-w>" },

                    -- `z` key
                    { mode = "n", keys = "z" },
                    { mode = "x", keys = "z" },
                },

                clues = {
                    miniclue.gen_clues.g(),
                    miniclue.gen_clues.marks(),
                    miniclue.gen_clues.registers(),
                    miniclue.gen_clues.windows(),
                    miniclue.gen_clues.z(),

                    { mode = "n", keys = "gz", desc = "Surround" },
                    { mode = "n", keys = "<space>b", desc = "Buffers" },
                    { mode = "n", keys = "<Leader>l", desc = "Lang" },
                    { mode = "n", keys = "<Leader>g", desc = "Git" },
                    { mode = "v", keys = "<Leader>g", desc = "Git" },
                    { mode = "n", keys = "<Leader>s", desc = "Search" },
                    { mode = "v", keys = "<Leader>s", desc = "Search" },
                    { mode = "n", keys = "<Leader>d", desc = "Debug" },
                    { mode = "v", keys = "<Leader>d", desc = "Debug" },
                    { mode = "n", keys = "<Leader>s", desc = "Search" },
                    { mode = "n", keys = "<Leader>lc", desc = "Copy as" },
                    { mode = "n", keys = "<Leader>lt", desc = "Tests" },
                    { mode = "n", keys = "<Leader>h", desc = "Http" },

                    -- completions
                    { mode = "i", keys = "<C-x><C-d>", desc = "Defined identifiers" },
                    { mode = "i", keys = "<C-x><C-e>", desc = "Scroll up" },
                    { mode = "i", keys = "<C-x><C-i>", desc = "Identifiers" },
                    { mode = "i", keys = "<C-x><C-k>", desc = "Identifiers from dictionary" },
                    { mode = "i", keys = "<C-x><C-l>", desc = "Whole lines" },
                    { mode = "i", keys = "<C-x><C-n>", desc = "Next completion" },
                    { mode = "i", keys = "<C-x><C-o>", desc = "Omni completion" },
                    { mode = "i", keys = "<C-x><C-p>", desc = "Previous completion" },
                    { mode = "i", keys = "<C-x><C-s>", desc = "Spelling suggestions" },
                    { mode = "i", keys = "<C-x><C-t>", desc = "Identifiers from thesaurus" },
                    { mode = "i", keys = "<C-x><C-y>", desc = "Scroll down" },
                    { mode = "i", keys = "<C-x><C-u>", desc = "With 'completefunc'" },
                    { mode = "i", keys = "<C-x><C-v>", desc = "Like in command line" },
                    { mode = "i", keys = "<C-x><C-z>", desc = "Stop completion" },
                    { mode = "i", keys = "<C-x>s", desc = "Spelling suggestions" },

                    { mode = "i", keys = "<c-x><c-f>", desc = "Files" },
                    { mode = "i", keys = "<c-x><c-]>", desc = "Tags" },
                },
            })
        end,
    },
}
