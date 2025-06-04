local lf = require("largefiles")
local fn = require("funcs")

fn.augroup(
  "lspconfig",
  {
    vim.g.pre_load_events,
    {
      pattern = "*",
      callback = function()
        require("lsp")
      end,
      once = true,
    },
  }
)

fn.augroup("linting", {
  { "BufWritePost", table.unpack(vim.g.post_load_events) },
  {
    pattern = { "*" },
    callback = function(data)
      if not lf.is_large_file(data.buf, true) then
        require("lint").try_lint()
      end
    end,
  },
})
