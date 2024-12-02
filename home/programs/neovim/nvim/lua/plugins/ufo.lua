local is_not_mini = require("funcs").is_not_mini

local ftMap = {
    vim = "treesitter",
    python = "indent",
}

local handler = function(virtText, lnum, endLnum, width, truncate)
    local newVirtText = {}
    local suffix = (" lines %d "):format(endLnum - lnum)
    local sufWidth = vim.fn.strdisplaywidth(suffix)
    local targetWidth = width - sufWidth
    local curWidth = 0
    for _, chunk in ipairs(virtText) do
        local chunkText = chunk[1]
        local chunkWidth = vim.fn.strdisplaywidth(chunkText)
        if targetWidth > curWidth + chunkWidth then
            table.insert(newVirtText, chunk)
        else
            chunkText = truncate(chunkText, targetWidth - curWidth)
            local hlGroup = chunk[2]
            table.insert(newVirtText, { chunkText, hlGroup })
            chunkWidth = vim.fn.strdisplaywidth(chunkText)
            -- str width returned from truncate() may less than 2nd argument, need padding
            if curWidth + chunkWidth < targetWidth then
                suffix = suffix .. (" "):rep(targetWidth - curWidth - chunkWidth)
            end
            break
        end
        curWidth = curWidth + chunkWidth
    end
    table.insert(newVirtText, { suffix, "MoreMsg" })
    return newVirtText
end

return {
    "kevinhwang91/nvim-ufo",
    -- enabled = false,
    cond = is_not_mini,
    dependencies = { "kevinhwang91/promise-async", "nvim-treesitter" },
    event = { table.unpack(vim.g.post_load_events) },
    opts = {
        fold_virt_text_handler = handler,
        provider_selector = function(_, filetype, _)
            return ftMap[filetype] or { "treesitter", "indent" }
        end,
        open_fold_hl_timeout = 50,
        close_fold_kinds_for_ft = {
            default = { "imports", "comment" },
            json = { "array" },
            c = { "comment", "region" },
            python = { "comment" },
        },
        preview = {
            win_config = {
                border = { "", "─", "", "", "", "─", "", "" },
                -- winhighlight = "Normal:Folded",
                winblend = 0,
            },
            mappings = {
                scrollU = "<C-e>",
                scrollD = "<C-d>",
                jumpTop = "[",
                jumpBot = "]",
            },
        },
    },
    init = function()
        vim.o.fillchars = [[eob: ,fold: ,foldopen:,foldsep: ,foldclose:]]
        vim.o.foldcolumn = "1" -- '0' is not bad
        vim.o.foldlevel = 20 -- Using ufo provider need a large value, feel free to decrease the value
        vim.o.foldenable = true
    end,
    keys = {
        "z",
        {
            "zR",
            function()
                require("ufo").openAllFolds()
            end,
            desc = "Open All Folds",
        },
        {
            "zM",
            function()
                require("ufo").closeAllFolds()
            end,
            desc = "Close All Folds",
        },
        {
            "zr",
            function()
                require("ufo").openFoldsExceptKinds()
            end,
            desc = "Close All Folds",
        },
        {
            "zk",
            function()
                local winid = require("ufo").peekFoldedLinesUnderCursor()
                if not winid then
                    vim.lsp.buf.hover()
                end
            end,
            desc = "Hover doc",
        },
    },
}
