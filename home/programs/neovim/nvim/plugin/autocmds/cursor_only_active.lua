-- Show cursor line only in active window.
-- https://github.com/folke/dot/blob/master/nvim/lua/config/autocmds.lua

local fn = require("funcs")

fn.augroup("cursoronlyactivate", {
  { "InsertLeave", "WinEnter" },
  {
    callback = function()
      if vim.wo.previewwindow then
        return
      end

      if vim.w.auto_cursorline then
        vim.wo.cursorline = true
        vim.w.auto_cursorline = false
      end
    end,
  },
}, {
  { "InsertEnter", "WinLeave" },
  {
    callback = function()
      if vim.wo.previewwindow then
        return
      end

      if vim.wo.cursorline then
        vim.w.auto_cursorline = true
        vim.wo.cursorline = false
      end
    end,
  },
})
