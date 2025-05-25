return {
  settings = {
    checkOnSave = true,
    completion = {
      autoimport = {
        enable = false,
      },
    },
    procMacro = {
      enable = true,
    },
    files = {
      excludeDirs = {
        ".direnv",
        "_build",
        ".dart_tool",
        ".flatpak-builder",
        ".git",
        ".gitlab",
        ".gitlab-ci",
        ".gradle",
        ".idea",
        ".next",
        ".project",
        ".scannerwork",
        ".settings",
        ".venv",
        "archetype-resources",
        "bin",
        "hooks",
        "node_modules",
        "po",
        "screenshots",
        "target",
      },
    },
  },
}
