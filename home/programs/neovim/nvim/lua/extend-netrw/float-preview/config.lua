local maxline = require("funcs").maxline

local CFG = {
    _cfg = {
        -- Whether the float preview is enabled by default. When set to false, it has to be "toggled" on.
        toggled_on = true,
        -- lines for scroll
        scroll_lines = 20,
        -- window config
        window = {
            style = "minimal",
            relative = "cursor",
            border = "rounded",
            wrap = false,
            trim_height = true,
        },
        mapping = {
            -- scroll down float buffer
            down = { "<C-d>" },
            -- scroll up float buffer
            up = { "<C-e>", "<C-u>" },
            -- enable/disable float windows
            toggle = { "<C-x>" },
        },
        -- hooks if return false preview doesn't shown
        hooks = {

            pre_open = function(path)
                local is_showed = require("extend-netrw.float-preview.utils").is_showed(path)
                if is_showed then
                    return false
                end

                local is_text = require("extend-netrw.float-preview.utils").is_text(path)
                if not is_text then
                    return false
                end

                -- if file > 5 MB or not text -> not preview
                local size = require("extend-netrw.float-preview.utils").get_size(path)
                if type(size) ~= "number" then
                    return false
                end

                if size > 5 then
                    return false
                end

                -- len
                local len = maxline(path)
                if type(len) ~= "number" then
                    return false
                end

                if len > vim.o.synmaxcol then
                    return false
                end

                return true
            end,
            post_open = function(bufnr)
                return true
            end,
        },
    },
}

CFG.config = function()
    return CFG._cfg
end

CFG.update = function(cfg)
    if not cfg then
        return
    end

    CFG._cfg = vim.tbl_extend("force", CFG._cfg, cfg)
end

return CFG
