local float = require("extend-netrw.float-preview")
local keymap = require("extend-netrw.keymap")

local buf = vim.api.nvim_get_current_buf()

-- vim.bo[buf].buflisted = false
vim.opt_local.wrap = false
vim.opt_local.number = false
vim.opt_local.bufhidden = "wipe"
vim.opt_local.colorcolumn = ""

keymap.init(buf)
float.attach_netrw(buf)
