local funcs = require("funcs")

local prompts = {}

funcs.merge_tables(prompts, require("plugins.ai.codecompanion.prompts.comments"))
funcs.merge_tables(prompts, require("plugins.ai.codecompanion.prompts.expert"))

return prompts
