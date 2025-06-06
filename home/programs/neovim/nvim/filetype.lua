local function vim2ext(t, s, ft)
  for k in string.gmatch(s, "%*%.(%w+),") do
    t[k] = ft
  end
end

local lf = require("largefiles")

local ext = {
  dockerfile = "dockerfile",
  automount = "systemd",
  mount = "systemd",
  path = "systemd",
  service = "systemd",
  socket = "systemd",
  swap = "systemd",
  target = "systemd",
  timer = "systemd",
  log = "log",
  LOG = "log",
  _log = "log",
  _LOG = "log",
  scpt = "applescript",
  applescript = "applescript",
  Caddyfile = "caddyfile",
  csv = "csv",
  tsv = "csv",
  tab = "csv",
  dat = "csv",
  mako = "mako",
  dbml = "dbml",
  lalrpop = "lalrpop",
  snippets = "snippets",
  jinja = "jinja",
  jinja2 = "jinja",
  j2 = "jinja",
  http = "http",
  tmpl = "gotmpl",
}

vim2ext(ext, "*.vert,*.tesc,*.tese,*.glsl,*.geom,*.frag,*.comp,*.rgen,*.rmiss,*.rchit,*.rahit,*.rint,*.rcall", "glsl")
vim2ext(ext, "*.vs,*.fs", "glsl")
vim2ext(ext, "*.graphql,*.graphqls,*.gql,*.prisma", "graphql")
vim2ext(ext, "*.gotmpl,helmfile*.yaml", "yaml.helm")

vim.filetype.add({
  extension = ext,
  pattern = {
    ["openapi.*%.ya?ml"] = "yaml.openapi",
    ["openapi.*%.json"] = "json.openapi",
    ["*%.snip"] = "vim",
    ["*%.nginx"] = "nginx",
    [".*nginx.*%.conf"] = "nginx",
    [".*nginx/.*/conf.*"] = "nginx",
    [".*/nginx/.*%.conf"] = "nginx",
    ["/srv/nginx/conf%.d/locations/.*"] = "nginx",
    [".*/playbooks/*.y*"] = "yaml.ansible",
    [".*compose.*.y*"] = "yaml.docker-compose",
    ["Caddyfile.*"] = "caddyfile",
    ["haproxy.*.c.*"] = "haproxy",
    [".*/templates/.*.yaml"] = "yaml.helm",
    [".*/templates/.*.tpl"] = "yaml.helm",
    [".*/helm/.*.yaml"] = "yaml.helm",
    [".*"] = {
      function(path, buf)
        lf.optimize_buffer(buf, path)
        local t = lf.is_large_file(buf, false, path)
        if t == lf.FILE_TYPE.LARGE_SIZE then
          return "largefile.size"
        end
        if t == lf.FILE_TYPE.READ_ONLY then
          return "largefile.readonly"
        end
        return nil
      end,
    },
  },
})
