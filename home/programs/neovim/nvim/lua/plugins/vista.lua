local autocmd = vim.api.nvim_create_autocmd
local augroup = vim.api.nvim_create_augroup

return {
    "liuchengxu/vista.vim",
    cmd = { "Vista" },
    keys = { { "<space>T", ":Vista ctags<cr>", desc = "Tagbar" } },
    init = function()
        vim.g.vista_update_on_text_changed = 1
        vim.g.vista_disable_statusline = 1
        vim.g.vista_sidebar_width = 30
        vim.g.vista_sidebar_open_cmd = "30vsplit"
        vim.g.vista_echo_cursor_strategy = "floating_win"
        vim.g.vista_close_on_jump = 0
    end,
    config = function()
        autocmd("FileType", {
            group = augroup("vista", { clear = true }),
            pattern = {
                "vista_kind",
                "vista",
            },
            callback = function(event)
                vim.keymap.set("n", "<space>T", "<cmd>close<cr>", { buffer = event.buf, silent = true })
                vim.keymap.set(
                    "n",
                    "o",
                    ":<c-u>call vista#cursor#FoldOrJump()<cr>",
                    { buffer = event.buf, silent = true, noremap = true }
                )
                vim.cmd([[vertical resize 30]])
            end,
        })
    end,
}
