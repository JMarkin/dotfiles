# my fork
self: super: {
  pythonPackagesExtensions = super.pythonPackagesExtensions ++ [
    (
      pyself: pysuper: {
        jedi-language-server = pysuper.jedi-language-server.overridePythonAttrs
          (oldAttrs: {
            src = super.fetchFromGitHub
              {
                owner = "JMarkin";
                repo = "jedi-language-server";
                rev = "main";
                hash = "sha256-ODYn4GtkLC1GXUU4K9NhmOLzilGQ0s/2dykiHwTFvU0=";
              };
          });
      }
    )
  ];
}
