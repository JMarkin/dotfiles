return {
    "antoinemadec/FixCursorHold.nvim",

    { "yorickpeterse/nvim-pqf", name = "pqf", config = true, ft = "qf" },

    {
        "kevinhwang91/nvim-bqf",
        ft = "qf",
        event = "VeryLazy",
        opts = {
            auto_enable = true,
            auto_resize_height = true,
        },
    },
    {
        "dstein64/vim-startuptime",
        cmd = { "StartupTime" },
        init = function()
            vim.g.startuptime_tries = 10
        end,
    },
    -- sudo
    {
        "lambdalisue/suda.vim",
        cmd = { "SudaRead", "SudaWrite" },
    },
    {
        "gbprod/stay-in-place.nvim",
        opts = {
            set_keymaps = true,
            preserve_visual_selection = true,
        },
        event = "ModeChanged",
    },

    {
        "farmergreg/vim-lastplace",
        init = function()
            vim.g.lastplace_ignore = "gitcommit,gitrebase,svn,hgcommit"
            vim.g.lastplace_ignore_buftype = "quickfix,nofile,help"
            vim.g.lastplace_open_folds = 1
        end,
    },
    {
        "JMarkin/gentags.lua",
        -- enabled = false,
        -- dev = true,
        cond = vim.fn.executable("ctags") == 1,
        opts = {
            autostart = false,
            async = false,
            args = {
                "--extras=+r+q",
                "--exclude=\\.*",
                "--exclude=.mypy_cache",
                "--exclude=.ruff_cache",
                "--exclude=.pytest_cache",
                "--exclude=dist",
                "--exclude=.git",
                "--exclude=node_modules*",
                "--exclude=BUILD",
                "--exclude=vendor*",
                "--exclude=*.min.*",
                "--exclude=__file__",
            },
        },
        cmd = {
            "GenCTags",
            "GenTagsEnable",
            "GenTagsDisable",
        },
    },
    {
        "lewis6991/whatthejump.nvim",
        -- enabled = false,
        keys = { "<C-i>", "<C-o>" },
    },

    {
        "m4xshen/hardtime.nvim",
        event = "VeryLazy",
        enabled = false,
        dependencies = { "MunifTanjim/nui.nvim", "nvim-lua/plenary.nvim" },
        opts = {
            disabled_filetypes = { "qf", "netrw", "NvimTree", "lazy", "mason", "dashboard", "vista", "vista_kind" },
            disable_mouse = false,
            restriction_mode = "hint",
        },
    },
}
