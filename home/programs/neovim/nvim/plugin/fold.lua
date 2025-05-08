local fn = require("funcs")

vim.o.foldenable = true
vim.o.foldlevel = 99
vim.o.foldmethod = "marker"
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

local function setfold(_buf, func)
  local win = vim.api.nvim_get_current_win()
  func(win)
end

local function undofoldexpr(buf)
  setfold(buf, function()
    vim.cmd([[setl foldmethod<]])
    vim.cmd([[setl foldexpr<]])
  end)
end

local function undofoldmarker(buf)
  setfold(buf, function()
    vim.cmd([[setl foldmethod<]])
    vim.cmd([[setl foldexpr<]])
  end)
end

vim.api.nvim_create_user_command("FoldDefault", function(opts)
  local buf = vim.api.nvim_get_current_buf()

  if opts.bang then
    undofoldmarker(buf)
    return
  end

  setfold(buf, function(_win)
    vim.opt_local.foldmethod = "marker"
    vim.opt_local.foldmarker = "{{{,}}}"
  end)
end, { bang = true })

vim.api.nvim_create_user_command("FoldRegion", function(opts)
  local buf = vim.api.nvim_get_current_buf()

  if opts.bang then
    undofoldmarker(buf)
    return
  end

  setfold(buf, function(_win)
    vim.opt_local.foldmethod = "marker"
    vim.opt_local.foldmarker = "#region,#endregion"
  end)
end, { bang = true })

vim.api.nvim_create_user_command("FoldTS", function(opts)
  local buf = vim.api.nvim_get_current_buf()

  if opts.bang then
    undofoldexpr(buf)
    return
  end

  setfold(buf, function(win)
    vim.opt_local.foldmethod = "expr"
    vim.opt_local.foldexpr = "v:lua.vim.treesitter.foldexpr()"
  end)
end, { bang = true })

vim.api.nvim_create_user_command("FoldLsp", function(opts)
  local buf = vim.api.nvim_get_current_buf()

  if opts.bang then
    undofoldexpr(buf)
    return
  end

  setfold(buf, function(win)
    vim.opt_local.foldmethod = "expr"
    vim.opt_local.foldexpr = "v:lua.vim.lsp.foldexpr()"
  end)
end, { bang = true })

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
    pattern = { "vim" },
    callback = function(args)
      setfold(args.buf, function(win)
        vim.wo[win][0].foldmethod = "marker"
        vim.wo[win][0].foldmarker = "{{{,}}}"
      end)
    end,
  },
}, {
  { "FileType" },
  {
    pattern = { "json" },
    callback = function(args)
      setfold(args.buf, function(win)
        vim.wo[win][0].foldmethod = "syntax"
      end)
    end,
  },
})
