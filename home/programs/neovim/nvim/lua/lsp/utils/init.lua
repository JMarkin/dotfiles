local is_large_file = require("largefiles").is_large_file
local methods = vim.lsp.protocol.Methods
local M = {}

local diag_opts = {
    focusable = false,
    close_events = { "BufLeave", "CursorMoved", "InsertEnter", "FocusLost" },
    border = "rounded",
    source = "always",
    prefix = " ",
    scope = "cursor",
}

local keys = {
    {
        "<leader>sd",
        function()
            require("fzf-lua").lsp_definitions({ multiprocess = true })
        end,
        { desc = "Search: Definitions" },
    },
    {
        "<leader>sS",
        function()
            require("fzf-lua").lsp_live_workspace_symbols({ multiprocess = true })
        end,
        { desc = "Search: Symbols" },
    },
    {
        "grr",
        function()
            require("fzf-lua").lsp_references({ multiprocess = true, ignore_current_line = true })
        end,
        { silent = true, desc = "Search: references" },
    },
    {
        "gf",
        "<cmd>Lspsaga peek_definition<cr>",
        { desc = "GoTo: definition float" },
    },
    {
        "gd",
        vim.lsp.buf.definition,
        { desc = "GoTo: definition" },
    },
    {
        "gD",
        vim.lsp.buf.declaration,
        { desc = "GoTo: declarations" },
    },
    {
        "gh",
        "<cmd>Lspsaga finder<CR>",
        { desc = "Lsp: Finder" },
    },
    {

        "K",
        "<cmd>Lspsaga hover_doc<CR>",
        { silent = true, desc = "Lang: hover doc" },
    },
    {

        "<leader>le",
        "<cmd>Lspsaga show_buf_diagnostics<CR>",
        { silent = true, desc = "Lang: show buf disagnostic" },
    },
    {

        "<leader>lE",
        "<cmd>Lspsaga show_workspace_diagnostics<CR>",
        { silent = true, desc = "Lang: show workspace disagnostic" },
    },
    {
        "grn",
        "<cmd>Lspsaga rename<CR>",
        { silent = true, desc = "Lang: rename" },
    },
    {

        "grN",
        "<cmd>Lspsaga rename ++project<CR>",
        { silent = true, desc = "Lang: rename project" },
    },
    -- {
    --     "<space>T",
    --     ":Vista nvim_lsp<cr>",
    --     { desc = "Tagbar", silent = true },
    -- },
}

--- https://github.com/neovim/nvim-lspconfig/blob/f4619ab31fc4676001ea05ae8200846e6e7700c7/plugin/lspconfig.lua#L123
---@param client vim.lsp.Client
---@param bufnr integer

--- Sets up LSP keymaps and autocommands for the given buffer.
---@param client vim.lsp.Client
---@param bufnr integer
local function on_attach(client, bufnr)
    if is_large_file(bufnr, true) then
        vim.schedule(function()
            vim.lsp.buf_detach_client(bufnr, client.id)
        end)
        vim.bo[bufnr].tagfunc = nil
        return 0
    end

    for _, keymap in ipairs(keys) do
        keymap[3].buffer = bufnr
        vim.keymap.set("n", table.unpack(keymap))
    end

    if not client.supports_method(methods.textDocument_hover) then
        client.server_capabilities.hoverProvider = false
    end

    if client.supports_method(methods.textDocument_codeAction) then
        vim.keymap.set({ "n", "v" }, "gra", function()
            require("fzf-lua").lsp_code_actions({
                winopts = {
                    relative = "cursor",
                    width = 0.6,
                    height = 0.6,
                    row = 1,
                    preview = { vertical = "up:70%" },
                },
            })
        end, { desc = "Code actions" })
    end

    if client.supports_method(methods.textDocument_inlayHint) then
        local inlay_hints_group = vim.api.nvim_create_augroup("toggle_inlay_hints", { clear = false })
        vim.keymap.set({ "n" }, "<leader>li", function()
            local enabled = vim.lsp.inlay_hint.is_enabled({ bufnr = bufnr })

            if not enabled then
                vim.api.nvim_create_autocmd("InsertEnter", {
                    group = inlay_hints_group,
                    desc = "Enable inlay hints",
                    buffer = bufnr,
                    callback = function()
                        vim.lsp.inlay_hint.enable(false, { bufnr = bufnr })
                    end,
                })
                vim.api.nvim_create_autocmd("InsertLeave", {
                    group = inlay_hints_group,
                    desc = "Disable inlay hints",
                    buffer = bufnr,
                    callback = function()
                        vim.lsp.inlay_hint.enable(true, { bufnr = bufnr })
                    end,
                })
            else
                vim.api.nvim_clear_autocmds({
                    buffer = bufnr,
                    group = inlay_hints_group,
                })
            end
            vim.lsp.inlay_hint.enable(not enabled, { bufnr = bufnr })
        end, { buffer = bufnr, silent = true, desc = "Toggle Inlay hint" })
    end

    -- vim.bo[bufnr].omnifunc = "v:lua.vim.lsp.omnifunc"

    return 1
end

M.on_attach = on_attach

local capabilities = vim.lsp.protocol.make_client_capabilities()

capabilities.textDocument = {
    foldingRange = {
        dynamicRegistration = false,
        lineFoldingOnly = true,
    },
    completion = {
        dynamicRegistration = false,
        completionItem = {
            snippetSupport = true,
            commitCharactersSupport = true,
            deprecatedSupport = true,
            preselectSupport = true,
            tagSupport = {
                valueSet = {
                    1, -- Deprecated
                },
            },
            insertReplaceSupport = true,
            resolveSupport = {
                properties = {
                    "documentation",
                    "detail",
                    "additionalTextEdits",
                    "sortText",
                    "filterText",
                    "insertText",
                    "textEdit",
                    "insertTextFormat",
                    "insertTextMode",
                },
            },
            insertTextModeSupport = {
                valueSet = {
                    1, -- asIs
                    2, -- adjustIndentation
                },
            },
            labelDetailsSupport = true,
        },
        contextSupport = true,
        insertTextMode = 1,
        completionList = {
            itemDefaults = {
                "commitCharacters",
                "editRange",
                "insertTextFormat",
                "insertTextMode",
                "data",
            },
        },
    },
}

M.capabilities = capabilities

local function setup_lsp(lsp_name, opts)
    local lsp_util = require("lspconfig.util")

    local _opts = {
        root_dir = lsp_util.root_pattern(table.unpack(vim.g.root_pattern)),
        capabilities = capabilities,
        on_attach = on_attach,
        autostart = vim.g.lsp_autostart,
    }
    opts = vim.tbl_extend("force", opts, _opts)

    local lsp = require("lspconfig")
    local conf = lsp[lsp_name]
    conf.setup(opts)

    -- local try_add = conf.manager.try_add
    -- conf.manager.try_add = function(self, bufnr, project_root)
    --     if is_large_file(bufnr, true) then
    --         vim.notify("disable lsp large buffer", vim.log.levels.ERROR)
    --         vim.bo[bufnr].tagfunc = nil
    --         vim.bo[bufnr].omnifunc = "syntaxcomplete#Complete"
    --         return
    --     end
    --
    --     return try_add(self, bufnr, project_root)
    -- end
end

M.setup_lsp = setup_lsp

return M
