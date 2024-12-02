local utils = require("lsp.utils")

return {
    install = function(sync, update)
    end,
    setup = function()
        vim.g.rustaceanvim = {
            tools = {},
            server = {
                on_attach = utils.on_attach,
                default_settings = {
                    ["rust-analyzer"] = {
                        checkOnSave = {
                            command = "clippy",
                        },
                        completion = {
                            autoimport = {
                                enable = false,
                            },
                        },
                        procMacro = {
                            enable = true,
                        },
                    },
                },
            },
        }
    end,
}
