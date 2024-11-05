local utils = require("lsp.utils")
local external_install = require("external_install")

local M = {
    install = function(sync, update)
        external_install("lua-language-server", sync, update)
    end,
    setup = function()
        local opts = {
            before_init = require("neodev.lsp").before_init,
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
        utils.setup_lsp("lua_ls", opts)
    end,
}

return M
