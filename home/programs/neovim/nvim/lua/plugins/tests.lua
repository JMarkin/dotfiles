local is_not_mini = require("funcs").is_not_mini
return {
    "nvim-neotest/neotest",
    cond = is_not_mini,
    dependencies = {
        "nvim-neotest/nvim-nio",
        "nvim-lua/plenary.nvim",
        "nvim-treesitter/nvim-treesitter",
        "antoinemadec/FixCursorHold.nvim",
        "nvim-neotest/neotest-python",
        "nvim-dap-ui",
    },
    keys = {
        {
            "<leader>ltt",
            function()
                require("neotest").summary.toggle()
            end,
            desc = "Tests",
        },
        {
            "<leader>lto",
            function()
                require("neotest").output_panel.toggle()
            end,
            desc = "Tests: output",
        },
    },
    config = function()
        require("neotest").setup({
            adapters = {
                require("neotest-python")({
                    dap = { justMyCode = false },
                    -- args = { "--log-level", "DEBUG", "--showlocals" },
                    runner = vim.g.python_test_runner or "pytest",
                }),
                require("rustaceanvim.neotest"),
            },
        })
    end,
    cmd = { "Neotest" },
}
