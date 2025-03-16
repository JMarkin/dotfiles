self: super: {
  vectorcode = with super.python3Packages; buildPythonPackage rec {
    pname = "vectorcode";
    version = "0.4.11";
    format = "pyproject";

    src = fetchPypi {
      inherit version;
      inherit pname;
      sha256 = "sha256-fcB8Xg/i+c104yVT+HAGrtxMwD84qPS8xwbBuHDo4X8=";
    };
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
    ];
  };
}
