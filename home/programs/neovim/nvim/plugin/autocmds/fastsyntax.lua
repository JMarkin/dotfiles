local fn = require("funcs")

fn.augroup("fastsyntax", {
  { "BufWinEnter", "Syntax" },
  {
    pattern = "*",
    command = "syn sync minlines=500 maxlines=500",
  },
})

fn.augroup("omnifuncsetter", {
  { "FileType" },
  {
    pattern = "*",
    callback = function()
      if vim.opt.omnifunc == "" then
        vim.opt_local.omnifunc = "syntaxcomplete#Complete"
      end
    end,
  },
})
