return {
    "antoinemadec/FixCursorHold.nvim",

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
        "m4xshen/hardtime.nvim",
        event = "VeryLazy",
        enabled = false,
        dependencies = { "MunifTanjim/nui.nvim", "nvim-lua/plenary.nvim" },
        opts = {
            disabled_filetypes = { "qf", "netrw", "NvimTree", "lazy", "mason", "dashboard", "vista", "vista_kind" },
            disable_mouse = true,
            restriction_mode = "hint",
            disabled_keys = {
                ["<Up>"] = { "n" },
                ["<Left>"] = { "n" },
                ["<Right>"] = { "n" },
                ["<Down>"] = { "n" },
            },
        },
    },
    {
      "mistricky/codesnap.nvim",
      build = "make build_generator",
      cmd = {"CodeSnap", "CodeSnapSave"},
      opts = {
            mac_window_bar = false,
        save_path = "~/Downloads",
        has_breadcrumbs = true,
        code_font_family = "JetBrainsMonoNL Nerd Font Mono",
        bg_x_padding = 0,
        bg_y_padding = 0,
        bg_padding = nil,
        watermark = ""
      },
    },
}
