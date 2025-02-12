return {

    { "yorickpeterse/nvim-pqf", name = "pqf", enabled = false, config = true, ft = "qf" },
    {
        "stevearc/quicker.nvim",
        event = "FileType qf",
        opts = {
            keys = {
                {
                    ">",
                    function()
                        require("quicker").expand({ before = 2, after = 2, add_to_existing = true })
                    end,
                    desc = "Expand quickfix context",
                },
                {
                    "<",
                    function()
                        require("quicker").collapse()
                    end,
                    desc = "Collapse quickfix context",
                },
            },
        },
        keys = {
            {
                "<space>Q",
                function()
                    require("quicker").toggle()
                end,
                desc = "Toggle quickfix",
            },
            {
                "<space>l",
                function()
                    require("quicker").toggle({ loclist = true })
                end,
                desc = "Toggle loclist",
            },
        },
    },
    {
        "kevinhwang91/nvim-bqf",
        event = "VeryLazy",
        opts = {
            auto_enable = true,
            auto_resize_height = true,
        },
    },
}
