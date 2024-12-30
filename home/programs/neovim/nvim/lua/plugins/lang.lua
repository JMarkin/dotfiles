local is_not_mini = require("funcs").is_not_mini

return {
    {
        "mfussenegger/nvim-lint",
        lazy = true,
        enabled = true,
        config = function()
            require("lint").linters_by_ft = vim.g.linter_by_ft
        end,
    },
    {
        "stevearc/conform.nvim",
        -- event = vim.g.pre_load_events,
        -- event = "VeryLazy",
        cmd = { "ConformInfo" },
        keys = {
            {
                -- Customize or remove this keymap to your liking
                "<space>bf",
                function()
                    local buf = vim.api.nvim_get_current_buf()
                    if require("largefiles").is_large_file(buf, true) then
                        vim.notify_once("Large buf can't format", vim.log.levels.WARN)
                        return
                    end
                    require("conform").format({ async = true })
                end,
                mode = "",
                desc = "Format buffer",
            },
        },
        -- This will provide type hinting with LuaLS
        ---@module "conform"
        ---@type conform.setupOpts
        opts = {
            formatters_by_ft = vim.g.formatters_by_ft,
            default_format_opts = {
                lsp_format = "fallback",
            },
            -- Customize formatters
            formatters = {
                sqlfluff = {
                    prepend_args = { "--dialect", "postgres" },
                },
            },
        },
        init = function()
            vim.o.formatexpr = "v:lua.require'conform'.formatexpr()"
        end,
    },
    {
        "mrcjkb/rustaceanvim",
        cond = is_not_mini,
        version = "^5", -- Recommended
        lazy = false,
        -- enabled = false,
    },
    -- {
    --     "ray-x/go.nvim",
    --     dependencies = { -- optional packages
    --         "ray-x/guihua.lua",
    --         "neovim/nvim-lspconfig",
    --         "nvim-treesitter/nvim-treesitter",
    --     },
    --     config = function()
    --         require("go").setup()
    --     end,
    --     event = { "CmdlineEnter" },
    --     ft = { "go", "gomod" },
    --     build = ':lua require("go.install").update_all_sync()', -- if you need to install/update all binaries
    -- },
    {
        name = "clangd_extenstions",
        url = "https://git.sr.ht/~p00f/clangd_extensions.nvim",
        cond = is_not_mini,
        lazy = true,
    },
    { "b0o/schemastore.nvim", cond = is_not_mini, lazy = true },
    {
        "ranelpadon/python-copy-reference.vim",
        cond = is_not_mini,
        ft = { "python" },
        init = function()
            vim.g.python_remove_prefixes = { "src" }
        end,
        keys = {
            {
                "<leader>lcd",
                ":PythonCopyReferenceDotted<CR>",
                desc = "Copy as: Python Dotted",
            },
            {
                "<leader>lcp",
                ":PythonCopyReferencePytest<CR>",
                desc = "Copy as: Pytest",
            },
            {
                "<leader>lci",
                ":PythonCopyReferenceImport<CR>",
                desc = "Copy as: Python Import",
            },
        },
    },
    {
        "cuducos/yaml.nvim",
        ft = { "yaml" }, -- optional
        dependencies = {
            "nvim-treesitter",
        },
    },
    -- uncompiler
    {
        "p00f/godbolt.nvim",
        config = function()
            require("godbolt").setup()
        end,
        cmd = { "Godbolt", "GodboltCompiler" },
    },
}
