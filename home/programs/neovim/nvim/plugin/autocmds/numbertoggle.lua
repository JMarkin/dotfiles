local fn = require("funcs")

vim.defer_fn(function()
  if vim.g.numbertoggle then
    fn.augroup("NumberToggle", {
      { "InsertLeave", "CmdlineLeave" },
      {
        callback = function(event)
          if
            vim.bo[event.buf].buflisted
            and vim.opt_local.number
            and vim.api.nvim_get_mode().mode ~= "i"
            and string.find(vim.fn.bufname(event.buf), "term://") == nil
          then
            vim.opt.relativenumber = true
          end
        end,
      },
    }, {
      { "InsertEnter", "CmdlineEnter" },
      {
        callback = function(event)
          if
            vim.bo[event.buf].buflisted
            and vim.opt_local.number
            and string.find(vim.fn.bufname(event.buf), "term://") == nil
          then
            vim.opt.relativenumber = false
            vim.cmd("redraw")
          end
        end,
      },
    })
  end
end, 100)
