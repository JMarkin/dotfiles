local fn = require("funcs")

fn.augroup("Format Options", {
    "BufReadPost",
    {
        callback = function()
            vim.opt_local.formatoptions = vim.opt_local.formatoptions
                - "a" -- Auto formatting is BAD.
                - "t" -- Don't auto format my code. I got linters for that.
                + "c" -- In general, I like it when comments respect textwidth
                + "q" -- Allow formatting comments w/ gq
                - "o" -- O and o, don't continue comments
                + "r" -- But do continue when pressing enter.
                + "n" -- Indent past the formatlistpat, not underneath it.
                + "j" -- Auto-remove comments if possible.
                - "2" -- I'm not in gradeschool anymore
                + "p" --
        end,
    },
})

-- Auto create dir when saving a file, in case some intermediate directory does not exist
fn.augroup("autocreatedir", {
    { "BufWritePre" },
    {
        callback = function(event)
            if event.match:match("^%w%w+://") then
                return
            end
            local file = vim.uv.fs_realpath(event.match) or event.match
            vim.fn.mkdir(vim.fn.fnamemodify(file, ":p:h"), "p")
        end,
    },
})

-- Check if we need to reload the file when it changed
fn.augroup("checktime", {
    { "BufEnter", "CursorHold", "CursorHoldI", "FocusGained", "TermLeave", "TermClose" },
    {
        command = "if mode() != 'c' | checktime | endif",
        pattern = { "*" },
    },
})

vim.api.nvim_create_autocmd("CmdlineLeave", {
    once = true,
    callback = function()
        if vim.v.event.cmdtype ~= '/' then
            return
        end
        fn.augroup("nohl", { { 'InsertEnter', 'CursorHold' }, {
            callback = function()
                if vim.v.hlsearch == 0 then
                    return
                end
                local keycode = vim.api.nvim_replace_termcodes('<Cmd>nohl<CR>', true, false, true)
                vim.api.nvim_feedkeys(keycode, 'n', false)
            end,
        } })
    end
}
)


if vim.env.TERM == 'alacritty' then
    vim.api.nvim_create_autocmd('ExitPre', {
        once = true,
        command = 'set guicursor=a:ver90',
        desc = 'Set cursor back to beam when leaving Neovim.',
    })
end
