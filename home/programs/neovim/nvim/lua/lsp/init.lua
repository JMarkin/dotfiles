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
    local external_install = require("external_install")

    return {
        install = function(sync, update)
            external_install(bin_name, sync, update)
        end,
        setup = function()
            if vim.fn.executable(bin_name) then
                utils.setup_lsp(lsp_name, opts)
            else
                vim.notify(string.format("Not Executable %s, try install", bin_name), vim.log.levels.DEBUG)
            end
        end,
    }
end

local M = {}
M.lsps = {
    nginx_language_server = default_lsp("nginx-language-server", "nginx_language_server"),
    -- ["nil"] = default_lsp("nil", "nil_ls"),
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
    -- pylsp = default_lsp("python-lsp-server", "pylsp", {
    --     filetypes = { "python", "python.django", "django" },
    --     settings = {
    --         pylsp = {
    --             configurationSources = {},
    --             plugins = {
    --                 jedi_completion = {
    --                     include_function_objects = true,
    --                     include_params = true,
    --                 },
    --                 yapf = {
    --                     enabled = false,
    --                 },
    --                 pycodestyle = {
    --                     enabled = false,
    --                 },
    --                 flake8 = {
    --                     enabled = false,
    --                 },
    --                 autopep8 = {
    --                     enabled = false,
    --                 },
    --             },
    --         },
    --     },
    -- }),
    -- pyright = default_lsp("pyright", "pyright", {
    --     filetypes = { "python", "python.django", "django" },
    -- }),
    -- pylyzer = default_lsp("pylyzer", "pylyzer"),
    -- basedpyright = default_lsp("basedpyright", "basedpyright", {
    --     filetypes = { "python", "python.django", "django" },
    --     settings = {
    --         basedpyright = {
    --             disableOrganizeImports = true,
    --             -- typeCheckingMode = "off",
    --             analysis = {
    --                 diagnosticMode = "openFilesOnly",
    --             },
    --         },
    --     },
    -- }),
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
}

M.setup = function()
    for _, lsp in pairs(M.lsps) do
        lsp.setup()
    end
end

return M
