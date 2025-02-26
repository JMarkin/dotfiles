local lf = require("largefiles")
local fn = require("funcs")

fn.augroup("largefiles", {
    vim.g.pre_load_events,
    {
        pattern = { "*" },
        callback = function(event)
            lf.optimize_buffer(event.buf, event.match)
        end,
    },
})

fn.augroup("local-highlight-attach", {
    vim.g.post_load_events,
    {
        pattern = "*",
        callback = function(data)
            if not lf.is_large_file(data.buf, true) then
                require("local-highlight").attach(data.buf)
            end
        end,
    },
})
