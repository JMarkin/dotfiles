--
-- https://github.com/neovim/nvim-lspconfig/blob/master/doc/configs.md

if vim.env.NVIM_MINI ~= nil then
    return {}
end

local default_lsp = function(bin_name, lsp_name, opts)
    if not opts then
        opts = {}
    end
    local utils = require("lsp.utils")

    return {
        setup = function()
            if vim.fn.executable(bin_name) == 1 then
                utils.setup_lsp(lsp_name, opts)
            else
                vim.notify(string.format("Not Executable %s skip", bin_name), vim.log.levels.DEBUG)
            end
        end,
    }
end

local M = {}
M.lsps = {
    nginx_language_server = default_lsp("nginx-language-server", "nginx_language_server"),
    ["nil"] = default_lsp("nil", "nil_ls"),
    lua_ls = require("lsp.lua_ls"),
    rust_analyzer = require("lsp.rust_analyzer"),
    bashls = default_lsp("bash-language-server", "bashls"),
    vimls = default_lsp("vim-language-server", "vimls"),
    html = default_lsp("vscode-html-language-server", "html", {
        filetypes = { "html", "jinja" },
    }),
    cssls = default_lsp("vscode-css-language-server", "cssls"),
    jedi_language_server = default_lsp("jedi-language-server", "jedi_language_server"),
    ruff = default_lsp("ruff", "ruff"),
    -- pylyzer = default_lsp("pylyzer", "pylyzer"),
    basedpyright = default_lsp("basedpyright", "basedpyright", {
        filetypes = { "python", "python.django", "django" },
        settings = {
            basedpyright = {
                disableOrganizeImports = true,
                analysis = {
                    typeCheckingMode = "off",
                    diagnosticMode = "openFilesOnly",
                },
            },
        },
    }),
    taplo = default_lsp("taplo", "taplo"),
    tsserver = default_lsp("typescript-language-server", "ts_ls"),
    neocmakelsp = default_lsp("neocmakelsp", "neocmake"),
    clangd = require("lsp.clangd"),
    volar = require("lsp.volar"),
    docker_compose_language_service = default_lsp("docker-compose-langserver", "docker_compose_language_service"),
    dockerls = default_lsp("docker-langserver", "dockerls"),
    yamlls = default_lsp("yaml-language-server", "yamlls", {
        settings = {
            yaml = {
                schemaStore = {
                    enable = false,
                },
                schemas = require("schemastore").yaml.schemas(),
            },
            redhat = {
                telemetry = {
                    enabled = false,
                },
            },
        },
    }),
    jsonls = default_lsp("vscode-json-language-server", "jsonls", {
        settings = {
            json = {
                schemas = require("schemastore").json.schemas(),
                validate = { enable = true },
            },
        },
    }),
    -- sourcekit = {
    --     install = function(_, _) end,
    --     setup = function()
    --         require("lsp.utils").setup_lsp("sourcekit", {})
    --     end,
    -- },
    biome = default_lsp("biome", "biome"),
    jinja_lsp = default_lsp("jinja-lsp", "jinja_lsp"),
    gopls = require("lsp.gopls"),
    golangci_lint_ls = default_lsp("golangci-lint-langserver", "golangci_lint_ls"),
    vacuum = default_lsp("vacuum", "vacuum"),
}

M.setup = function()
    for _, lsp in pairs(M.lsps) do
        lsp.setup()
    end
end

vim.lsp.handlers['workspace/diagnostic/refresh'] = function(_, _, ctx)
    local ns = vim.lsp.diagnostic.get_namespace(ctx.client_id)
    local bufnr = vim.api.nvim_get_current_buf()
    vim.diagnostic.reset(ns, bufnr)
    return true
end

return M
