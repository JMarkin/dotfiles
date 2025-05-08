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
