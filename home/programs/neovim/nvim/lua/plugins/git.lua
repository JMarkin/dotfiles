return {
    {
        "NeogitOrg/neogit",
        cmd = {
            "Neogit",
        },
        dependencies = {
            "nvim-lua/plenary.nvim", -- required
            "sindrets/diffview.nvim", -- optional - Diff integration

            -- Only one of these is needed.
            -- "nvim-telescope/telescope.nvim", -- optional
            "ibhagwan/fzf-lua", -- optional
            -- "echasnovski/mini.pick", -- optional
        },
        opts = {
            graph_style = "unicode",
            git_services = {
                ["github.com"] = "https://github.com/${owner}/${repository}/compare/${branch_name}?expand=1",
                ["bitbucket.org"] = "https://bitbucket.org/${owner}/${repository}/pull-requests/new?source=${branch_name}&t=1",
                ["gitlab.com"] = "https://gitlab.com/${owner}/${repository}/merge_requests/new?merge_request[source_branch]=${branch_name}",
                ["scm.com"] = "https://scm.com/${owner}/${repository}/merge_requests/new?merge_request[source_branch]=${branch_name}",
                ["azure.com"] = "https://dev.azure.com/${owner}/_git/${repository}/pullrequestcreate?sourceRef=${branch_name}&targetRef=${target}",
            },
        },
    },
    {
        "FabijanZulj/blame.nvim",
        config = function()
            require("blame").setup({
                date_format = "%d.%m.%Y",
                virtual_style = "right_align",
                commit_detail_view = "vsplit",
                merge_consecutive = true,
                mappings = {
                    commit_info = "i",
                    stack_push = "<TAB>",
                    stack_pop = "<BS>",
                    show_commit = "s",
                    close = { "<esc>", "q" },
                },
            })
        end,
        keys = {
            { "<leader>gB", ":BlameToggle window<cr>", desc = "Git blame" },
        },
    },
    {
        "moyiz/git-dev.nvim",
        opts = {
            cd_type = "tab",
            opener = function(dir)
                vim.cmd("tabnew")
                -- require("yazi").yazi({}, vim.fn.fnameescape(dir))
                vim.cmd("NvimTreeOpen " .. vim.fn.fnameescape(dir))
            end,
            git = {
                base_uri_format = "%s",
            },
        },
        keys = {
            {
                "<leader>o",
                function()
                    local repo = vim.fn.input("Repository name / URI: ")
                    if repo ~= "" then
                        require("git-dev").open(repo)
                    end
                end,
                desc = "[O]pen a remote git repository",
            },
        },
    },
    {
        "lewis6991/gitsigns.nvim",
        config = function()
            require("gitsigns").setup({
                on_attach = function(bufnr)
                    local gs = package.loaded.gitsigns

                    local function map(mode, l, r, opts)
                        opts = opts or {}
                        opts.buffer = bufnr
                        vim.keymap.set(mode, l, r, opts)
                    end

                    -- Navigation
                    map("n", "]c", function()
                        if vim.wo.diff then
                            return "]c"
                        end
                        vim.schedule(function()
                            gs.next_hunk({ preview = true })
                        end)
                        return "<Ignore>"
                    end, { expr = true, desc = "Git: next hunk" })

                    map("n", "[c", function()
                        if vim.wo.diff then
                            return "[c"
                        end
                        vim.schedule(function()
                            gs.prev_hunk({ preview = true })
                        end)
                        return "<Ignore>"
                    end, { expr = true, desc = "Git: prev hunk" })

                    -- Actions
                    map("n", "<leader>gb", function()
                        gs.blame_line({ full = true })
                    end, { desc = "Git: blame line full" })
                end,
            })
        end,
        -- event = vim.g.pre_load_events,
        event = "VeryLazy",
        keys = {
            "<leader>gS",
            "<leader>gu",
            "<leader>gb",
            "[c",
            "]c",
            { "<space>s", ":Gitsign stage_hunk<cr>", desc = "Git: stage hunk", mode = { "n", "v" } },
            { "<space>S", ":Gitsign stage_buffer<cr>", desc = "Git: stage buffer" },
            { "<space>u", ":Gitsign undo_stage_hunk<cr>", desc = "Git: undo stage hunk", mode = { "n", "v" } },
            { "<leader>gr", ":Gitsign reset_hunk<cr>", desc = "Git: reset hunk", mode = { "n", "v" } },
            { "<leader>gR", ":Gitsign reset_buffer<cr>", desc = "Git: reset buffer" },
            { "<leader>gp", ":Gitsign preview_hunk_inline<cr>", desc = "Git: preview hunk" },
            { "ih", ":<C-U>Gitsigns select_hunk<CR>", desc = "Git: select hunk", mode = { "o", "x" } },
        },
    },
}
