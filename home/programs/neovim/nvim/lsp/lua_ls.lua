return {
  settings = {
    Lua = {
      telemetry = {
        enable = false,
      },
      hint = {
        enable = true,
      },
      runtime = {
        version = "LuaJIT",
      },
      diagnostics = {
        globals = {
          "vim",
        },
      },
      completion = {
        callSnippet = "Replace",
      },
      workspace = {
        checkThirdParty = false,
        library = {
          [vim.fn.expand("$VIMRUNTIME/lua")] = true,
          [vim.fn.expand("$VIM/lazy")] = true,
          [vim.fn.expand("$VIMRUNTIME")] = true,
          [vim.fn.expand("~/.config/nvim/lua")] = true,
        },
      },
    },
  },
}
