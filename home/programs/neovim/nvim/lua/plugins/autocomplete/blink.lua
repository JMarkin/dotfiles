return {
    "saghen/blink.cmp",
    lazy = true,
    event = { "InsertEnter", "CmdlineEnter" },
    -- optional: provides snippets for the snippet source
    dependencies = {
        "L3MON4D3/LuaSnip",
        "saadparwaiz1/cmp_luasnip",
        "rafamadriz/friendly-snippets",
        "mikavilpas/blink-ripgrep.nvim",
        "danymat/neogen",
        { "saghen/blink.compat", opts = { impersonate_nvim_cmp = true } },
    },
    build = "nix run .#build-plugin",
    -- On musl libc based systems you need to add this flag
    -- build = 'RUSTFLAGS="-C target-feature=-crt-static" cargo build --release',

    opts = {
        keymap = {
            preset = "default",
            ["<C-a>"] = { "hide" },
            ["<c-b>"] = {},
            ["<CR>"] = { "accept", "fallback" },
            ["<C-e>"] = { "scroll_documentation_up", "fallback" },
            ["<C-d>"] = { "scroll_documentation_down", "fallback" },
            ["<C-p>"] = { "select_prev" },
            ["<C-n>"] = { "select_next" },
            ["<S-Tab>"] = {
                function(cmp)
                    local neogen = require("neogen")
                    if require("blink.cmp.completion.windows.menu").win:is_open() then
                        return cmp.select_prev()
                    elseif neogen.jumpable(true) then
                        vim.schedule(neogen.jump_prev)
                        return true
                    end
                end,
                "snippet_backward",
                "fallback",
            },
            ["<Tab>"] = {
                function(cmp)
                    local neogen = require("neogen")
                    if require("blink.cmp.completion.windows.menu").win:is_open() then
                        return cmp.select_next()
                    elseif neogen.jumpable() then
                        vim.schedule(neogen.jump_next)
                        return true
                    end
                end,
                "snippet_forward",
                "fallback",
            },
        },
        snippets = {
            expand = function(snippet)
                require("luasnip").lsp_expand(snippet)
            end,
            active = function(filter)
                if filter and filter.direction then
                    return require("luasnip").jumpable(filter.direction)
                end
                return require("luasnip").in_snippet()
            end,
            jump = function(direction)
                require("luasnip").jump(direction)
            end,
        },

        completion = {
            accept = {
                auto_brackets = {
                    enabled = false,
                },
            },
            ghost_text = {
                enabled = false,
            },
            trigger = {
                show_in_snippet = false,
            },
            list = {
                selection = "auto_insert",
            },
        },

        sources = {
            completion = {
                enabled_providers = { "lsp", "snippets", "buffer", "ripgrep", "dadbod" }, -- add "ripgrep" here
            },
            providers = {
                ripgrep = {
                    module = "blink-ripgrep",
                    name = "Ripgrep",
                },
                dadbod = { name = "Dadbod", module = "vim_dadbod_completion.blink" },
            },
        },

        appearance = {
            use_nvim_cmp_as_default = true,
            nerd_font_variant = "mono",
        },
    },
}
