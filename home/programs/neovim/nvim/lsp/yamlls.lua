return {
  filetypes = { "yaml", "yaml.openapi", "yaml.helm", "yaml.ansible" },
  settings = {
    yaml = {
      schemaStore = {
        enable = false,
      },
      schemas = require("schemastore").yaml.schemas(),
    },
    redhat = {
      telemetry = {
        enabled = false,
      },
    },
  },
}
