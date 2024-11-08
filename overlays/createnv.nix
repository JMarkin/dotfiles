self: super: {

  createnv = super.rustPlatform.buildRustPackage {
    pname = "createnv";
    version = "0.0.3";

    src = super.fetchFromGitHub {
      owner = "cuducos";
      repo = "createnv";
      rev = "v0.0.3";
      hash = "sha256-acB9ZkD4wzK1lhxI9RcpkVqEUn05z33O8MoSQU5myQ8=";
    };
    cargoHash = "sha256-RrW9cncSbuo7AXJTG+yJ3UfA2h9MUQ1mXc/vnTWoz/4=";

    doCheck = false;

    meta = {
      description = "createnv";
      homepage = "https://github.com/cuducos/createnv";
      changelog = "";
      mainProgram = "createnv";
    };
  };
}


