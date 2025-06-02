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
  on_attach = function(client, buf)
    if vim.bo[buf].filetype == "lua" and vim.api.nvim_buf_get_name(buf):find("_spec") then
      vim.diagnostic.enable(false, { bufnr = buf })
      return
    end
  end,
}
