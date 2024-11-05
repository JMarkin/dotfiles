return {
    "saghen/blink.cmp",
    lazy = true,
    event = { "InsertEnter", "CmdlineEnter" },
    -- optional: provides snippets for the snippet source
    dependencies = {
        "rafamadriz/friendly-snippets",
        "netmute/blink-cmp-ctags",
        "niuiic/blink-cmp-rg.nvim",
    },

    -- OR build from source, requires nightly: https://rust-lang.github.io/rustup/concepts/channels.html#working-with-nightly-rust
    build = "rustup run nightly cargo build --release",
    -- On musl libc based systems you need to add this flag
    -- build = 'RUSTFLAGS="-C target-feature=-crt-static" cargo build --release',

    opts = {
        keymap = {
            show = "<C-space>",
            hide = "<C-a>",
            accept = "<cr>",
            select_prev = { "<Up>", "<C-p>", "<s-tab>" },
            select_next = { "<Down>", "<C-n>", "<tab>" },

            show_documentation = "<C-k>",
            hide_documentation = "<C-k>",
            scroll_documentation_up = "<C-e>",
            scroll_documentation_down = "<C-d>",

            snippet_forward = "<Tab>",
            snippet_backward = "<S-Tab>",
        },
        highlight = {
            -- sets the fallback highlight groups to nvim-cmp's highlight groups
            -- useful for when your theme doesn't support blink.cmp
            -- will be removed in a future release, assuming themes add support
            use_nvim_cmp_as_default = true,
        },
        -- set to 'mono' for 'Nerd Font Mono' or 'normal' for 'Nerd Font'
        -- adjusts spacing to ensure icons are aligned
        nerd_font_variant = "mono",

        sources = {
            completion = {
                enabled_providers = { "lsp", "snippets", "buffer", "ripgrep", "ctags" }, -- add "ripgrep" here
            },
            providers = {
                lsp = { module = "blink.cmp.sources.lsp", name = "LSP" },
                snippets = { module = "blink.cmp.sources.snippets", name = "Snippets", score_offset = -3 },
                buffer = { module = "blink.cmp.sources.buffer", name = "Buffer", fallback_for = { "lsp" } },
                ctags = { module = "blink-cmp-ctags", name = "Ctags", fallback_for = { "lsp" } },
                ripgrep = {
                    module = "blink-cmp-rg",
                    name = "Ripgrep",
                },
            },
        },

        -- experimental auto-brackets support
        accept = { auto_brackets = { enabled = true } },
        -- experimental signature help support
        trigger = { signature_help = { enabled = true } },
    },
    config = function(opts)
        local keymap = require("blink.cmp.keymap")
        local function apply_keymap_to_current_buffer()
            -- skip if we've already applied the keymaps
            for _, mapping in ipairs(vim.api.nvim_buf_get_keymap(0, "i")) do
                if mapping.desc == "blink.cmp" then
                    return
                end
            end
            local insert_keys_to_commands = {
                ["<CR>"] = { "accept" },
                ["<C-Space>"] = { "show" },
                ["<C-a>"] = { "hide" },
                ["<C-d>"] = { "scroll_documentation_down" },
                ["<C-e>"] = { "scroll_documentation_up" },
                ["<C-k>"] = { "show_documentation", "hide_documentation" },
                ["<Tab>"] = { "snippet_forward", "select_next" },
                ["<Down>"] = { "snippet_forward", "select_next" },
                ["<C-n>"] = { "snippet_forward", "select_next" },
                ["<S-Tab>"] = { "snippet_backward", "select_prev" },
                ["<Up>"] = { "snippet_backward", "select_prev" },
                ["<C-p>"] = { "snippet_backward", "select_prev" },
            }
            local snippet_keys_to_commands = {
                ["<Tab>"] = { "snippet_forward" },
                ["<Down>"] = { "snippet_forward" },
                ["<C-n>"] = { "snippet_forward" },
                ["<S-Tab>"] = { "snippet_backward" },
                ["<Up>"] = { "snippet_backward" },
                ["<C-p>"] = { "snippet_forward" },
            }

            -- insert mode: uses both snippet and insert commands
            for key, commands in pairs(insert_keys_to_commands) do
                keymap.set("i", key, function()
                    for _, command in ipairs(commands) do
                        local did_run = require("blink.cmp")[command]()
                        if did_run then
                            return
                        end
                    end
                    return keymap.run_non_blink_keymap("i", key)
                end)
            end

            -- snippet mode
            for key, commands in pairs(snippet_keys_to_commands) do
                keymap.set("s", key, function()
                    for _, command in ipairs(commands) do
                        local did_run = require("blink.cmp")[command]()
                        if did_run then
                            return
                        end
                    end
                    return keymap.run_non_blink_keymap("s", key)
                end)
            end
        end

        keymap.apply_keymap_to_current_buffer = apply_keymap_to_current_buffer
        require("blink.cmp").setup(opts)
    end,
}
