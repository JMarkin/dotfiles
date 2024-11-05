local is_empty = function(str)
    return str == nil or str == ""
end

local shorting_target = 40

---shortens path by turning apple/orange -> a/orange
---@param path string
---@param sep string path separator
---@param max_len integer maximum length of the full filename string
---@return string
local function shorten_path(path, sep, max_len)
    local len = #path
    if len <= max_len then
        return path
    end

    local segments = vim.split(path, sep)
    for idx = 1, #segments - 1 do
        if len <= max_len then
            break
        end

        local segment = segments[idx]
        local shortened = segment:sub(1, vim.startswith(segment, ".") and 2 or 1)
        segments[idx] = shortened
        len = len - (#segment - #shortened)
    end

    return table.concat(segments, sep)
end

local get_filename = function(path)
    if is_empty(path) then
        return " %f"
    end
    return shorten_path(path, "/", shorting_target)
end

return {
    {
        "ramilito/winbar.nvim",
        -- event = "VeryLazy",
        dependencies = { "nvim-tree/nvim-web-devicons" },
        config = function()
            require("winbar").setup({
                -- your configuration comes here, for example:
                icons = true,
                filetype_exclude = {
                    "help",
                    "startify",
                    "dashboard",
                    "packer",
                    "neo-tree",
                    "neogitstatus",
                    "NvimTree",
                    "Trouble",
                    "alpha",
                    "lir",
                    "Outline",
                    "spectre_panel",
                    "toggleterm",
                    "TelescopePrompt",
                    "prompt",
                    "httpResult",
                    "http",
                    "rest_nvim_result",
                    "netrw",
                },
                diagnostics = true,
                buf_modified = true,
                dir_levels = 2,
                -- buf_modified_symbol = "M",
                -- or use an icon
                buf_modified_symbol = "●",
                dim_inactive = {
                    enabled = true,
                    highlight = "WinbarNC",
                    icons = true, -- whether to dim the icons
                    name = true, -- whether to dim the name
                },
            })
        end,
    },
}
