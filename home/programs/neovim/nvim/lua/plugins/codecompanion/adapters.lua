local M = {
    opts = {
        show_defaults = false,
    },
}


M.gemini = function()
    return require("codecompanion.adapters").extend("gemini", {
        env = {
            api_key = "GEMINI_API",
        },
    })
end
M.x5qwen = function()
    return require("codecompanion.adapters").extend("openai_compatible", {
        env = {
            url = "http://proxy-kafka.k8s.airun-dev-1.salt.x5.ru",
            api_key = "X5_QWEN_API",           -- optional: if your endpoint is authenticated
            chat_url = "/v1/chat/completions", -- optional: default value, override if different
            -- models_endpoint = "/v1/models", -- optional: attaches to the end of the URL to form the endpoint to retrieve models
        },
        schema = {
            model = {
                default = "x5-airun-medium-coder-prod",
                choices = function(self)
                    return {}
                end,
            },
            num_ctx = {
                default = 32768,
            },
        },
    })
end

local function ollama_params(model_name, model)
    return function()
        return require("codecompanion.adapters").extend("ollama", {
            env = {
                url = vim.g.ollama_url,
            },
            headers = {
                ["Content-Type"] = "application/json",
            },
            parameters = {
                sync = true,
                keep_alive = "30m",
            },
            name = model_name,
            schema = {
                model = {
                    default = model,
                },
                num_ctx = {
                    default = 16384,
                },
                temperature = {
                    default = 0.5,
                },
            },
        })
    end
end

M.ollama_deepseek = ollama_params("deepseek-r1", "hf.co/unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF:Q4_K_M")
M.ollama_deepcode = ollama_params("deepcode", "hf.co/lmstudio-community/DeepCoder-14B-Preview-GGUF:Q4_K_M")
M.ollama_gemma3 = ollama_params("gemma3", "gemma3:12b")
M.ollama_phimini = ollama_params("phimini", "phi4-mini:latest")
M.ollama_codegemma = ollama_params("codegemma", "codegemma:latest")


local function ollama_qwen(model_name, model)
    local params_func = ollama_params(model_name, model)

    return function()
        local params = params_func()
        params.schema.num_ctx.default = 40960
        params.schema.num_predict.default = 32768

        return params
    end
end

M.ollama_qwencoder = ollama_qwen("qwen2.5", "qwen2.5-coder:14b-instruct-q4_K_M")
M.ollama_qwen = ollama_qwen("qwen3", "qwen3:8b")
M.ollama_qwenamall = ollama_qwen("qwen3-small", "qwen3:0.6b")
M.ollama_qwenlarge = ollama_qwen("qwen3-large", "qwen3:30b-a3b")


M.default_adapter = M.ollama_qwenlarge
return M
