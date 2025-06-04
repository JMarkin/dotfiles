return {
  {
    "saghen/blink.pairs",
    enabled = true,
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
