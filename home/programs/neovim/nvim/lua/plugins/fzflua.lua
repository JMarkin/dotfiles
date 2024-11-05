local autocmd = vim.api.nvim_create_autocmd
local augroup = vim.api.nvim_create_augroup

return {
    "ibhagwan/fzf-lua",
    cmd = "FzfLua",
    lazy = true,
    keys = {
        {
            "<leader>sq",
            function()
                require("fzf-lua").quickfix({ multiprocess = true })
            end,
            desc = "Search: quickfix",
        },
        {
            "<leader>sr",
            function()
                require("fzf-lua").oldfiles({
                    multiprocess = true,
                    cwd_only = true,
                })
            end,
            desc = "Search: old files",
        },
        {
            "<leader>sl",
            function()
                require("fzf-lua").loclist({ multiprocess = true })
            end,
            desc = "Search: loclist",
        },
        {
            "<leader>ss",
            function()
                require("fzf-lua").resume({ multiprocess = true })
            end,
            desc = "Search: previous",
        },
        -- {
        --     "<leader>sb",
        --     function()
        --         require("fzf-lua").buffers({ multiprocess = true, current_tab_only = true })
        --     end,
        --     desc = "Search: buffers",
        -- },
        {
            "<leader>sb",
            function()
                require("fzf-lua").buffers({ multiprocess = true }) --, current_tab_only = true })
            end,
            desc = "Search: buffers",
        },
        {
            "<leader>sf",
            function()
                require("fzf-lua").files({ multiprocess = true })
            end,
            desc = "Search: find files",
        },
        {
            "<leader>sg",
            function()
                require("fzf-lua").grep_project({ multiprocess = true, continue_last_search = true })
            end,
            desc = "Search: project",
        },
        {
            "<leader>sg",
            function()
                require("fzf-lua").grep_visual({ multiprocess = true, continue_last_search = true })
            end,
            desc = "Search: project",
            mode = "v",
        },
        {
            "gr",
            function()
                require("fzf-lua").grep_cword({ multiprocess = true })
            end,
            desc = "Search: references",
        },
        {
            "gr",
            function()
                require("fzf-lua").grep_visual({ multiprocess = true })
            end,
            desc = "Search: visual references",
            mode = "v",
        },
        {
            "<leader>s/",
            function()
                require("fzf-lua").lgrep_curbuf({ multiprocess = true })
            end,
            desc = "Search: current buffer",
        },
        {
            "<leader>st",
            function()
                require("fzf-lua").btags({ multiprocess = true })
            end,
            desc = "Search: tags current file",
        },
        {
            "<leader>sT",
            function()
                require("fzf-lua").tags({ multiprocess = true })
            end,
            desc = "Search: tags global",
        },
        {
            "<leader>sT",
            function()
                require("fzf-lua").tags_grep_visual({ multiprocess = true })
            end,
            desc = "Search: tags",
            mode = "v",
        },
        {
            "<leader>sh",
            function()
                require("fzf-lua").help_tags({ multiprocess = true })
            end,
            desc = "Search: helptags",
        },
        {
            "<leader>sc",
            function()
                require("fzf-lua").commands({ multiprocess = true })
            end,
            desc = "Search: commands",
        },
        {
            "<leader>sk",
            function()
                require("fzf-lua").keymaps({ multiprocess = true })
            end,
            desc = "Search: keymaps",
        },
        {
            "<leader>sch",
            function()
                require("fzf-lua").command_history({ multiprocess = true })
            end,
            desc = "Search: command_history",
        },
        {
            "<leader>gt",
            function()
                require("fzf-lua").git_status({ multiprocess = true })
            end,
            desc = "Search: git status",
        },
        {
            "<leader>gC",
            function()
                require("fzf-lua").git_commits({ multiprocess = true })
            end,
            desc = "Search: git commits",
        },
        {
            "<leader>gc",
            function()
                require("fzf-lua").git_bcommits({ multiprocess = true })
            end,
            desc = "Search: git commits",
        },
    },
    config = function()
        local actions = require("fzf-lua.actions")
        require("fzf-lua").setup({
            -- fzf_bin = "sk",
            async_or_timeout = 3000,
            global_resume = true,
            global_resume_query = true,
            -- winopts = {
            --     height = 0.8,
            --     width = 0.75,
            --     -- preview = {
            --     --     scrollbar = false,
            --     --     default = "builtin",
            --     --     layout = "vertical",
            --     --     title_align = "center",
            --     -- },
            -- },
            keymap = {
                builtin = {
                    ["<F1>"] = "toggle-help",
                    ["<F2>"] = "toggle-fullscreen",
                    ["<F3>"] = "toggle-preview-wrap",
                    ["<F4>"] = "toggle-preview",
                    ["<F5>"] = "toggle-preview-ccw",
                    ["<F6>"] = "toggle-preview-cw",
                    ["<C-d>"] = "preview-page-down",
                    ["<C-e>"] = "preview-page-up",
                    ["<C-r>"] = "preview-page-reset",
                },
                fzf = {
                    ["ctrl-z"] = "abort",
                    ["ctrl-u"] = "unix-line-discard",
                    ["ctrl-f"] = "half-page-down",
                    ["ctrl-b"] = "half-page-up",
                    ["ctrl-a"] = "beginning-of-line",
                    ["ctrl-e"] = "end-of-line",
                    ["alt-a"] = "toggle-all",
                    ["f3"] = "toggle-preview-wrap",
                    ["f4"] = "toggle-preview",
                    ["shift-down"] = "preview-page-down",
                    ["shift-up"] = "preview-page-up",
                    ["tab"] = "down",
                    ["shift-tab"] = "up",
                    ["ctrl-space"] = "toggle+down",
                },
            },
            files = {
                actions = {
                    ["ctrl-g"] = { actions.toggle_ignore },
                    ["tab"] = false,
                },
            },
            fzf_opts = {
                ["--ansi"] = "",
                ["--info"] = "inline",
                ["--height"] = "100%",
                ["--layout"] = "reverse",
                ["--border"] = "none",
            },
            lsp = {
                code_actions = {
                    previewer = "codeaction_native",
                    preview_pager = "delta --side-by-side --width=${FZF_PREVIEW_COLUMNS} --hunk-header-style='omit' --file-style='omit'",
                },
            },
            helptags = {
                actions = {
                    -- Open help pages in a vertical split.
                    ["default"] = actions.help_vert,
                },
            },
            oldfiles = {
                include_current_session = true,
                fzf_opts = { ["--tiebreak"] = "index" },
            },
            git = {
                files = {
                    prompt = "GitFiles❯ ",
                    cmd = "git ls-files --exclude-standard",
                    multiprocess = true, -- run command in a separate process
                    git_icons = true, -- show git icons?
                    file_icons = true, -- show file icons?
                    color_icons = true, -- colorize file|git icons
                    -- force display the cwd header line regardles of your current working
                    -- directory can also be used to hide the header when not wanted
                    -- cwd_header = true
                },
                status = {
                    prompt = "GitStatus❯ ",
                    cmd = "git -c color.status=false status -su",
                    file_icons = true,
                    git_icons = true,
                    color_icons = true,
                    previewer = "git_diff",
                    -- uncomment if you wish to use git-delta as pager
                    preview_pager = "delta --width=${FZF_PREVIEW_COLUMNS}",
                    actions = {
                        -- actions inherit from 'actions.files' and merge
                        ["right"] = { fn = actions.git_unstage, reload = true },
                        ["left"] = { fn = actions.git_stage, reload = true },
                        ["ctrl-x"] = { fn = actions.git_reset, reload = true },
                    },
                    -- If you wish to use a single stage|unstage toggle instead
                    -- using 'ctrl-s' modify the 'actions' table as shown below
                    -- actions = {
                    --   ["right"]   = false,
                    --   ["left"]    = false,
                    --   ["ctrl-x"]  = { fn = actions.git_reset, reload = true },
                    --   ["ctrl-s"]  = { fn = actions.git_stage_unstage, reload = true },
                    -- },
                },
                commits = {
                    prompt = "Commits❯ ",
                    cmd = "git log --color --pretty=format:'%C(yellow)%h%Creset %Cgreen(%><(12)%cr%><|(12))%Creset %s %C(blue)<%an>%Creset'",
                    preview = "git show --pretty='%Cred%H%n%Cblue%an <%ae>%n%C(yellow)%cD%n%Cgreen%s' --color {1}",
                    -- uncomment if you wish to use git-delta as pager
                    preview_pager = "delta --width=${FZF_PREVIEW_COLUMNS}",
                    actions = {
                        ["default"] = actions.git_checkout,
                        -- remove `exec_silent` or set to `false` to exit after yank
                        ["ctrl-y"] = { fn = actions.git_yank_commit, exec_silent = true },
                    },
                },
                bcommits = {
                    prompt = "BCommits❯ ",
                    -- default preview shows a git diff vs the previous commit
                    -- if you prefer to see the entire commit you can use:
                    --   git show --color {1} --rotate-to=<file>
                    --   {1}    : commit SHA (fzf field index expression)
                    --   <file> : filepath placement within the commands
                    cmd = "git log --color --pretty=format:'%C(yellow)%h%Creset %Cgreen(%><(12)%cr%><|(12))%Creset %s %C(blue)<%an>%Creset' <file>",
                    preview = "git diff --color {1}^! -- <file>",
                    -- uncomment if you wish to use git-delta as pager
                    preview_pager = "delta --width=${FZF_PREVIEW_COLUMNS}",
                    actions = {
                        ["default"] = actions.git_buf_edit,
                        ["ctrl-s"] = actions.git_buf_split,
                        ["ctrl-v"] = actions.git_buf_vsplit,
                        ["ctrl-t"] = actions.git_buf_tabedit,
                        ["ctrl-y"] = { fn = actions.git_yank_commit, exec_silent = true },
                    },
                },
                branches = {
                    prompt = "Branches❯ ",
                    cmd = "git branch --all --color",
                    preview = "git log --graph --pretty=oneline --abbrev-commit --color {1}",
                    actions = {
                        ["default"] = actions.git_switch,
                    },
                },
                tags = {
                    prompt = "Tags> ",
                    cmd = "git for-each-ref --color --sort=-taggerdate --format "
                        .. "'%(color:yellow)%(refname:short)%(color:reset) "
                        .. "%(color:green)(%(taggerdate:relative))%(color:reset)"
                        .. " %(subject) %(color:blue)%(taggername)%(color:reset)' refs/tags",
                    preview = "git log --graph --color --pretty=format:'%C(yellow)%h%Creset "
                        .. "%Cgreen(%><(12)%cr%><|(12))%Creset %s %C(blue)<%an>%Creset' {1}",
                    fzf_opts = { ["--no-multi"] = "" },
                    actions = { ["default"] = actions.git_checkout },
                },
                stash = {
                    prompt = "Stash> ",
                    cmd = "git --no-pager stash list",
                    preview = "git --no-pager stash show --patch --color {1}",
                    actions = {
                        ["default"] = actions.git_stash_apply,
                        ["ctrl-x"] = { fn = actions.git_stash_drop, reload = true },
                    },
                    fzf_opts = {
                        ["--no-multi"] = "",
                        ["--delimiter"] = "'[:]'",
                    },
                },

                previewers = {
                    builtin = {
                        syntax = true, -- preview syntax highlight?
                        treesitter = { enable = true, disable = {} },
                    },
                },
                grep = {
                    rg_opts = "--multiline --column --line-number --no-heading --color=always --smart-case --max-columns=4096 -e",
                },
            },
        })
        require("fzf-lua").config.globals.fzf_opts["--border"] = nil

        local fzf = "FZF"
        augroup(fzf, { clear = true })
        autocmd("VimResized", {
            pattern = "*",
            group = fzf,
            command = 'lua require("fzf-lua").redraw()',
        })

        require("fzf-lua").register_ui_select()
    end,
    init = function()
        vim.ui.select = function(...)
            require("lazy").load({ plugins = { "fzf-lua" } })
            return vim.ui.select(...)
        end
    end,
}
