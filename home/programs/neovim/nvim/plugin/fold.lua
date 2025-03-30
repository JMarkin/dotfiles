local fn = require("funcs")

vim.o.foldenable = true
vim.o.foldlevel = 99
vim.o.foldmethod = "marker"
vim.o.foldmarker = "###,###"
vim.o.foldtext = ""
vim.opt.foldcolumn = "0"

vim.opt.fillchars:append({
    fold = "·",
    foldsep = " ",
})

if vim.g.modern_ui then
    vim.opt.fillchars:append({
        foldopen = "",
        foldclose = "",
    })
end

local function setfold(buf, func, rollback)
    if vim.b[buf].foldmethodfreeze then
        return
    end

    local win = vim.api.nvim_get_current_win()
    func(win)

    if not rollback then
        vim.b[buf].foldmethodfreeze = true
    end
end

local function undofold(buf)
    setfold(buf, function()
        vim.cmd([[setl foldmethod<]])
        vim.cmd([[setl foldexpr<]])
    end, true)
end

vim.api.nvim_create_user_command("FoldRegion", function(opts)
    local buf = vim.api.nvim_get_current_buf()

    if opts.bang then
        setfold(buf, function()
            vim.cmd([[setl foldmethod<]])
            vim.cmd([[setl foldmarker<]])
        end, true)
        return
    end

    setfold(buf, function(_win)
        vim.opt_local.foldmethod = "marker"
        vim.opt_local.foldmarker = "#region,#endregion"
    end, true)
end, { bang = true })

fn.augroup("TSFolding", {
    { "User" },
    {
        pattern = "TSFoldAttach",
        callback = function(args)
            setfold(args.buf, function(win)
                vim.wo[win][0].foldmethod = "expr"
                vim.wo[win][0].foldexpr = "v:lua.vim.treesitter.foldexpr()"
            end, true)
        end,
    },
}, {
    { "User" },
    {
        pattern = "TSFoldDetach",
        callback = function(args)
            undofold(args.buf)
        end,
    },
})

fn.augroup("LspFolding", {
    { "LspAttach" },
    {
        pattern = "*",
        callback = function(args)
            setfold(args.buf, function(win)
                local client = vim.lsp.get_client_by_id(args.data.client_id)
                if client:supports_method("textDocument/foldingRange") then
                    vim.wo[win][0].foldmethod = "expr"
                    vim.wo[win][0].foldexpr = "v:lua.vim.lsp.foldexpr()"
                end
            end, true)
        end,
    },
}, {
    { "LspDetach" },
    {
        pattern = "*",
        callback = function(args)
            undofold(args.buf)
        end,
    },
})

fn.augroup("FoldByFt", {
    { "FileType" },
    {
        pattern = "python",
        callback = function(args)
            setfold(args.buf, function(win)
                vim.wo[win][0].foldmethod = "indent"
            end)
        end,
    },
}, {
    { "FileType" },
    {
        pattern = { "vim", "help" },
        callback = function(args)
            setfold(args.buf, function(win)
                vim.wo[win][0].foldmethod = "marker"
                vim.wo[win][0].foldmarker = "{{{,}}}"
            end)
        end,
    },
})
