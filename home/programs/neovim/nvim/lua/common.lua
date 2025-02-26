local g = vim.g
local opt = vim.opt

g.has_ui = #vim.api.nvim_list_uis() > 0
g.modern_ui = (g.has_ui and vim.env.DISPLAY ~= nil) or string.format("%s", vim.env.TERM):find("256")
g.post_load_events = { "BufReadPost", "FileReadPost", "TermOpen" }
g.pre_load_events = { "BufReadPre", "FileReadPre", "BufNewFile", "TermOpen" }

-- stylua: ignore start
g.snips_author                                    = vim.env.AUTHOR or "Jury Markin"
g.snips_email                                     = vim.env.EMAIL or "me@jmarkin.ru"
g.snips_github                                    = vim.env.GITHUB or "https://github.com/JMarkin"


opt.foldlevelstart                                = 99
-- opt.foldenable                                    = true
-- opt.foldlevel                                     = 99
-- opt.foldmethod                                    = "expr"
-- opt.foldexpr                                      = "v:lua.vim.treesitter.foldexpr()"


opt.colorcolumn                                   = '+1'
opt.cursorlineopt                                 = 'both'
opt.cursorline                                    = true
g.cursorhold_updatetime                           = 200
g.default_winwidth                                = 20
g.default_winheight                               = 1
opt.winwidth                                      = g.default_winwidth
opt.winheight                                     = g.default_winheight
opt.winminwidth                                   = 20
opt.pumheight                                     = 20
opt.splitright                                    = true
opt.splitbelow                                    = true
opt.equalalways                                   = false
opt.updatetime                                    = 200
opt.mousemoveevent                                = true
opt.number                                        = true
g.numbertoggle                                    = true
opt.ruler                                         = true
opt.scrolloff                                     = 4
opt.sidescrolloff                                 = 8
opt.sidescroll                                    = 0
opt.signcolumn                                    = 'yes:1'
opt.swapfile                                      = true
opt.undofile                                      = true
opt.wrap                                          = false
opt.linebreak                                     = true
opt.breakindent                                   = true
opt.scrollback                                    = 2000
opt.conceallevel                                  = 0
opt.autowriteall                                  = true
opt.virtualedit                                   = 'block'
opt.mouse                                         = "a"
g.mapleader                                       = "\\"
opt.fileencoding                                  = "utf-8"
opt.encoding                                      = "utf-8"
opt.hidden                                        = true
opt.showmatch                                     = false
opt.hlsearch                                      = true
opt.autochdir                                     = false
opt.bs                                            = "indent,eol,start"
g.editorconfig                                    = true
opt.synmaxcol                                     = 2000
opt.exrc                                          = true

opt.guifont                                       = "JetBrainsMonoNL Nerd Font Mono:h13"
opt.guicursor                                     = "a:block"
opt.background                                    = "dark"

opt.completeopt                                   = "menu,menuone,noselect,popup,noinsert,fuzzy"
-- opt.completeopt                                   = "menu,menuone,popup,noselect"
opt.tags                                          = { "tags", ".git/tags" }

opt.spell                                         = false
opt.spelllang                                     = { "en", "ru" }
g.spellfile_URL                                   = "https://ftp.nluug.nl/vim/runtime/spell/"

g.root_pattern                                    = {
                                                        "pyproject.toml",
                                                        "package.json",
                                                        "Cargo.toml",
                                                        ".nvim.lua",
                                                        "Makefile",
                                                        ".git",
                                                        ".venv",
                                                    }
opt.list                                          = true
opt.listchars                                     = {
                                                      tab     = '→ ',
                                                      trail   = '·',
                                                      eol     = '↲',
                                                    }
opt.fillchars                                     = {
                                                      fold    = '·',
                                                      foldsep = ' ',
                                                      eob     = ' ',
                                                    }

opt.tabstop                                       = 4
opt.softtabstop                                   = 4
opt.shiftwidth                                    = 4
opt.expandtab                                     = true
opt.smartindent                                   = true
opt.autoindent                                    = true

opt.ignorecase                                    = true
opt.smartcase                                     = true

opt.termguicolors                                 = true

opt.textwidth                                     = 80

opt.relativenumber                                = true
opt.sessionoptions                                = 'curdir,folds,globals,help,tabpages,terminal,winsize'

g.omni_sql_ignorecase                             = 1


g.ollama_host                                     = vim.env.OLLAMA_HOST or "localhost"
g.ollama_port                                     = vim.env.OLLAMA_PORT or "11434"
g.ollama_url                                      = string.format("http://%s:%s", g.ollama_host, g.ollama_port)
g.ollama_generate_endpoint                        = string.format("%s/api/generate", g.ollama_url)
g.ollama_chat_endpoint                            = string.format("%s/api/chat", g.ollama_url)
g.ollama_completions_endpoint                     = string.format("%s/v1/completions", g.ollama_url)


g.lsp_autostart                                   = vim.env.LSP_AUTOSTART
opt.laststatus                                    = 3

opt.wildignore:append({ -- Ignore on file name completion.
	".DS_store",
	"**/node_modules/**",
})

-- stylua: ignore end
--
g.dbs = {
    { name = "local", url = "postgresql://kron:@/postgres" },
}

opt.shortmess:append({ W = false, I = true, c = true, C = true, A = false })

if g.modern_ui then
    opt.listchars:append({ nbsp = "␣" })
    opt.fillchars:append({
        eob = " ",
        foldsep = " ",
        foldopen = "",
        foldclose = "",
        diff = "╱",
    })

    vim.api.nvim_command("colorscheme ex-bamboo")
else
    opt.termguicolors = false
end

opt.backup = true
opt.backupdir:remove(".")

-- netrw settings
-- stylua: ignore start
g.netrw_winsize         = 20
g.netrw_banner          = 0
g.netrw_cursor          = 5
g.netrw_keepdir         = 1
g.netrw_list_hide       =  "__pycache__," .. [[\(^\|\s\s\)\zs\.\S\+]]
g.netrw_liststyle       = 0
g.netrw_localcopydircmd = "cp -r"
g.netrw_localmkdir      = "mkdir -p"
g.netrw_preview         = 1
g.netrw_alto            = 1
g.netrw_fastbrowse      = 2
g.netrw_sizestyle       = "H"
g.netrw_sort_options    = "i"
-- stylua: ignore end

-- disable plugins shipped with neovim
-- g.loaded_2html_plugin = 1
g.loaded_matchit = 1
g.loaded_tutor_mode_plugin = 1
g.loaded_vimball = 1
g.loaded_vimballPlugin = 1
g.loaded_python3_provider = 0
g.loaded_ruby_provider = 0
g.loaded_node_provider = 0
g.loaded_perl_provider = 0

-- g.loaded_zip = 1
-- g.loaded_zipPlugin = 1
-- g.loaded_gzip = 1
-- g.loaded_tar = 1
-- g.loaded_tarPlugin = 1
-- stylua: ignore end

g.linter_by_ft = {
    sql = { "codespell", "sqlfluff" },
    jinja = { "djlint" },
    htmldjango = { "djlint" },
    python = { "codespell", "mypy" },
    rust = { "codespell" },
}

g.formatters_by_ft = {
    lua = { "stylua" },
    python = { "ruff_format" },
    rust = { "rustfmt" },
    javascript = { "prettierd" },
    json = { "fixjson" },
    jinja = { "djlint" },
    htmldjango = { "djlint" },
    nix = { "nixpkgs_fmt" },
    go = { "gofmt" },
}

for _, lang in ipairs({
    "javascript",
    "typescript",
    "jsx",
    "tsx",
    "jsonc",
}) do
    g.formatters_by_ft[lang] = { "biome" }
end
for _, lang in ipairs({
    "markdown",
    "html",
    "css",
    "yaml",
    "scss",
    "vue",
}) do
    g.formatters_by_ft[lang] = { "prettierd" }
end

vim.g.rainbow_delimiters_highlight = {
    "RainbowDelimiterRed",
    "RainbowDelimiterYellow",
    "RainbowDelimiterBlue",
    "RainbowDelimiterOrange",
    "RainbowDelimiterGreen",
    "RainbowDelimiterViolet",
    "RainbowDelimiterCyan",
}
