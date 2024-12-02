local M = {}
function M.getVenvSuffix()
    if vim.loop.os_uname().sysname == "Windows_NT" then
        return "Scripts/python.exe"
    else
        return "bin/python"
    end
end

function M.getVenvFromJson(jsonfile)
    if not vim.fn.filereadable(jsonfile) then
        return nil
    end
    local f = io.open(jsonfile, "r")
    if not f then
        return nil
    end
    local data = f:read("*a")
    f:close()
    if data then
        local jdata = vim.json.decode(data)
        if jdata["venvPath"] ~= nil and jdata["venv"] ~= nil then
            return jdata["venvPath"] .. "/" .. jdata["venv"]
        end
    end
    return nil
end

function M.unixGetPythonPath()
    local out = vim.system({ "which", "python3" }, { text = true }):wait()
    local res = out.stdout:gsub("%s+", "")
    return res
end

function M.getPythonEnv()
    local venv = os.getenv("VIRTUAL_ENV")
    if venv ~= nil then
        return string.format("%s/%s", venv, M.getVenvSuffix())
    end
    local conda = os.getenv("CONDA_PREFIX")
    if conda ~= nil then
        return string.format("%s/%s", conda, "python.exe")
    end

    local cwd = vim.fn.getcwd()

    local jsonVenv = M.getVenvFromJson(cwd .. "/pyrightconfig.json")
    if jsonVenv ~= nil then
        return jsonVenv .. "/" .. M.getVenvSuffix()
    end

    if vim.fn.executable(cwd .. "/venv/" .. M.getVenvSuffix()) == 1 then
        return cwd .. "/venv/" .. M.getVenvSuffix()
    elseif vim.fn.executable(cwd .. "/.venv/" .. M.getVenvSuffix()) == 1 then
        return cwd .. "/.venv/" .. M.getVenvSuffix()
    else
        if vim.loop.os_uname().sysname == "Windows_NT" then
            return os.getenv("SCOOP") .. "/apps/python/current/python.exe"
        else
            return M.unixGetPythonPath()
        end
    end
end

print(M.getPythonEnv())

function M.getPythonEnvs()
    local venvs = {}
    local venv = os.getenv("VIRTUAL_ENV")
    if venv ~= nil then
        table.insert(venvs, {
            name = "VIRTUAL_ENV",
            path = string.format("%s/%s", venv, M.getVenvSuffix()),
        })
    end
    local conda = os.getenv("CONDA_PREFIX")
    if conda ~= nil then
        table.insert(venvs, {
            name = "CONDA_PREFIX",
            path = string.format("%s/%s", conda, "python.exe"),
        })
    end

    local cwd = vim.fn.getcwd()

    local jsonVenv = M.getVenvFromJson(cwd .. "/pyrightconfig.json")
    if jsonVenv ~= nil then
        table.insert(venvs, {
            name = "pyrightconfig.json",
            path = jsonVenv .. "/" .. M.getVenvSuffix(),
        })
    end

    local venvDirs = { "venv", ".venv" }
    for _, envDir in pairs(venvDirs) do
        if vim.fn.executable(cwd .. "/" .. envDir .. "/" .. M.getVenvSuffix()) == 1 then
            table.insert(venvs, {
                name = envDir,
                path = cwd .. "/" .. envDir .. "/" .. M.getVenvSuffix(),
            })
        end
    end
    if vim.loop.os_uname().sysname == "Windows_NT" then
        table.insert(venvs, {
            name = "system",
            path = os.getenv("SCOOP") .. "/apps/python/current/python.exe",
        })
    else
        table.insert(venvs, {
            name = "system",
            path = M.unixGetPythonPath(),
        })
    end
    return venvs
end

M.pick_venv = function()
    vim.ui.select(M.getPythonEnvs(), {
        prompt = "Select python venv",
        format_item = function(item)
            return string.format("%s (%s)", item.name, item.path)
        end,
    }, function(choice)
        if not choice then
            return
        end
        print(choice.path)
    end)
end

return M
