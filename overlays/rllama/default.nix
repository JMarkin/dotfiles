
self: pkgs: {

  ir-datasets = pkgs.callPackage ./irdatasets { };

  FlagEmbedding = with pkgs.python3Packages; buildPythonPackage rec {
    pname = "FlagEmbedding";
    version = "1.0.6";

    src = fetchPypi {
      inherit version;
      inherit pname;
      sha256 = "sha256-vMgSPEr9c+Ub/d0mtfpGIvTIzPRGSYEeRIvYF/3A0Tg=";
    };
    doCheck = false;
    dependencies = [
      torch
      transformers
      datasets
      accelerate
      sentence-transformers
      peft
      ir-datasets
      sentencepiece
      protobuf
    ];
  };
}
