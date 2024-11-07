self: super: {

  cgrc = super.rustPlatform.buildRustPackage rec {
    pname = "cgrc";
    version = "2.0.5";

    src = super.fetchFromGitHub {
      owner = "carlonluca";
      repo = "cgrc";
      rev = "v2.0.5";
      hash = "sha256-aJpQzyzN5mLHnrzBmXA6YhHEzE/aIDtX0r2Dv/E0OCU=";
    };
    sourceRoot = "${src.name}/cgrc-rust";

    cargoHash = "sha256-2rKI3NTunmSKbFdDJDVsmy/kp5U3ZZ9cIxtqPvbee9A=";

    doCheck = false;

    meta = {
      description = "CGRC - Generic Colorizer";
      homepage = "https://github.com/carlonluca/cgrc/blob/master/cgrc-rust";
      changelog = "";
      mainProgram = "cgrc";
    };
  };
}

