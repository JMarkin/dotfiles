# my fork
self: super: {
  vectorcode = with super.python3Packages; buildPythonPackage rec {
    pname = "vectorcode";
    version = "0.4.5";
    format = "pyproject";

    src = fetchPypi {
      inherit version;
      inherit pname;
      sha256 = "sha256-gzwkKlrc95zg0j7RerG+PHkrzeXmsnrYY6DiKNSCX0E=";
    };
    doCheck = false;
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
    ];
  };
}
