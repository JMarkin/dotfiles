local fn = require("funcs")

--
-- Use 'q' to quit from common plugins
fn.augroup("quit", {
    "FileType",
    {
        pattern = {
            "help",
            "man",
            "lspinfo",
            "trouble",
            "null-ls-info",
            "qf",
            "notify",
            "startuptime",
            "checkhealth",
            "neotest-output",
            "neotest-output-panel",
            "neotest-summary",
            "vista_kind",
            "sagaoutline",
        },
        callback = function(event)
            vim.opt_local.wrap = false
            vim.bo[event.buf].buflisted = false
            vim.keymap.set("n", "q", "<cmd>close<cr>", { buffer = event.buf, silent = true })
        end,
    },
})

fn.augroup("spell", {
    "FileType",
    {
        pattern = { "gitcommit", "markdown", "text" },
        callback = function()
            vim.opt_local.spell = true
        end,
    },
})
