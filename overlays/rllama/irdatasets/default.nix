{ pkgs, ... }:
let
  packageOverrides = pkgs.callPackage ./python-packages.nix { };
  python = pkgs.python3.override { inherit packageOverrides; };
  pythonWithPackages = python.withPackages (ps: [ 
    ps.beautifulsoup4
    ps.inscriptis
    ps.lxml
    ps.numpy
    ps.pyyaml
    ps.requests
    ps.tqdm
    ps.trec-car-tools
    ps.lz4
    ps.warc3-wet
    ps.warc3-wet-clueweb09
    ps.zlib-state
    ps.ijson
    ps.unlzw3
    ps.pyarrow
  ]);
in
with pkgs.python3Packages; buildPythonPackage rec {
  pname = "ir_datasets";
  version = "0.5.10";
  format = "pyproject";

  src = fetchPypi {
    inherit version;
    inherit pname;
    sha256 = "sha256-/vq+NSq0vxT5tfIk3xfE5hBTvm9ThAs1sPf1FFKz2ls=";
  };
  doCheck = false;
  nativeBuildInputs = [ pythonWithPackages ];
}
