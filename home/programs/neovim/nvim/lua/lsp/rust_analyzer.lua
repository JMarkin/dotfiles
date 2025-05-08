local utils = require("lsp.utils")

return {
  install = function(sync, update) end,
  setup = function()
    vim.g.rustaceanvim = {
      tools = {},
      server = {
        on_attach = utils.on_attach,
        default_settings = {
          ["rust-analyzer"] = {
            checkOnSave = true,
            completion = {
              autoimport = {
                enable = false,
              },
            },
            procMacro = {
              enable = true,
            },
            files = {
              excludeDirs = {
                ".direnv",
                "_build",
                ".dart_tool",
                ".flatpak-builder",
                ".git",
                ".gitlab",
                ".gitlab-ci",
                ".gradle",
                ".idea",
                ".next",
                ".project",
                ".scannerwork",
                ".settings",
                ".venv",
                "archetype-resources",
                "bin",
                "hooks",
                "node_modules",
                "po",
                "screenshots",
                "target",
              },
            },
          },
        },
      },
    }
  end,
}
