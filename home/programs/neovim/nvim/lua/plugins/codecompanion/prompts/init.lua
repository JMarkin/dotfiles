local funcs = require("funcs")

local prompts = {}

funcs.merge_tables(prompts, require("plugins.codecompanion.prompts.comments"))
funcs.merge_tables(prompts, require("plugins.codecompanion.prompts.expert"))

return prompts
