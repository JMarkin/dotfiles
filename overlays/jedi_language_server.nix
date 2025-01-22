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
                hash = "sha256-7kudUIjX+jrQ06ko56gTM3GF4XPQErqJ3rCNL4xTYls=";
              };
          });
      }
    )
  ];
}
