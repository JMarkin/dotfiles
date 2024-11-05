-- Maeson cool but

local fn = require("funcs")

local function pip_install(...)
    return {
        command = "bash",
        args = { "pip.sh", ...},
        cwd = "~/.config/nvim/installers",
    }
end

local DEFAULT_INSTALL_EXEC = {
    -- pip
    ruff = pip_install("ruff", "ruff>=0.5.6"),
    curlylint = pip_install("curlylint", "curlylint"),
    sqlfluff = pip_install("sqlfluff", "sqlfluff"),
    sqlfmt = pip_install("sqlfmt", "shandy-sqlfmt[jinjafmt]"),
    yapf = pip_install("yapf", "yapf"),
    black = pip_install("black", "black"),
    isort = pip_install("isort", "isort"),
    mypy = pip_install("mypy", "mypy"),
    pylint = pip_install("pylint", "pylint"),
    flake8 = pip_install("flake8", "flake8"),
    djhtml = pip_install("djhtml", "djhtml"),
    docformatter = pip_install("docformatter", "docformatter"),
    ["jedi-language-server"] = pip_install(
        "jedi-language-server",
        "git+https://github.com/JMarkin/jedi-language-server.git"
    ),
    ["python-lsp-server"] = pip_install("python-lsp-server", "python-lsp-server"),
    pyright = pip_install("pyright", "pyright"),
    basedpyright = pip_install("basedpyright", "basedpyright", "basedpyright-langserver"),
    ["nginx-language-server"] = pip_install("nginx-language-server", "nginx-language-server"),
    djlint = pip_install("djlint", "djlint"),
    codespell = pip_install("codespell", "codespell"),
    pylyzer = pip_install("pylyzer", "pylyzer"),

    -- npm
    spectral = { command = "npm", args = { "install", "-g", "@stoplight/spectral-cli" } },
    rome = { command = "npm", args = { "install", "-g", "rome" } },
    fixjson = { command = "npm", args = { "install", "-g", "fixjson" } },
    nginxbeautifier = { command = "npm", args = { "install", "-g", "nginxbeautifier" } },
    prettierd = { command = "npm", args = { "install", "-g", "@fsouza/prettierd" } },
    prettier = { command = "npm", args = { "install", "-g", "prettier" } },
    biome = { command = "npm", args = { "install", "-g", "@biomejs/biome" } },
    ["bash-language-server"] = { command = "npm", args = { "install", "-g", "bash-language-server" } },
    ["vue-language-server"] = { command = "npm", args = { "install", "-g", "@volar/vue-language-server" } },
    ["docker-compose-langserver"] = {
        command = "npm",
        args = { "install", "-g", "@microsoft/compose-language-service" },
    },
    ["docker-langserver"] = { command = "npm", args = { "install", "-g", "dockerfile-language-server-nodejs" } },
    ["yaml-language-server"] = { command = "npm", args = { "install", "-g", "yaml-language-server" } },
    ["vscode-json-language-server"] = { command = "npm", args = { "install", "-g", "vscode-langservers-extracted" } },
    ["vscode-html-language-server"] = { command = "npm", args = { "install", "-g", "vscode-langservers-extracted" } },
    ["vscode-css-language-server"] = { command = "npm", args = { "install", "-g", "vscode-langservers-extracted" } },
    ["vim-language-server"] = { command = "npm", args = { "install", "-g", "vim-language-server" } },
    ["typescript-language-server"] = {
        command = "npm",
        args = { "install", "-g", "typescript", "typescript-language-server" },
    },

    -- go
    protolint = { command = "go", args = { "install", "github.com/yoheimuta/protolint/cmd/protolint@latest" } },
    yamlfmt = { command = "go", args = { "install", "github.com/google/yamlfmt/cmd/yamlfmt@latest" } },

    -- cargo
    ["nil"] = {
        command = "cargo",
        args = { "install", "--git", "https://github.com/oxalica/nil.git", "--tag", "2023-08-09", "nil" },
    },
    stylua = {
        command = "cargo",
        args = { "install", "--locked", "--git", "https://github.com/JohnnyMorganz/StyLua.git", "--tag", "v0.20.0" },
    },
    taplo = {
        command = "cargo",
        args = {
            "install",
            "--locked",
            "--features",
            "lsp",
            "--git",
            "https://github.com/tamasfe/taplo.git",
            "taplo-cli",
        },
    },
    neocmakelsp = {
        command = "cargo",
        args = {
            "install",
            "neocmakelsp",
        },
    },
    ["jinja-lsp"] = {
        command = "cargo",
        args = {
            "install",
            "jinja-lsp",
        },
    },

    -- rustup
    ["rust-analyzer"] = {
        command = "rustup",
        args = { "component", "add", "rust-analyzer" },
    },
    ["rustfmt"] = {
        command = "rustup",
        args = { "component", "add", "rustfmt" },
    },

    -- custom
    ["lua-language-server"] = {
        command = "bash",
        args = { "luals.sh" },
        cwd = "~/.config/nvim/installers",
    },
}

local client_notifs = {}

local function get_notif_data(exec)
    if not client_notifs[exec] then
        client_notifs[exec] = {}
    end

    return client_notifs[exec]
end

local notify_progress = function(msg, exec, is_end, log_level)
    local notify = require("notify")
    local notify_data = get_notif_data(exec)
    -- local opts = { replace = notify_data.notify }
    local opts = {}
    if is_end then
        opts.timeout = 1000
    end
    if not log_level then
        log_level = vim.log.levels.INFO
    end
    local ny = notify(msg, log_level, opts)
    if ny then
        notify_data.notify = ny
    end
end

local function external_install(exec, sync, update, on_exit)
    local f = function()
        if vim.fn.executable(exec) ~= 1 or update then
            local shell = DEFAULT_INSTALL_EXEC[exec]
            if shell ~= nil then
                shell = vim.fn.map(shell, function(_, v)
                    return v
                end)
                shell.enable_recording = false
                shell.on_exit = function(_, return_val)
                    if return_val ~= 0 then
                        notify_progress(string.format("%s error", exec), exec, true, vim.log.levels.WARN)
                    else
                        notify_progress(string.format("Complete install %s", exec), exec, true)
                    end
                    if on_exit then
                        on_exit()
                    end
                end
                shell.on_stdout = function(_, data)
                    notify_progress(string.format("INSTALL %s %s", exec, data), exec, false)
                end
                shell.on_stderr = function(_, data)
                    notify_progress(string.format("INSTALL %s %s", exec, data), exec, false)
                end

                local notify_data = get_notif_data(exec)
                notify_data.notify = vim.notify(exec .. " not found, try install", vim.log.levels.INFO)

                local job = require("plenary.job"):new(shell)

                job:start()
                if sync then
                    -- 10min
                    job:wait(1000 * 60 * 10, 5, true)
                end
            else
                vim.notify(exec .. " not found config, please install manually", vim.log.levels.WARN)
            end
        else
            vim.notify(string.format("%s installed", exec), vim.log.levels.INFO)
        end
    end
    if sync then
        f()
    else
        vim.schedule(f)
    end
end

local default_sources = {
    "ruff",
    "mypy",
    "stylua",
    "nginxbeautifier",
    "prettier",
    "fixjson",
    "rustfmt",
    "sqlfmt",
    -- lsp
    "nginx-language-server",
    "jedi-language-server",
    "lua-language-server",
    "rust-analyzer",
    "bash-language-server",
}

local MAX_CONCURRENT = 2

local install = function(sync, update, sources)
    if not sources then
        sources = default_sources
    end

    local counter = 0
    local jobs = #sources

    local on_exit = function()
        counter = counter - 1
        jobs = jobs - 1
    end

    local function loop()
        if jobs > 0 then
            if counter < MAX_CONCURRENT then
                local source = sources[jobs - counter]
                if not source then
                    return
                end
                external_install(source, sync, update, on_exit)
                counter = counter + 1
            end
            vim.defer_fn(function()
                loop()
            end, 100)
        end
    end
    vim.schedule(loop)
end

vim.api.nvim_create_user_command("ExternalInstallDefault", function(_)
    install()
end, {})

vim.api.nvim_create_user_command("ExternalInstallDefaultSync", function(_)
    install(true)
end, {})

vim.api.nvim_create_user_command("ExternalUpdateDefault", function(_)
    install(false, true)
end, {})

vim.api.nvim_create_user_command("ExternalUpdateDefaultSync", function(_)
    install(true, true)
end, {})

local COMPL = {}
for key, _ in pairs(DEFAULT_INSTALL_EXEC) do
    table.insert(COMPL, key)
end

vim.api.nvim_create_user_command("ExternalInstall", function(event)
    external_install(event.args, false, false)
end, {
    nargs = 1,
    complete = function(_)
        return COMPL
    end,
})

vim.api.nvim_create_user_command("ExternalUpdate", function(event)
    external_install(event.args, false, true)
end, {
    nargs = 1,
    complete = function(_)
        return COMPL
    end,
})

return external_install
