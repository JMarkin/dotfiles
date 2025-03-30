local is_large_file = require("largefiles").is_large_file
local fn = require("funcs")
local FILE_TYPE = require("largefiles").FILE_TYPE

---@diagnostic disable-next-line: unused-local
local is_disable = function(_lang, buf)
    local _type = is_large_file(buf)

    local r = _type ~= FILE_TYPE.NORMAL
    if r then
        fn.doau("TSFoldAttach", { buf = buf })
    end

    return r
    -- return _type == FILE_TYPE.READ_ONLY or _type == FILE_TYPE.LARGE_SIZE
end

return {
    "nvim-treesitter/nvim-treesitter",
    -- build = ":TSUpdate",
    -- enabled = false,
    lazy = true,
    dir = vim.fn.stdpath("data") .. "/nix/nvim-treesitter",
    dev = true,
    -- ft = "qf",
    event = vim.g.post_load_events,
    -- event = "VeryLazy",
    dependencies = {
        {
            "m-demare/hlargs.nvim",
        },
        "yioneko/nvim-yati",
        {
            "andymass/vim-matchup",
            -- enabled = false,
            init = function()
                vim.g.matchup_transmute_enabled = 1

                vim.g.matchup_delim_noskips = 2
                vim.g.matchup_matchparen_deferred = 0
                vim.g.matchup_delim_start_plaintext = 1

                vim.g.matchup_matchparen_hi_surround_always = 1
                vim.g.matchup_matchparen_nomode = "i"
                vim.g.matchup_matchparen_deferred = 1
                vim.g.matchup_matchparen_deferred_show_delay = 100
                vim.g.matchup_matchparen_deferred_hide_delay = 500
                vim.g.matchup_matchparen_offscreen = { method = "popup" }
            end,
        },
        {
            "HiPhish/rainbow-delimiters.nvim",
            enabled = false,
            config = function()
                local rainbow = require("rainbow-delimiters")
                require("rainbow-delimiters.setup").setup({
                    strategy = {
                        [""] = function(bufnr)
                            if is_large_file(bufnr, true) then
                                return nil
                            else
                                local line_count = vim.api.nvim_buf_line_count(bufnr)
                                if line_count < 100 then
                                    return rainbow.strategy["global"]
                                end
                            end
                            return rainbow.strategy["local"]
                        end,
                    },
                    query = {
                        [""] = "rainbow-delimiters",
                        lua = "rainbow-blocks",
                        latex = "rainbow-blocks",
                    },
                    priority = {
                        [""] = 210,
                    },
                    highlight = vim.g.rainbow_delimiters_highlight,
                })
                rainbow.enable()
            end,
        },
        {
            "nvim-treesitter/nvim-treesitter-context",
            config = function()
                local tsc = require("treesitter-context")
                tsc.setup({
                    enable = true, -- Enable this plugin (Can be enabled/disabled later via commands)
                    max_lines = 5, -- How many lines the window should span. Values <= 0 mean no limit.
                    min_window_height = 30, -- Minimum editor window height to enable context. Values <= 0 mean no limit.
                    line_numbers = true,
                    multiline_threshold = 20, -- Maximum number of lines to show for a single context
                    trim_scope = "outer", -- Which context lines to discard if `max_lines` is exceeded. Choices: 'inner', 'outer'
                    mode = "cursor", -- Line used to calculate context. Choices: 'cursor', 'topline'
                    -- Separator between context and content. Should be a single character string, like '-'.
                    -- When separator is set, the context will only show up when there are at least 2 lines above cursorline.
                    -- separator = "-",
                    zindex = 20, -- The Z-index of the context window
                    on_attach = function(buf)
                        return not is_disable(nil, buf)
                    end, -- (fun(buf: integer): boolean) return false to disable attaching
                })
                vim.api.nvim_create_autocmd({ "DiagnosticChanged" }, {
                    callback = function()
                        if tsc.enabled() then
                            tsc.disable()
                            tsc.enable()
                        end
                    end,
                })
            end,
        },
        "nvim-treesitter/nvim-treesitter-textobjects",
    },
    config = function()
        require("nvim-treesitter").define_modules({
            fold = {
                attach = function(buf, lang)
                    fn.doau("TSFoldAttach", { buf = buf })
                end,
                detach = function(buf)
                    fn.doau("TSFoldDetach", { buf = buf })
                end,
            },
        })
        require("nvim-treesitter.install").prefer_git = true
        require("nvim-treesitter.configs").setup({
            autotag = {
                enable = false,
                disable = is_disable,
            },
            highlight = {
                enable = true,
                additional_vim_regex_highlighting = true,
                disable = is_disable,
            },
            incremental_selection = {
                enable = true,
                keymaps = {
                    init_selection = "<cr>",
                    node_incremental = "<cr>",
                    scope_incremental = "<tab>",
                    node_decremental = "<s-tab>",
                },
                disable = is_disable,
            },
            yati = {
                enable = true,
                disable = is_disable,
            },
            indent = {
                enable = false,
                disable = is_disable,
            },
            matchup = {
                enable = true,
                include_match_words = true,
                disable = is_disable,
            },
            textobjects = {
                move = {
                    enable = true,
                    goto_next_start = {
                        ["]f"] = "@function.outer",
                        ["]a"] = "@argument.outer",
                        ["]m"] = "@method.outer",
                    },
                    goto_previous_start = {
                        ["[f"] = "@function.outer",
                        ["[a"] = "@argument.outer",
                        ["[m"] = "@method.outer",
                    },
                },
            },
        })

        vim.treesitter.language.register("htmldjango", "jinja")

        require("hlargs").setup({
            use_colorpalette = true,
            paint_arg_declarations = true,
            paint_arg_usages = true,
            paint_catch_blocks = {
                declarations = true,
                usages = true,
            },
            extras = {
                named_parameters = true,
            },
            excluded_argnames = {
                declarations = {},
                usages = {
                    python = {},
                    lua = {},
                },
            },
            disable = is_disable,
            excluded_filetypes = { "jinja", "htmldjango" },
        })
    end,
    init = function()
        local prev = vim.treesitter.language.get_lang
        vim.treesitter.language.get_lang = function(...)
            require("lazy").load({ plugins = { "nvim-treesitter" } })
            return prev(...)
        end
    end,
}
