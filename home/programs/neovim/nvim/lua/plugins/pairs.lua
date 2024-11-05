return {
    -- {
    --     "echasnovski/mini.pairs",
    --     enabled = false,
    --     event = { "InsertEnter", "CmdwinEnter" },
    --     opts = {
    --         modes = { insert = true, command = true, terminal = false },
    --         -- skip autopair when next character is one of these
    --         skip_next = [=[[%w%%%'%[%"%.%`%$]]=],
    --         -- skip autopair when the cursor is inside these treesitter nodes
    --         skip_ts = { "string" },
    --         -- skip autopair when next character is closing pair
    --         -- and there are more closing pairs than opening pairs
    --         skip_unbalanced = true,
    --         -- better deal with markdown code blocks
    --         markdown = true,
    --     },
    --     keys = {
    --         {
    --             "<leader>up",
    --             function()
    --                 vim.g.minipairs_disable = not vim.g.minipairs_disable
    --                 if vim.g.minipairs_disable then
    --                     vim.notify("Disabled auto pairs")
    --                 else
    --                     vim.notify("Enabled auto pairs")
    --                 end
    --             end,
    --             desc = "Toggle Auto Pairs",
    --         },
    --     },
    -- },
    {
        "ZhiyuanLck/smart-pairs",
        event = "InsertEnter",
        config = function()
            require("pairs"):setup({
                enter = {
                    enable_mapping = false,
                },
            })
            -- local cmp = require("cmp")
            -- local kind = cmp.lsp.CompletionItemKind
            -- cmp.event:on("confirm_done", function(event)
            --     local item = event.entry:get_completion_item()
            --     local parensDisabled = item.data and item.data.funcParensDisabled or false
            --     if not parensDisabled and (item.kind == kind.Method or item.kind == kind.Function) then
            --         require("pairs.bracket").type_left("(")
            --     end
            -- end)
        end,
    },
}
