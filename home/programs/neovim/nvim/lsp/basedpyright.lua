return {
  filetypes = { "python", "python.django", "django" },
  settings = {
    basedpyright = {
      disableOrganizeImports = true,
      analysis = {
        autoImportCompletions = false,
        typeCheckingMode = "off",
        diagnosticMode = "openFilesOnly",
      },
    },
  },
}
