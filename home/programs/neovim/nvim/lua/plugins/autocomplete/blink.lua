local context = {}

-- https://github.com/hrsh7th/nvim-cmp/blob/main/lua/cmp/utils/api.lua
local api = {}
local CTRL_V = vim.api.nvim_replace_termcodes("<C-v>", true, true, true)
local CTRL_S = vim.api.nvim_replace_termcodes("<C-s>", true, true, true)

api.get_mode = function()
    local mode = vim.api.nvim_get_mode().mode:sub(1, 1)
    if mode == "i" then
        return "i" -- insert
    elseif mode == "v" or mode == "V" or mode == CTRL_V then
        return "x" -- visual
    elseif mode == "s" or mode == "S" or mode == CTRL_S then
        return "s" -- select
    elseif mode == "c" and vim.fn.getcmdtype() ~= "=" then
        return "c" -- cmdline
    end
end

api.is_insert_mode = function()
    return api.get_mode() == "i"
end

---Check if cursor is in syntax group
---@param group string | []string
---@return boolean
context.in_syntax_group = function(group)
    local row, col = unpack(vim.api.nvim_win_get_cursor(0))
    if not api.is_insert_mode() then
        col = col + 1
    end

    for _, syn_id in ipairs(vim.fn.synstack(row, col)) do
        syn_id = vim.fn.synIDtrans(syn_id) -- Resolve :highlight links
        local g = vim.fn.synIDattr(syn_id, "name")
        if type(group) == "string" and g == group then
            return true
        elseif type(group) == "table" and vim.tbl_contains(group, g) then
            return true
        end
    end

    return false
end

---Check if cursor is in treesitter capture
---@param capture string | []string
---@return boolean
context.in_treesitter_capture = function(capture)
    local buf = vim.api.nvim_get_current_buf()
    local row, col = unpack(vim.api.nvim_win_get_cursor(0))
    row = row - 1
    if vim.api.nvim_get_mode().mode == "i" then
        col = col - 1
    end

    local get_captures_at_pos = -- See neovim/neovim#20331
        require("vim.treesitter").get_captures_at_pos -- for neovim >= 0.8 or require('vim.treesitter').get_captures_at_position -- for neovim < 0.8

    local captures_at_cursor = vim.tbl_map(function(x)
        return x.capture
    end, get_captures_at_pos(buf, row, col))

    if vim.tbl_isempty(captures_at_cursor) then
        return false
    elseif type(capture) == "string" and vim.tbl_contains(captures_at_cursor, capture) then
        return true
    elseif type(capture) == "table" then
        for _, v in ipairs(capture) do
            if vim.tbl_contains(captures_at_cursor, v) then
                return true
            end
        end
    end

    return false
end

return {
    "saghen/blink.cmp",
    lazy = true,
    event = { "InsertEnter", "CmdlineEnter" },
    -- optional: provides snippets for the snippet source
    dependencies = {
        "rafamadriz/friendly-snippets",
        "mikavilpas/blink-ripgrep.nvim",
        "danymat/neogen",
        "quangnguyen30192/cmp-nvim-tags",
        "JMarkin/cmp-diag-codes",
        { "saghen/blink.compat", opts = { impersonate_nvim_cmp = true } },
    },
    -- version = "*",
    build = "nix run .#build-plugin",
    -- On musl libc based systems you need to add this flag
    -- build = 'RUSTFLAGS="-C target-feature=-crt-static" cargo build --release',
    -- init = function()
    --     local orig_list_selection
    --     vim.api.nvim_create_autocmd("CmdlineEnter", {
    --         callback = function()
    --             local list = require("blink.cmp.completion.list")
    --             orig_list_selection = list.config.selection
    --             list.config.selection = "manual"
    --         end,
    --     })
    --     vim.api.nvim_create_autocmd("CmdlineLeave", {
    --         callback = function()
    --             if orig_list_selection then
    --                 local list = require("blink.cmp.completion.list")
    --                 list.config.selection = orig_list_selection
    --             end
    --         end,
    --     })
    -- end,
    opts = {
        keymap = {
            cmdline = {
                ["<CR>"] = {
                    function(cmp)
                        return cmp.accept({
                            callback = function()
                                vim.api.nvim_feedkeys(
                                    vim.api.nvim_replace_termcodes("<CR>", true, true, true),
                                    "n",
                                    true
                                )
                            end,
                        })
                    end,
                    "fallback",
                },
                ["<Tab>"] = { "select_next" },
                ["<S-Tab>"] = { "select_prev" },
            },
            preset = "default",
            ["<C-a>"] = { "hide" },
            ["<C-k>"] = { "show_documentation", "hide_documentation" },
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
        -- snippets = {
        --     expand = function(snippet)
        --         require("luasnip").lsp_expand(snippet)
        --     end,
        --     active = function(filter)
        --         if filter and filter.direction then
        --             return require("luasnip").jumpable(filter.direction)
        --         end
        --         return require("luasnip").in_snippet()
        --     end,
        --     jump = function(direction)
        --         require("luasnip").jump(direction)
        --     end,
        -- },

        completion = {
            keyword = { range = "full" },
            accept = {
                auto_brackets = {
                    enabled = false,
                },
            },
            ghost_text = {
                enabled = true,
            },
            trigger = {
                show_in_snippet = false,
                show_on_keyword = true,
                show_on_trigger_character = true,
                show_on_insert_on_trigger_character = true,
                show_on_accept_on_trigger_character = true,
            },
            list = { selection = { preselect = false } },
        },

        sources = {
            default = function(ctx)
                if vim.bo.filetype == "sql" then
                    return { "dadbod", "ripgrep" }
                elseif vim.bo.filetype == "codecompanion" then
                    return { "codecompanion", "tags", "ripgrep" }
                elseif context.in_treesitter_capture("comment") or context.in_syntax_group("Comment") then
                    return { "diag-codes", "buffer", "snippets", "ripgrep" }
                else
                    return { "lsp", "path", "tags", "snippets", "buffer", "ripgrep" }
                end
            end,
            providers = {
                ripgrep = {
                    module = "blink-ripgrep",
                    name = "Ripgrep",
                    score_offset = -2,
                    opts = {},
                },
                dadbod = { name = "Dadbod", module = "vim_dadbod_completion.blink" },
                tags = {
                    name = "tags",
                    module = "blink.compat.source",
                    score_offset = -2,
                    opts = {
                        -- this is the default options, change them if you want.
                        -- Delayed time after user input, in milliseconds.
                        complete_defer = 100,
                        -- Max items when searching `taglist`.
                        max_items = 10,
                        -- The number of characters that need to be typed to trigger
                        -- auto-completion.
                        keyword_length = 3,
                        -- Use exact word match when searching `taglist`, for better searching
                        -- performance.
                        exact_match = false,
                        -- Prioritize searching result for current buffer.
                        current_buffer_only = false,
                    },
                },
                ["diag-codes"] = {
                    name = "diag-codes",
                    module = "blink.compat.source",
                    score_offset = 100,
                    opts = {
                        in_comment = false,
                    },
                },
            },
        },

        appearance = {
            use_nvim_cmp_as_default = true,
            nerd_font_variant = "mono",
        },

        fuzzy = {
            prebuilt_binaries = {
                download = false,
            },
        },
    },
}
