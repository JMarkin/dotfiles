{ pkgs, ... }:
let
  version = "0.6.3";
  src = pkgs.fetchFromGitHub {
    owner = "Davidyz";
    repo = "VectorCode";
    tag = version;
    sha256 = "sha256-I6YuX09a2C9Ik1uO1Z78ACIPgzhJ9jl6ixVDSW8+Awo=";
  };
  vectorcode = with pkgs.python3Packages; buildPythonPackage {
    pname = "vectorcode";
    version = version;
    format = "pyproject";

    src = src;
    # doCheck = false;
    nativeBuildInputs = [ pdm-backend ];
    dependencies = [
      chromadb
      numpy
      sentence-transformers
      tabulate
      shtab
      psutil
      httpx
      pathspec
      pygls
      lsprotocol
      tree-sitter
      tree-sitter-language-pack
      pygments
      pydantic
      colorlog
    ];
  };
in
{
  home.packages = [
    vectorcode
  ];

  home.file = {
    ".local/share/nvim/nix/VectorCode/" = {
      recursive = true;
      source = src;
    };
  };
}
