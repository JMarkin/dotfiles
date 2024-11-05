local utils = require("lsp.utils")
local external_install = require("external_install")

return {
    install = function(sync, update)
        external_install("vue-language-server", sync, update)
    end,
    setup = function()
        local setup_lsp = utils.setup_lsp

        local lspconfig_configs = require("lspconfig.configs")
        local lspconfig_util = require("lspconfig.util")
        local function on_new_config(new_config, new_root_dir)
            local function get_typescript_server_path(root_dir)
                local project_root = lspconfig_util.find_node_modules_ancestor(root_dir)
                return project_root
                        and (lspconfig_util.path.join(
                            project_root,
                            "node_modules",
                            "typescript",
                            "lib",
                            "tsserverlibrary.js"
                        ))
                    or ""
            end

            if
                new_config.init_options
                and new_config.init_options.typescript
                and new_config.init_options.typescript.serverPath == ""
            then
                new_config.init_options.typescript.serverPath = get_typescript_server_path(new_root_dir)
            end
        end

        local volar_cmd = { "vue-language-server", "--stdio" }
        local volar_root_dir = lspconfig_util.root_pattern("package.json")

        local filetypes = { "vue" }

        -- If you want to use Volar's Take Over Mode (if you know, you know)
        if vim.g.vue_takeover then
            filetypes = { "typescript", "javascript", "javascriptreact", "typescriptreact", "vue", "json" }
        end

        lspconfig_configs.volar_api = {
            default_config = {
                cmd = volar_cmd,
                root_dir = volar_root_dir,
                on_new_config = on_new_config,
                filetypes = filetypes,
                init_options = {
                    typescript = {
                        serverPath = "",
                    },
                    languageFeatures = {
                        implementation = true, -- new in @volar/vue-language-server v0.33
                        references = true,
                        definition = true,
                        typeDefinition = true,
                        callHierarchy = true,
                        hover = true,
                        rename = true,
                        renameFileRefactoring = true,
                        signatureHelp = true,
                        codeAction = true,
                        workspaceSymbol = true,
                        completion = {
                            defaultTagNameCase = "both",
                            defaultAttrNameCase = "kebabCase",
                            getDocumentNameCasesRequest = false,
                            getDocumentSelectionRequest = false,
                        },
                    },
                },
            },
        }
        setup_lsp("volar_api", {})

        lspconfig_configs.volar_doc = {
            default_config = {
                cmd = volar_cmd,
                root_dir = volar_root_dir,
                on_new_config = on_new_config,
                filetypes = filetypes,
                init_options = {
                    typescript = {
                        serverPath = "",
                    },
                    languageFeatures = {
                        implementation = true, -- new in @volar/vue-language-server v0.33
                        documentHighlight = true,
                        documentLink = true,
                        codeLens = { showReferencesNotification = true },
                        -- not supported - https://github.com/neovim/neovim/pull/15723
                        semanticTokens = false,
                        diagnostics = true,
                        schemaRequestService = true,
                    },
                },
            },
        }
        setup_lsp("volar_doc", {})

        lspconfig_configs.volar_html = {
            default_config = {
                cmd = volar_cmd,
                root_dir = volar_root_dir,
                on_new_config = on_new_config,
                filetypes = filetypes,
                init_options = {
                    typescript = {
                        serverPath = "",
                    },
                    documentFeatures = {
                        selectionRange = true,
                        foldingRange = true,
                        linkedEditingRange = true,
                        documentSymbol = true,
                        -- not supported - https://github.com/neovim/neovim/pull/13654
                        documentColor = false,
                        documentFormatting = {
                            defaultPrintWidth = 100,
                        },
                    },
                },
            },
        }
        setup_lsp("volar_html", {})
    end,
}
