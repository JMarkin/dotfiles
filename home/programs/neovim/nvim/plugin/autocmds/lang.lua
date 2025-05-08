local lf = require("largefiles")
local fn = require("funcs")

fn.augroup("linting", {
  { "BufWritePost", table.unpack(vim.g.post_load_events) },
  {
    pattern = { "*" },
    callback = function(data)
      if not lf.is_large_file(data.buf, true) then
        require("lint").try_lint()
      end
    end,
  },
})

local timer = nil --[[uv_timer_t]]
local function reset_timer()
  if timer then
    timer:stop()
    timer:close()
  end
  timer = nil
end

fn.augroup(
  "lspattach",
  {
    { "LspAttach" },
    {
      pattern = { "*" },
      callback = function(args)
        vim.b.lsp_attached = true
        if vim.bo[args.buf].filetype == "lua" and vim.api.nvim_buf_get_name(args.buf):find("_spec") then
          vim.diagnostic.enable(false, { bufnr = args.buf })
          return
        end
        local client = vim.lsp.get_clients({ id = args.data.client_id })[1]
        client.server_capabilities.semanticTokensProvider = nil
      end,
    },
  },
  {
    { "LspDetach" },
    {
      callback = function(args)
        local client_id = args.data.client_id
        local client = vim.lsp.get_clients({ client_id = client_id })[1]
        if not client or not vim.tbl_isempty(client.attached_buffers) then
          return
        end
        reset_timer()
        timer = assert(vim.uv.new_timer())
        timer:start(200, 0, function()
          reset_timer()
          vim.schedule(function()
            vim.lsp.stop_client(client_id, true)
          end)
        end)
      end,
      desc = "Auto stop client when no buffer atttached",
    },
  },
  --disable diagnostic in neovim test file *_spec.lua
  {
    "FileType",
    {
      pattern = "lua",
      callback = function(opt)
        local fname = vim.api.nvim_buf_get_name(opt.buf)
        if fname:find("%w_spec%.lua") then
          vim.diagnostic.enable(not vim.diagnostic.is_enabled({ bufnr = opt.buf }))
        end
      end,
    },
  }
)
