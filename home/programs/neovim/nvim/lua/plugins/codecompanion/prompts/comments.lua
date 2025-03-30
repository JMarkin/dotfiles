local PROMPTS = {
    ["Comments"] = {
        strategy = "inline",
        description = "Add comments to not simplify ",
        opts = {
            modes = { "v" },
            short_name = "comments",
            auto_submit = true,
            stop_context_insertion = true,
            user_prompt = false,
        },
        prompts = {
            {
                role = "system",
                content = function(context)
                    return "I want you to act as a expert of "
                        .. context.filetype
                        .. "\n"
                        .. [[
You must:
- Answer without ```
- Avoid wrapping the whole response in triple backticks.
]]
                end,
            },
            {
                role = "user",
                content = function(context)
                    local text = require("codecompanion.helpers.actions").get_code(context.start_line, context.end_line)

                    return "I have the following code:\n\n```"
                        .. context.filetype
                        .. "\n"
                        .. text
                        .. "\n```\n Please add short comments on not simply cases.\n"
                end,
                opts = {
                    contains_code = true,
                },
            },
        },
    },
}
PROMPTS["Comments Ru"] = vim.deepcopy(PROMPTS["Comments"])
PROMPTS["Comments Ru"].opts.short_name = "comments_ru"
PROMPTS["Comments Ru"].prompts[2].content = function(context)
    return PROMPTS["Comments"].prompts[2].content(context) .. "\n Ответь кратко на русском."
end

return PROMPTS
