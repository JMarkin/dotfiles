return {
  {
    "altermo/ultimate-autopair.nvim",
    enabled = true,
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
  {
    "saghen/blink.pairs",
    enabled = false,
    dev = true,
    dir = vim.fn.stdpath("data") .. "/nix/blink.pairs",
    pin = true,
    opts = {
      mappings = {
        -- you can call require("blink.pairs.mappings").enable() and require("blink.pairs.mappings").disable() to enable/disable mappings at runtime
        enabled = true,
        -- see the defaults: https://github.com/Saghen/blink.pairs/blob/main/lua/blink/pairs/config/mappings.lua#L10
        pairs = {},
      },
      highlights = {
        enabled = true,
        groups = vim.g.rainbow_delimiters_highlight,
        matchparen = {
          enabled = true,
          group = "MatchParen",
        },
      },
      debug = false,
    },
  },
}
