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
      "PlenaryTestPopup",
      "dbout",
      "gitsigns-blame",
      "grug-far",
      "spectre_panel",
      "tsplayground",
    },
    callback = function(event)
      vim.opt_local.wrap = false
      vim.bo[event.buf].buflisted = false
      vim.schedule(function()
        vim.keymap.set("n", "q", "<cmd>close<cr>", { buffer = event.buf, silent = true })
      end)
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

fn.augroup("tempfile", {
  { "BufWritePre" },
  {
    pattern = { "/tmp/*", "COMMIT_EDITMSG", "MERGE_MSG", "*.tmp", "*.bak" },
    command = "setlocal noundofile",
  },
})
