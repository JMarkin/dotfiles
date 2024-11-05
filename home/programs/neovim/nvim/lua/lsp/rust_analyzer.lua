local utils = require("lsp.utils")
local external_install = require("external_install")

return {
    install = function(sync, update)
        external_install("rust-analyzer", sync, update)
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

        vim.api.nvim_create_autocmd("FileType", {
            once = true,
            callback = function(_)
                require("rustaceanvim")
            end,
        })
    end,
}
