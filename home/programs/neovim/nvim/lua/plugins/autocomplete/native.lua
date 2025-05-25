-- https://github.com/deathbeam/myplugins.nvim/blob/main/lua/myplugins

local group = vim.api.nvim_create_augroup("native-completion", { clear = true })
local funcs = require("funcs")

local config = {
  -- entry_mapper = function(vim_item, client)
  --     local entry = {
  --         source = {
  --             source = {
  --                 client = client,
  --             }
  --         }
  --     }
  --     entry.get_completion_item = function(self)
  --         return {
  --                 label = vim_item.abbr,
  --                 abbr = vim_item.abbr,
  --                 kind = vim_item.kind,
  --                 menu = vim_item.menu,
  --                 icase = vim_item.icase,
  --                 dup = vim_item.dup,
  --                 empty = vim_item.empty,
  --                 detail = vim_item.menu,
  --         }
  --     end
  --     local highlights_info = require("colorful-menu").cmp_highlights(entry)
  --     vim.print(highlights_info)
  --     if highlights_info ~= nil then
  --         vim_item.abbr_hl_group = highlights_info.highlights
  --         vim_item.abbr = highlights_info.text
  --     end
  --     return vim_item
  -- end,
  debounce_delay = 200,
}

local function complete_changed(args)
  local methods = vim.lsp.protocol.Methods
  if not string.find(vim.o.completeopt, "popup") then
    return
  end

  if not vim.v.event or not vim.v.event.completed_item then
    return
  end

  local cur_item = vim.v.event.completed_item
  local cur_info = vim.fn.complete_info()
  local selected = cur_info.selected

  funcs.debounce(config.debounce_delay, function()
    local completion_item = vim.tbl_get(cur_item or {}, "user_data", "nvim", "lsp", "completion_item")
    if not completion_item then
      return
    end

    -- vim.print(methods.completionItem_resolve)

    local _, cancel = vim.lsp.buf_request(
      args.buf,
      methods.completionItem_resolve,
      ---@param client vim.lsp.Client
      function(client, buf)
        if not client:supports_method(methods.completionItem_resolve, buf) then
          return
        end
        return completion_item
      end,
      vim.schedule_wrap(function(err, item)
        if err or not item then
          return
        end

        local docs = vim.tbl_get(item, "documentation", "value")
        if not docs or #docs == 0 then
          return
        end

        local wininfo = vim.api.nvim__complete_set(selected, { info = docs })
        if not wininfo.winid or not wininfo.bufnr then
          return
        end

        vim.api.nvim_win_set_config(wininfo.winid, {
          ---@diagnostic disable-next-line: assign-type-mismatch
          border = vim.o.winborder,
          focusable = false,
        })

        vim.treesitter.start(wininfo.bufnr, "markdown")
        vim.wo[wininfo.winid].conceallevel = 3
        vim.wo[wininfo.winid].concealcursor = "niv"
      end),
      function() end
    )

    return cancel
  end)
end

vim.api.nvim_create_autocmd("CompleteChanged", {
  group = group,
  desc = "Auto show LSP documentation",
  callback = complete_changed,
})

vim.api.nvim_create_autocmd("LspAttach", {
  group = group,
  desc = "Attach completion events",
  callback = function(args)
    if not vim.lsp.completion or not vim.lsp.completion.enable then
      return
    end

    local client = vim.lsp.get_client_by_id(args.data.client_id)
    if not client then
      return
    end

    if not client:supports_method(vim.lsp.protocol.Methods.textDocument_completion, args.buf) then
      return
    end

    if client.name == "minuet" then
      return
    end

    vim.lsp.completion.enable(true, client.id, args.buf, {
      autotrigger = true,
      convert = function(item)
        local doc = item.documentation or {}
        local info
        if vim.bo.filetype == "c" then
          info = ("%s%s\n \n%s"):format(item.detail or "", item.label, doc.value or "")
        end
        local entry = {
          abbr = item.label,
          kind = vim.lsp.protocol.CompletionItemKind[item.kind] or "Unknown",
          menu = item.detail or "",
          icase = 1,
          dup = 0,
          empty = 0,
          info = info and info:gsub("\n+%s*\n$", "") or nil,
        }

        if config.entry_mapper then
          return config.entry_mapper(entry, client)
        end

        return entry
      end,
    })

  end,
})

-- cmdcompletion
local function cmdcmp()
  if vim.fn.has("nvim-0.11.0") == 0 then
    return
  end

  local term = vim.api.nvim_replace_termcodes("<C-@>", true, true, true)

  vim.cmd([[set wildcharm=<C-@>]])
  vim.opt.wildmenu = true
  vim.opt.wildmode = "noselect:lastused,full"

  vim.keymap.set("c", "<Up>", "<End><C-U><Up>", { silent = true })
  vim.keymap.set("c", "<Down>", "<End><C-U><Down>", { silent = true })

  vim.api.nvim_create_autocmd("CmdlineChanged", {
    group = group,
    desc = "Auto show command line completion",
    pattern = ":",
    callback = function()
      local cmdline = vim.fn.getcmdline()
      local curpos = vim.fn.getcmdpos()
      local last_char = cmdline:sub(curpos - 1, curpos - 1)

      if
        curpos == #cmdline + 1
        and vim.fn.pumvisible() == 0
        and last_char:match("[%w%/%:- ]")
        and not cmdline:match("^%d+$")
      then
        vim.api.nvim_feedkeys(term, "ti", false)
        vim.opt.eventignore:append("CmdlineChanged")
        vim.schedule(function()
          vim.fn.setcmdline(vim.fn.substitute(vim.fn.getcmdline(), "\\%x00", "", "g"))
          vim.opt.eventignore:remove("CmdlineChanged")
        end)
      end
    end,
  })
end

-- vim.api.nvim_create_autocmd({ "CmdlineEnter" }, {
--     once = true,
--     callback = cmdcmp,
-- })
