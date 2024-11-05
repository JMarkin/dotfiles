local autocmd = vim.api.nvim_create_autocmd
local augroup = vim.api.nvim_create_augroup
local is_not_mini = require("funcs").is_not_mini

local enabled = true

TAGS_SOURCE = {
    name = "tags",
    option = {
        -- this is the default options, change them if you want.
        -- Delayed time after user input, in milliseconds.
        complete_defer = 100,
        -- Max items when searching `taglist`.
        max_items = 10,
        -- The number of characters that need to be typed to trigger
        -- auto-completion.
        keyword_length = 3,
        -- Use exact word match when searching `taglist`, for better searching
        -- performance.
        exact_match = false,
        -- Prioritize searching result for current buffer.
        current_buffer_only = false,
    },
}

OMNI_SOURCE = {
    name = "omni",
    option = {
        disable_omnifuncs = { "v:lua.vim.lsp.omnifunc" },
    },
}
LUASNIP_SOURCE = { name = "luasnip", keyword_length = 1, max_item_count = 5 }
LUASNIP_CHOIDCE_SOURCE = { name = "luasnip_choice" }
VIMDADBOD_SOURCE = {
    name = "vim-dadbod-completion",
    filetype = { "sql", "mssql", "plsql" },
}
DIAG_CODES_SOURCE = { name = "diag-codes", in_comment = true }
LSP_SOURCE = { name = "nvim_lsp", max_item_count = 30 }
RG_SOURCE = {
    name = "rg",
    keyword_length = 2,
    max_item_count = 5,
    option = { additional_arguments = "--max-depth 4" },
}
NVIM_SOURCE = { name = "nvim_lua" }
FILE_SOURCE = { name = "async_path" }

local mini_sources = {
    TAGS_SOURCE,
    OMNI_SOURCE,
}

local default_sources = {
    OMNI_SOURCE,
    VIMDADBOD_SOURCE,
    TAGS_SOURCE,
    RG_SOURCE,
    LUASNIP_SOURCE,
}

local lsp_sources = {
    DIAG_CODES_SOURCE,
    LSP_SOURCE,
    VIMDADBOD_SOURCE,
    TAGS_SOURCE,
    RG_SOURCE,
    LUASNIP_SOURCE,
}

local nvim_sources = {
    NVIM_SOURCE,
    DIAG_CODES_SOURCE,
    LSP_SOURCE,
    RG_SOURCE,
}

local default_comparators = function(compare)
    return {
        require("plugins.autocomplete._cmp_tools").put_down_snippet,
        compare.offset,
        compare.exact,
        compare.score,
        compare.recently_used,
        compare.locality,
        require("plugins.autocomplete._cmp_tools").lspkind_comparator(),
        compare.sort_text,
        compare.length,
        compare.order,
    }
end

local rust_comparators = function(compare)
    return {
        require("plugins.autocomplete._cmp_tools").put_down_snippet,
        -- deprioritize `.box`, `.mut`, etc.
        require("plugins.autocomplete._cmp_tools").deprioritize_postfix,
        -- deprioritize `Borrow::borrow` and `BorrowMut::borrow_mut`
        require("plugins.autocomplete._cmp_tools").deprioritize_borrow,
        -- deprioritize `Deref::deref` and `DerefMut::deref_mut`
        require("plugins.autocomplete._cmp_tools").deprioritize_deref,
        -- deprioritize `Into::into`, `Clone::clone`, etc.
        require("plugins.autocomplete._cmp_tools").deprioritize_common_traits,
        compare.offset,
        compare.exact,
        compare.score,
        compare.recently_used,
        require("plugins.autocomplete._cmp_tools").lspkind_comparator(),
        compare.locality,
        compare.sort_text,
        compare.length,
        compare.order,
    }
end

local python_comparators = function(compare)
    return {
        require("plugins.autocomplete._cmp_tools").under,
        require("plugins.autocomplete._cmp_tools").put_down_snippet,
        compare.offset,
        compare.exact,
        compare.score,
        compare.recently_used,
        compare.locality,
        require("plugins.autocomplete._cmp_tools").lspkind_comparator(),
        compare.sort_text,
        compare.length,
        compare.order,
    }
end

local clang_comparators = function(compare)
    return {
        require("plugins.autocomplete._cmp_tools").put_down_snippet,
        require("plugins.autocomplete._cmp_tools").lspkind_comparator(),
        compare.offset,
        compare.exact,
        compare.score,
        compare.recently_used,
        require("clangd_extensions.cmp_scores"),
        compare.locality,
        compare.kind,
        compare.sort_text,
        compare.length,
        compare.order,
    }
end

---Hack: `nvim_lsp` and `nvim_lsp_signature_help` source still use
---deprecated `vim.lsp.buf_get_clients()`, which is slower due to
---the deprecation and version check in that function. Overwrite
---it using `vim.lsp.get_clients()` to improve performance.
---@diagnostic disable-next-line: duplicate-set-field
function vim.lsp.buf_get_clients(bufnr)
    return vim.lsp.get_clients({ buffer = bufnr })
end

---@type string?
local last_key

vim.on_key(function(k)
    last_key = k
end)

local cmp_config = function(sources, buffer, comparators)
    comparators = comparators or default_comparators
    local luasnip_enabled, luasnip = pcall(require, "luasnip")

    local neogen_enabled, neogen = pcall(require, "neogen")

    local cmp = require("cmp")
    local compare = require("cmp.config.compare")

    local move_down = cmp.mapping(function(fallback)
        if cmp.visible() then
            cmp.select_next_item()
        elseif luasnip_enabled and luasnip.expand_or_locally_jumpable() then
            luasnip.expand_or_jump()
        elseif neogen_enabled and neogen.jumpable() then
            neogen.jump_next()
        else
            fallback()
        end
    end, { "i", "s" })

    local move_up = cmp.mapping(function(fallback)
        if cmp.visible() then
            cmp.select_prev_item()
        elseif luasnip and luasnip.in_snippet() and luasnip.jumpable(-1) then
            luasnip.jump(-1)
        elseif neogen and neogen.jumpable(true) then
            neogen.jump_prev()
        else
            fallback()
        end
    end, { "i", "s" })

    local preselect = cmp.PreselectMode.None

    local setup = cmp.setup

    if buffer then
        setup = cmp.setup.buffer
    else
        cmp.setup.filetype({ "dap-repl", "dapui_watches", "dapui_hover" }, {
            sources = {
                { name = "dap" },
            },
        })
    end

    local has_words_after = require("plugins.autocomplete._cmp_tools").has_words_after
    local menu_map = require("plugins.autocomplete._cmp_tools").menu_map

    vim.api.nvim_set_hl(0, "CmpGhostText", { link = "Comment", default = true })

    setup({
        performance = {
            debounce = 0,
            throttle = 0,
            fetching_timeout = 5,
            confirm_resolve_timeout = 80,
            -- async_budget = 1,
            max_view_entries = 50,
        },
        enabled = function()
            local disabled = false
            ---@diagnostic disable-next-line: deprecated
            disabled = disabled or (vim.api.nvim_buf_get_option(0, "buftype") == "prompt")
            disabled = disabled or (vim.fn.reg_recording() ~= "")
            disabled = disabled or (vim.fn.reg_executing() ~= "")
            if is_not_mini() then
                disabled = disabled or require("cmp_dap").is_dap_buffer()
            end
            return not disabled
        end,
        preselect = preselect,
        sorting = {
            priority_weight = 2,
            comparators = comparators(compare),
        },
        view = {
            entries = { name = "custom" },
            docs = {
                auto_open = true,
            },
        },
        ghost_text = {
            hl_group = "CmpGhostText",
        },
        snippet = {
            expand = is_not_mini() and function(args)
                luasnip.lsp_expand(args.body) -- For `luasnip` users.
            end,
        },
        mapping = {
            ["<C-k>"] = cmp.mapping(function()
                if cmp.visible_docs() then
                    cmp.close_docs()
                else
                    cmp.open_docs()
                end
            end),
            ["<C-e>"] = cmp.mapping.scroll_docs(-4),
            ["<C-d>"] = cmp.mapping.scroll_docs(4),
            ["<C-Space>"] = cmp.mapping.complete(),
            ["<c-x><c-f>"] = cmp.mapping.complete({
                config = {
                    sources = {
                        FILE_SOURCE,
                    },
                },
            }),
            ["<c-f>"] = cmp.mapping.complete({
                config = {
                    sources = {
                        FILE_SOURCE,
                    },
                },
            }),
            ["<c-x><c-]>"] = cmp.mapping.complete({
                config = {
                    sources = {
                        TAGS_SOURCE,
                    },
                },
            }),
            ["<c-]>"] = cmp.mapping.complete({
                config = {
                    sources = {
                        TAGS_SOURCE,
                    },
                },
            }),
            ["<C-a>"] = cmp.mapping.abort(),
            ["<CR>"] = cmp.mapping({
                i = function(fallback)
                    if cmp.visible() and cmp.get_active_entry() or vim.fn.pumvisible() > 0 then
                        if not cmp.confirm({ behavior = cmp.ConfirmBehavior.Replace, select = false }) then
                            require("pairs.enter").type()
                        end
                    else
                        require("pairs.enter").type()
                    end
                end,
                s = cmp.mapping.confirm({ select = true }),
            }),
            ["<Tab>"] = move_down,
            ["<S-Tab>"] = move_up,
            -- ["<C-]>"] = cmp.mapping(
            --     cmp.mapping.complete({
            --         config = {
            --             sources = cmp.config.sources({
            --                 { name = "cmp_ai" },
            --             }),
            --         },
            --     }),
            --     { "i" }
            -- ),
        },
        sources = sources,
        formatting = {
            fields = { "abbr", "kind", "menu" },
            format = function(entry, vim_item)
                if entry.source.name == "cmp_ai" then
                    vim_item.menu = menu_map[entry.source.name]
                    local detail = (entry.completion_item.labelDetails or {}).detail
                    vim_item.kind = ""
                    if detail and detail:find(".*%%.*") then
                        vim_item.kind = vim_item.kind .. " " .. detail
                    end

                    if (entry.completion_item.data or {}).multiline then
                        vim_item.kind = vim_item.kind .. " " .. "[ML]"
                    end
                    vim_item.abbr = string.sub(vim_item.abbr, 1, 80)
                    return vim_item
                end

                if not is_not_mini() then
                    return vim_item
                end
                local resp = require("lspkind").cmp_format({ mode = "symbol_text", maxwidth = 50, menu = menu_map })(
                    entry,
                    vim_item
                )
                return resp
            end,
        },
        window = {
            completion = {
                -- winhighlight = "Normal:Pmenu,FloatBorder:Pmenu,Search:None",
                col_offset = 1,
                side_padding = 0,
            },
            documentation = {
                max_width = 80,
                max_height = 20,
                border = "solid",
            },
        },
    })
end

local function cmp_cmdline(is_large)
    local cmp = require("cmp")

    if is_large then
        cmp.setup.cmdline({ "/", "?" }, { enabled = false })
    else
        cmp.setup.cmdline({ "/", "?" }, {
            mapping = cmp.mapping.preset.cmdline(),
            sources = {
                { name = "buffer" },
                { name = "cmdline_history", max_item_count = 2 },
            },
            performance = {
                max_view_entries = 10,
            },
            view = {
                entries = { name = "wildmenu", separator = " | " },
            },
        })
    end

    cmp.setup.cmdline(":", {
        mapping = cmp.mapping.preset.cmdline(),
        sources = cmp.config.sources({
            { name = "cmdline", option = {
                ignore_cmds = { "Man" },
            } },
            { name = "cmdline_history", max_item_count = 2 },
        }),
    })
end

if enabled then
    local gr = augroup("cmp", { clear = true })

    autocmd("FileType", {
        group = gr,
        pattern = "python",
        callback = function(opts)
            vim.b.comparators = python_comparators
        end,
    })

    autocmd("FileType", {
        group = gr,
        pattern = "rust",
        callback = function(opts)
            vim.b.comparators = rust_comparators
        end,
    })

    autocmd("FileType", {
        group = gr,
        pattern = { "c", "cpp", "h" },
        callback = function(opts)
            vim.b.comparators = clang_comparators
        end,
    })

    autocmd("LspAttach", {
        group = gr,
        pattern = "*",
        callback = function(opts)
            cmp_config(lsp_sources, opts.buf, vim.b.comparators)
        end,
    })

    -- autocmd("FileType", {
    --     group = gr,
    --     pattern = { "lua" },
    --     callback = function(opts)
    --         local current_file = vim.fn.expand("%:p")
    --
    --         local base_vimruntime_dir = vim.api.nvim_call_function("finddir", "vimruntime")
    --
    --         if string.find(base_vimruntime_dir, current_file) then
    --             cmp_config(nvim_sources, opts.buf, vim.b.comparators)
    --         end
    --     end,
    -- })

    autocmd("User", {
        pattern = "LargeFile",
        group = gr,
        callback = function(opts)
            cmp_config(default_sources, opts.buf)
        end,
    })
end

return {
    {
        enabled = enabled,
        "L3MON4D3/LuaSnip",
        build = "make install_jsregexp",
        ft = "snippets",
        dependencies = {
            "rafamadriz/friendly-snippets",
        },
        cond = is_not_mini,
        lazy = true,
        config = function(_, opts)
            if opts then
                require("luasnip").config.setup(opts)
            end
            local luasnip = require("luasnip")

            luasnip.config.set_config({
                region_check_events = "InsertEnter",
                delete_check_events = "TextChanged,InsertLeave",
            })
            vim.tbl_map(function(type)
                require("luasnip.loaders.from_" .. type).lazy_load()
            end, { "vscode", "snipmate", "lua" })

            -- -- friendly-snippets - enable standardized comments snippets
            require("luasnip").filetype_extend("typescript", { "tsdoc" })
            require("luasnip").filetype_extend("javascript", { "jsdoc" })
            require("luasnip").filetype_extend("lua", { "luadoc" })
            require("luasnip").filetype_extend("python", { "pydoc" })
            require("luasnip").filetype_extend("rust", { "rustdoc" })
            require("luasnip").filetype_extend("cs", { "csharpdoc" })
            require("luasnip").filetype_extend("java", { "javadoc" })
            require("luasnip").filetype_extend("c", { "cdoc" })
            require("luasnip").filetype_extend("cpp", { "cppdoc" })
            require("luasnip").filetype_extend("php", { "phpdoc" })
            require("luasnip").filetype_extend("kotlin", { "kdoc" })
            require("luasnip").filetype_extend("ruby", { "rdoc" })
            require("luasnip").filetype_extend("sh", { "shelldoc" })
        end,
    },
    {
        -- "JMarkin/nvim-cmp",
        -- branch = "perf-up",
        -- dev = true,
        -- "hrsh7th/nvim-cmp",
        "iguanacucumber/magazine.nvim",
        enabled = enabled,
        lazy = true,
        event = { "InsertEnter", "CmdlineEnter" },
        -- dev = true,
        dependencies = {
            { "lukas-reineke/cmp-rg", cond = is_not_mini },
            { "saadparwaiz1/cmp_luasnip", cond = is_not_mini },
            "hrsh7th/cmp-omni",
            { "danymat/neogen", cond = is_not_mini },
            {
                -- "hrsh7th/cmp-nvim-lua",
                "iguanacucumber/mag-nvim-lua",
                name = "cmp-nvim-lua",
                cond = is_not_mini,
            },
            {
                "JMarkin/cmp-diag-codes",
                cond = is_not_mini,
                -- dev = true,
            },
            {
                -- "hrsh7th/cmp-nvim-lsp",
                "iguanacucumber/mag-nvim-lsp",
                name = "cmp-nvim-lsp",
                dependencies = { "onsails/lspkind.nvim" },
                cond = is_not_mini,
            },
            { "rcarriga/cmp-dap", cond = is_not_mini },
            "quangnguyen30192/cmp-nvim-tags",
            "dmitmel/cmp-cmdline-history",
            {
                -- "hrsh7th/cmp-cmdline",
                "iguanacucumber/mag-cmdline",
                name = "cmp-cmdline",
            },
            {
                -- "hrsh7th/cmp-buffer",
                "iguanacucumber/mag-buffer",
                name = "cmp-buffer",
            },
            "https://codeberg.org/FelipeLema/cmp-async-path",
            -- {
            --     "tzachar/cmp-ai",
            --     cond = is_not_mini,
            --     -- dev = true,
            --     config = function()
            --         local cmp_ai = require("cmp_ai.config")
            --
            --         local host = vim.env.OLLAMA_HOST or "192.168.88.251"
            --         local port = vim.env.OLLAMA_PORt or "11434"
            --
            --         cmp_ai:setup({
            --             max_lines = 200,
            --             provider = "Ollama",
            --             provider_options = {
            --                 base_url = string.format("http://%s:%s/api/generate", host, port),
            --                 model = "codellama:7b-code",
            --                 -- prompt = function(lines_before, lines_after)
            --                 --     local prmpt =  string.format(
            --                 --         "<|fim_prefix|>%s<|fim_suffix|>%s<|fim_middle|>",
            --                 --         lines_before,
            --                 --         lines_after
            --                 --     )
            --                 --     return prmpt
            --                 -- end,
            --             },
            --             notify = true,
            --             notify_callback = function(msg)
            --                 vim.notify(msg)
            --             end,
            --             run_on_every_keystroke = true,
            --         })
            --     end,
            -- },
        },
        config = function()
            local cmp = require("cmp")

            if is_not_mini() then
                cmp_config(default_sources)
            else
                cmp_config(mini_sources)
            end
            cmp_cmdline()

            -- cmp does not work with cmdline with type other than `:`, '/', and '?', e.g.
            -- it does not respect the completion option of `input()`/`vim.ui.input()`, see
            -- https://github.com/hrsh7th/nvim-cmp/issues/1690
            -- https://github.com/hrsh7th/nvim-cmp/discussions/1073
            cmp.setup.cmdline("@", { enabled = false })
            cmp.setup.cmdline(">", { enabled = false })
            cmp.setup.cmdline("-", { enabled = false })
            cmp.setup.cmdline("=", { enabled = false })
        end,
    },
}
