local M = {}

local funcs = require("funcs")

local get_payload = function()
    local parse = require("netrw.parse")

    local bufnr = vim.api.nvim_get_current_buf()
    local winid = vim.api.nvim_get_current_win()

    local row, _ = unpack(vim.api.nvim_win_get_cursor(winid))
    local line = vim.api.nvim_buf_get_lines(bufnr, row - 1, row, false)
    return parse.get_node(line[1])
end

M.get_node = function()
    local payload = get_payload()

    if string.sub(payload.dir, -1) ~= "/" then
        payload.absolute_path = payload.dir .. "/" .. payload.node
    else
        payload.absolute_path = payload.dir .. payload.node
    end

    if payload.extension ~= nil then
        payload.type = "file"
    else
        payload.type = "dir"
    end
    return payload
end


M.debug = function()
    vim.print(M.get_node())
end

-- error
M.create_under_cursor = function()
    local payload = get_payload()
    vim.opt_local.modifiable = true
    if payload.extension == nil then
        mapcheck_call(M.open)
    end
    mapcheck_call("<Plug>NetrwOpenFile")
    vim.opt_local.modifiable = false
end

M.split = function(mode)
    local node = M.get_node()
    local windows = vim.tbl_filter(function(id)
        return vim.api.nvim_win_get_config(id).relative == ""
    end, vim.api.nvim_tabpage_list_wins(0))
    if #windows > 0 then
        require("nvim-window").pick()
    else
        mode = "v"
    end
    vim.cmd(mode .. "split")
    vim.cmd("e " .. node.absolute_path)
end

M.toggle_hidden = "<Plug>NetrwHide_a"
M.close_preview = "<C-w>z"
M.close = ":Rexplore<cr>"
M.reload = "<Plug>NetrwRefresh"
M.open = "<Plug>NetrwLocalBrowseCheck"
M.server_edit = "<Plug>NetrwServerEdit"
M.prev = "<Plug>NetrwBrowseUpDir"

M.open_o = ":call <SNR>43_NetrwSplit(3)<CR>"
M.open_v = ":call <SNR>43_NetrwSplit(5)<CR>"

return M
