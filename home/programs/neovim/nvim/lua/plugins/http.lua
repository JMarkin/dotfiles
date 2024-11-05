return {
    "rest-nvim/rest.nvim",
    cmd = "Rest",
    ft = "http",
    -- dev = true,
    keys = {
        {
            "<leader>hr",
            "<cmd>Rest run<cr>",
            silent = true,
            desc = "run the request under the cursor",
            ft = "http",
        },
        {
            "<leader>hp",
            "<Plug>RestNvimPreview",
            silent = true,
            desc = "preview the request cURL command",
            ft = "http",
        },
        {
            "<leader>hl",
            "<cmd>Rest run last<cr>",
            silent = true,
            desc = "re-run the last request",
            ft = "http",
        },
    },
    -- enabled = false,
    config = function()
        vim.g.rest_nvim = {
            clients = {
                curl = {
                    statistics = {
                        { id = "remote_ip", winbar = "ip", title = "Remote IP" },
                        { id = "time_total", winbar = "time", title = "Time" },
                        { id = "time_namelookup", title = "Time dns" },
                        { id = "time_connect", title = "Time connect" },
                        { id = "time_pretransfer", title = "Time pretransfer" },
                        { id = "time_redirect", title = "Time redirect" },
                        { id = "time_starttransfer", title = "Time starttransfer" },
                        { id = "size_download", title = "Download size", winbar = false },
                        { id = "speed_download", title = "Download speed" },
                        { id = "size_upload", title = "Upload size" },
                        { id = "speed_upload", title = "Upload speed" },
                    },
                },
            },
        }
    end,
}
