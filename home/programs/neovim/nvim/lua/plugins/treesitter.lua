local is_large_file = require("largefiles").is_large_file
local FILE_TYPE = require("largefiles").FILE_TYPE

local syntax_langs = {
    -- languages
    "rust",
    "c",
    "cpp",
    "cuda",
    "python",
    "typescript",
    "javascript",
    "fish",
    "go",
    "lua",
    "html",
    "htmldjango",
    "css",
    "bash",
    "vue",
    "scss",
    "sql",
    "markdown",
    "json",
    "json5",
    "jsonc",
    "graphql",
    "commonlisp",
    "latex",
    "glsl",
    -- conf files
    "ssh_config",
    "jsdoc",
    "yaml",
    "toml",
    "proto",
    "http",
    "hurl",
    "make",
    "cmake",
    "dockerfile",
    "ini",
    "vim",
    "vimdoc",
    "passwd",
    "requirements",
    "hcl",
    "xml",
    "nginx",
    "tmux",
    "udev",
    -- tools
    "markdown_inline",
    "jq",
    "regex",
    "query",
    "comment",
    "rst",

    -- git
    "gitcommit",
    "git_rebase",
    "gitignore",
    "git_config",
    "gitattributes",
}

vim.g.treesitter_langs = {}
for _, value in ipairs(syntax_langs) do
    vim.g.treesitter_langs[value] = 1
end

local install = function(sync)
    require("nvim-treesitter")
    for _, lang in ipairs(syntax_langs) do
        if sync then
            vim.cmd("TSUpdateSync " .. lang)
        else
            vim.cmd("TSUpdate " .. lang)
        end
    end
end

vim.api.nvim_create_user_command("TSInstallDefault", function(_)
    install()
end, {})

vim.api.nvim_create_user_command("TSInstallDefaultSync", function(_)
    install(true)
end, {})

---@diagnostic disable-next-line: unused-local
local is_disable = function(_lang, buf)
    local _type = is_large_file(buf)

    return _type ~= FILE_TYPE.NORMAL
    -- return _type == FILE_TYPE.READ_ONLY or _type == FILE_TYPE.LARGE_SIZE
end

return {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    -- enabled = false,
    lazy = true,
    -- ft = "qf",
    event = vim.g.post_load_events,
    -- event = "VeryLazy",
    dependencies = {
        {
            "m-demare/hlargs.nvim",
            -- dev = true,
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
                local rainbow_delimiters = require("rainbow-delimiters")
                require("rainbow-delimiters.setup").setup({
                    strategy = {
                        [""] = rainbow_delimiters.strategy["global"],
                        vim = rainbow_delimiters.strategy["local"],
                        commonlisp = rainbow_delimiters.strategy["local"],
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
                rainbow_delimiters.enable()
            end,
        },
        {
            "nvim-treesitter/nvim-treesitter-context",
            config = function()
                require("treesitter-context").setup({
                    enable = true, -- Enable this plugin (Can be enabled/disabled later via commands)
                    max_lines = 5, -- How many lines the window should span. Values <= 0 mean no limit.
                    min_window_height = 30, -- Minimum editor window height to enable context. Values <= 0 mean no limit.
                    line_numbers = true,
                    multiline_threshold = 20, -- Maximum number of lines to show for a single context
                    trim_scope = "outer", -- Which context lines to discard if `max_lines` is exceeded. Choices: 'inner', 'outer'
                    mode = "cursor", -- Line used to calculate context. Choices: 'cursor', 'topline'
                    -- Separator between context and content. Should be a single character string, like '-'.
                    -- When separator is set, the context will only show up when there are at least 2 lines above cursorline.
                    separator = nil,
                    zindex = 20, -- The Z-index of the context window
                    on_attach = function(buf)
                        return not is_disable(nil, buf)
                    end, -- (fun(buf: integer): boolean) return false to disable attaching
                })
            end,
        },
    },
    config = function()
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
}
