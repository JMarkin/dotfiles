local M = {}

M.pcall_notify = function(func)
    local ok, out = pcall(func)
    if not ok then
        vim.notify_once(string.format("%s", out), vim.log.levels.DEBUG)
    end
    return out
end

M.is_not_mini = function()
    return vim.env.NVIM_MINI == nil
end

M.doau = function(pattern, data)
    vim.api.nvim_exec_autocmds("User", {
        pattern = pattern,
        data = data,
    })
end

function M.maxline(path, break_after)
    if break_after == nil then
        break_after = vim.o.synmaxcol + 1
    end
    local max = 0
    local fd = vim.uv.fs_open(path, "r", 1)
    if not fd then
        return max
    end
    local stat = vim.uv.fs_fstat(fd)
    local data = vim.uv.fs_read(fd, stat.size, nil)
    vim.uv.fs_close(fd)
    if not data then
        return max
    end

    local lines = vim.split(data, "[\r]?\n")

    for _, line in pairs(lines) do
        if max < #line then
            max = #line
        end
        if max >= break_after then
            return max
        end
    end
    return max
end

-- Executes a user-supplied "reducer" callback function on each element of the table indexed with a numeric key, in order, passing in the return value from the calculation on the preceding element
M.ireduce = function(tbl, func, acc)
    for i, v in ipairs(tbl) do
        acc = func(acc, v, i)
    end
    return acc
end

-- Returns the first element in the array that satisfies the provided testing function
M.ifind = function(tbl, func)
    for index, item in ipairs(tbl) do
        if func(item, index) then
            return item
        end
    end

    return nil
end

vim.api.nvim_create_user_command("Jaq", function(opts)
    local bufnr = vim.api.nvim_get_current_buf()
    local path = vim.api.nvim_buf_get_name(bufnr)

    if #opts.fargs > 0 then
        path = path
    end

    local fzflua = require("fzf-lua")

    local function jaq_fzf(jaq_query)
        fzflua.fzf_exec(string.format("jaq -c '%s' %s", jaq_query, path), {
            multiprocess = true,
            prompt = string.format("%s > ", jaq_query),
            fzf_opts = {
                ["--preview"] = "echo -e {} | fixjson | bat --style numbers",
            },
            actions = {
                ---@diagnostic disable-next-line: unused-local
                ["default"] = function(selected, _opts)
                    fzflua.grep_curbuf({
                        multiprocess = true,
                        search = selected[1],
                    })
                end,
            },
            fn_transform = function(x)
                if x == "null" then
                    return
                end
                return x
            end,
        })
    end

    fzflua.fzf_live(string.format("jaq -c '<query>' %s", path), {
        multiprocess = true,
        prompt = "jaq> ",
        fzf_opts = {
            ["--preview"] = "echo -e {} | fixjson | bat --style numbers",
        },
        actions = {
            ---@diagnostic disable-next-line: unused-local
            ["default"] = function(_selected, _opts)
                jaq_fzf(fzflua.get_last_query())
            end,
        },
        fn_transform = function(x)
            if x == "null" then
                return
            end
            return x
        end,
    })
end, {
    nargs = "*",
})

return M
