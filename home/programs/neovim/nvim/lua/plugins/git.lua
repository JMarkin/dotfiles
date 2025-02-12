return {
    {
        "moyiz/git-dev.nvim",
        opts = {
            cd_type = "tab",
            opener = function(dir)
                vim.cmd("tabnew")
                -- require("yazi").yazi({}, vim.fn.fnameescape(dir))
                -- vim.cmd("NvimTreeOpen " .. vim.fn.fnameescape(dir))
                vim.cmd("Explore" .. vim.fn.fnameescape(dir))
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
                end,
            })
        end,
        -- event = vim.g.pre_load_events,
        event = "VeryLazy",
        keys = {
            "[c",
            "]c",
            { "<leader>gb", ":Gitsign blame_line<cr>", desc = "Git: blake line" },
            { "<leader>gB", ":Gitsign blame<cr>", desc = "Git: blame" },
            { "<leader>gs", ":Gitsign stage_hunk<cr>", desc = "Git: stage hunk", mode = { "n", "v" } },
            { "<leader>gS", ":Gitsign stage_buffer<cr>", desc = "Git: stage buffer" },
            { "<leader>gu", ":Gitsign undo_stage_hunk<cr>", desc = "Git: undo stage hunk", mode = { "n", "v" } },
            { "<leader>gr", ":Gitsign reset_hunk<cr>", desc = "Git: reset hunk", mode = { "n", "v" } },
            { "<leader>gR", ":Gitsign reset_buffer<cr>", desc = "Git: reset buffer" },
            { "<leader>gp", ":Gitsign preview_hunk_inline<cr>", desc = "Git: preview hunk" },
            { "ih", ":<C-U>Gitsigns select_hunk<CR>", desc = "Git: select hunk", mode = { "o", "x" } },
        },
    },
    {
        "tpope/vim-fugitive",
        cmd = {
            "Git",
        },
    },
}
