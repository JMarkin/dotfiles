local autocmd = vim.api.nvim_create_autocmd
local groupid = vim.api.nvim_create_augroup

local M = {}

M.get_size = function(path)
  local ok, stats = pcall(function()
    return vim.loop.fs_stat(path)
  end)
  if not (ok and stats) then
    return
  end
  return math.floor(0.5 + (stats.size / (1024 * 1024)))
end

M.is_text = function(path)
  -- Determine if file is text. This is not 100% proof, but good enough.
  -- Source: https://github.com/sharkdp/content_inspector
  local ok, fd = pcall(function()
    return vim.loop.fs_open(path, "r", 1)
  end)
  if not (ok and fd) then
    return false
  end
  ---@diagnostic disable-next-line: redefined-local
  local ok, bytes = pcall(function()
    return vim.loop.fs_read(fd, 1024)
  end)
  if not (ok and bytes) then
    return false
  end
  local is_text = bytes:find("\0") == nil
  vim.loop.fs_close(fd)
  return is_text
end

-- copy from https://github.com/Bekaboo/nvim/blob/master/lua/core/autocmds.lua
---@param group string
---@vararg { [1]: string|string[], [2]: vim.api.keyset.create_autocmd }
---@return nil
M.augroup = function(group, ...)
  local id = groupid(group, { clear = true })
  for _, a in ipairs({ ... }) do
    a[2].group = id
    autocmd(unpack(a))
  end
end

M.pcall_notify = function(func)
  local ok, out = pcall(func)
  if not ok then
    vim.notify_once(string.format("%s", out), vim.log.levels.DEBUG)
  end
  return out
end

M.is_not_mini = function()
  return vim.env.NVIM_MINI == nil
end

M.doau = function(pattern, data)
  vim.api.nvim_exec_autocmds("User", {
    pattern = pattern,
    data = data,
  })
end

function M.maxline(path, break_after)
  if break_after == nil then
    break_after = vim.o.synmaxcol + 1
  end
  local max = 0
  local fd = vim.uv.fs_open(path, "r", 1)
  if not fd then
    return max
  end
  local stat = vim.uv.fs_fstat(fd)
  local data = vim.uv.fs_read(fd, stat.size, nil)
  vim.uv.fs_close(fd)
  if not data then
    return max
  end

  local lines = vim.split(data, "[\r]?\n")

  for _, line in pairs(lines) do
    if max < #line then
      max = #line
    end
    if max >= break_after then
      return max
    end
  end
  return max
end

-- Executes a user-supplied "reducer" callback function on each element of the table indexed with a numeric key, in order, passing in the return value from the calculation on the preceding element
M.ireduce = function(tbl, func, acc)
  for i, v in ipairs(tbl) do
    acc = func(acc, v, i)
  end
  return acc
end

-- Returns the first element in the array that satisfies the provided testing function
M.ifind = function(tbl, func)
  for index, item in ipairs(tbl) do
    if func(item, index) then
      return item
    end
  end

  return nil
end

-- Function to merge two tables in Lua using Neovim.
function M.merge_tables(table1, table2)
  local merged_table = table1 or {} -- Ensure a valid table, even if nil
  for k, _ in pairs(table2) do
    merged_table[k] = table2[k]
  end

  -- Return the merged table.
  return merged_table
end

function M.debounce(ms, func)
  local entry = { timer = nil, cancel = nil }

  entry.timer = vim.uv.new_timer()
  entry.timer:start(
    ms,
    0,
    vim.schedule_wrap(function()
      entry.cancel = func()
    end)
  )

  return entry
end

-- https://github.com/hrsh7th/nvim-cmp/blob/main/lua/cmp/utils/api.lua
local api = {}
local CTRL_V = vim.api.nvim_replace_termcodes("<C-v>", true, true, true)
local CTRL_S = vim.api.nvim_replace_termcodes("<C-s>", true, true, true)

api.get_mode = function()
  local mode = vim.api.nvim_get_mode().mode:sub(1, 1)
  if mode == "i" then
    return "i" -- insert
  elseif mode == "v" or mode == "V" or mode == CTRL_V then
    return "x" -- visual
  elseif mode == "s" or mode == "S" or mode == CTRL_S then
    return "s" -- select
  elseif mode == "c" and vim.fn.getcmdtype() ~= "=" then
    return "c" -- cmdline
  end
end

api.is_insert_mode = function()
  return api.get_mode() == "i"
end

---Check if cursor is in syntax group
---@param group string | []string
---@return boolean
M.in_syntax_group = function(group)
  local row, col = unpack(vim.api.nvim_win_get_cursor(0))
  if not api.is_insert_mode() then
    col = col + 1
  end

  for _, syn_id in ipairs(vim.fn.synstack(row, col)) do
    syn_id = vim.fn.synIDtrans(syn_id) -- Resolve :highlight links
    local g = vim.fn.synIDattr(syn_id, "name")
    if type(group) == "string" and g == group then
      return true
    elseif type(group) == "table" and vim.tbl_contains(group, g) then
      return true
    end
  end

  return false
end

---Check if cursor is in treesitter capture
---@param capture string | []string
---@return boolean
M.in_treesitter_capture = function(capture)
  local buf = vim.api.nvim_get_current_buf()
  local row, col = unpack(vim.api.nvim_win_get_cursor(0))
  row = row - 1
  if vim.api.nvim_get_mode().mode == "i" then
    col = col - 1
  end

  local get_captures_at_pos = -- See neovim/neovim#20331
    require("vim.treesitter").get_captures_at_pos -- for neovim >= 0.8 or require('vim.treesitter').get_captures_at_position -- for neovim < 0.8

  local captures_at_cursor = vim.tbl_map(function(x)
    return x.capture
  end, get_captures_at_pos(buf, row, col))

  if vim.tbl_isempty(captures_at_cursor) then
    return false
  elseif type(capture) == "string" and vim.tbl_contains(captures_at_cursor, capture) then
    return true
  elseif type(capture) == "table" then
    for _, v in ipairs(capture) do
      if vim.tbl_contains(captures_at_cursor, v) then
        return true
      end
    end
  end

  return false
end
return M
