local fn = require("funcs")

fn.augroup("netrw", {
    "FileType",
    {
        pattern = {
            "netrw",
        },
        callback = function(event)
        end,
    },
})
