return {

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
}
