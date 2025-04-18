local api, completion, lsp = vim.api, vim.lsp.completion, vim.lsp
local ms = lsp.protocol.Methods
local g = api.nvim_create_augroup('glepnir.completion', { clear = true })

return {
    "nvimdev/phoenix.nvim",
    init = function()
        ---Default configuration values for Phoenix
        ---@type PhoenixConfig
        vim.g.phoenix = {
            -- Enable for all filetypes by default
            filetypes = { '*' },

            -- Dictionary settings control word storage
            dict = {
                capacity = 50000,                 -- Store up to 50k words
                min_word_length = 2,              -- Ignore single-letter words
                word_pattern = '[^%s%.%_:%p%d]+', -- Word pattern
            },

            -- Completion control the scoring
            completion = {
                max_items = 100,     -- Max result items
                decay_minutes = 30,  -- Time period for decay calculation
                weights = {
                    recency = 0.3,   -- 30% weight to recent usage
                    frequency = 0.7, -- 70% weight to frequency
                },
                priority = {
                    base = 100,         -- Base priority score (0-999)
                    position = 'after', -- Position relative to other LSP results: 'before' or 'after'
                },
            },

            -- Cleanup settings control dictionary maintenance
            cleanup = {
                cleanup_batch_size = 1000,   -- Process 1000 words per batch
                frequency_threshold = 0.1,   -- Keep words used >10% of max frequency
                collection_batch_size = 100, -- Collect 100 words before yielding
                rebuild_batch_size = 100,    -- Rebuild 100 words before yielding
                idle_timeout_ms = 1000,      -- Wait 1s before cleanup
                cleanup_ratio = 0.9,         -- Cleanup at 90% capacity
                enable_notify = false,       -- Enable notify when cleanup dictionary
            },

            -- Scanner settings control filesystem interaction
            scanner = {
                scan_batch_size = 1000,                        -- Scan 1000 items per batch
                cache_duration_ms = 5000,                      -- Cache results for 5s
                throttle_delay_ms = 200,                       -- Wait 200ms between updates
                ignore_patterns = {},                          -- Dictionary or file ignored when path completion
            },
            snippet = vim.fn.stdpath("config") .. "/snippets" -- path of snippet json file like c.json/zig.json/go.json
        }

        api.nvim_create_autocmd('CompleteChanged', {
            callback = function()
                local info = vim.fn.complete_info({ 'selected' })
                if info.preview_bufnr then
                    vim.bo[info.preview_bufnr].filetype = 'markdown'
                    vim.wo[info.preview_winid].conceallevel = 2
                    vim.wo[info.preview_winid].concealcursor = 'niv'
                    vim.wo[info.preview_winid].wrap = true
                end
            end,
        })

        api.nvim_create_autocmd('LspAttach', {
            group = g,
            callback = function(args)
                local bufnr = args.buf
                local client = lsp.get_client_by_id(args.data.client_id)
                if not client or not client:supports_method(ms.textDocument_completion) then
                    return
                end
                local chars = client.server_capabilities.completionProvider.triggerCharacters
                if chars then
                    for i = string.byte('a'), string.byte('z') do
                        if not vim.list_contains(chars, string.char(i)) then
                            table.insert(chars, string.char(i))
                        end
                    end

                    for i = string.byte('A'), string.byte('Z') do
                        if not vim.list_contains(chars, string.char(i)) then
                            table.insert(chars, string.char(i))
                        end
                    end
                end

                completion.enable(true, client.id, bufnr, {
                    autotrigger = true,
                    convert = function(item)
                        local kind = lsp.protocol.CompletionItemKind[item.kind] or 'u'
                        local doc = item.documentation or {}
                        local info
                        if vim.bo.filetype == 'c' then
                            info = ('%s%s\n \n%s'):format(item.detail or '', item.label, doc.value or '')
                        end
                        return {
                            abbr = item.label:gsub('%b()', ''),
                            kind = kind:sub(1, 1):lower(),
                            menu = '',
                            info = info and info:gsub('\n+%s*\n$', '') or nil,
                        }
                    end,
                })

                api.nvim_create_autocmd('TextChangedP', {
                    buffer = bufnr,
                    group = g,
                    command = 'let g:_ts_force_sync_parsing = v:true',
                })

                api.nvim_create_autocmd('CompleteDone', {
                    buffer = bufnr,
                    group = g,
                    command = 'let g:_ts_force_sync_parsing = v:false',
                })
            end,
        })
    end

}
