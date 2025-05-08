return {
  {
    "echasnovski/mini.pairs",
    event = { "InsertEnter", "CmdlineEnter" },
    enabled = false,
    opts = {
      modes = { insert = true, command = true, terminal = false },
      -- skip autopair when next character is one of these
      skip_next = [=[[%w%%%'%[%"%.%`%$]]=],
      -- skip autopair when the cursor is inside these treesitter nodes
      skip_ts = { "string" },
      -- skip autopair when next character is closing pair
      -- and there are more closing pairs than opening pairs
      skip_unbalanced = true,
      -- better deal with markdown code blocks
      markdown = true,
    },
    init = function()
      vim.api.nvim_create_autocmd("User", {
        pattern = "VeryLazy",
        callback = function()
          Snacks.toggle({
            name = "Auto Pairs",
            get = function()
              vim.g.minipairs_disable = not vim.g.minipairs_disable
              return vim.g.minipairs_disable
            end,
            set = function(state)
              vim.g.minipairs_disable = not state
            end,
          }):map("<leader>up")
        end,
      })
    end,
  },
  {
    "altermo/ultimate-autopair.nvim",
    event = { "InsertEnter", "CmdlineEnter" },
    branch = "v0.6", --recommended as each new version will have breaking changes
    opts = {
      --Config goes here
    },
    init = function()
      vim.api.nvim_create_autocmd("User", {
        pattern = "VeryLazy",
        callback = function()
          Snacks.toggle({
            name = "Auto Pairs",
            get = function()
              return require("ultimate-autopair").isenabled()
            end,
            set = function(state)
              require("ultimate-autopair").toggle()
            end,
          }):map("<leader>up")
        end,
      })
    end,
  },
  -- {
  --     "ZhiyuanLck/smart-pairs",
  --     event = "InsertEnter",
  --     enabled = true,
  --     config = function()
  --         require("pairs"):setup({
  --             enter = {
  --                 enable_mapping = false,
  --             },
  --         })
  --         -- local cmp = require("cmp")
  --         -- local kind = cmp.lsp.CompletionItemKind
  --         -- cmp.event:on("confirm_done", function(event)
  --         --     local item = event.entry:get_completion_item()
  --         --     local parensDisabled = item.data and item.data.funcParensDisabled or false
  --         --     if not parensDisabled and (item.kind == kind.Method or item.kind == kind.Function) then
  --         --         require("pairs.bracket").type_left("(")
  --         --     end
  --         -- end)
  --     end,
  -- },
}
