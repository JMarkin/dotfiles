{ pkgs, ... }:
let
  kulala-nvim = pkgs.fetchFromGitHub {
    owner = "mistweaverco";
    repo = "kulala.nvim";
    rev = "v5.2.1";
    hash = "sha256-kTA2EtLwJbwlgFFWekrQn2B9jnqW8FREqxpvdWTZA+4=";
  };

  # kulala-lsp = pkgs.buildNpmPackage
  #   rec {
  #     pname = "kulala-ls";
  #     version = "1.9.0";
  #
  #     src = pkgs.fetchFromGitHub {
  #       owner = "mistweaverco";
  #       repo = "kulala-ls";
  #       rev = "v${version}";
  #       hash = "sha256-We7d6if++n8Y0eouY3I9hbb5iJ+YyaPyFSvu6Ff5U0U=";
  #     };
  #
  #     npmDepsHash = "sha256-/6JZYsIYDJHS/8TOPjtR/SrRbzTbL43X0g/tPIn2YfQ=";
  #   };

  # kulala-fmt = pkgs.buildNpmPackage
  #   rec {
  #     pname = "kulala-fmt";
  #     version = "2.10.0";
  #
  #     src = pkgs.fetchFromGitHub {
  #       owner = "mistweaverco";
  #       repo = "kulala-fmt";
  #       rev = "v${version}";
  #       hash = "sha256-ICxuNVFHMP8qjOMvWSuestsLWBU3bDVMd1D2TCaugNA=";
  #     };
  #
  #     npmDepsHash = "";
  #   };

in
{
  home.packages = with pkgs; [
    kulala-nvim
    # kulala-lsp
    # kulala-fmt

    grpcurl
    websocat
    jq
  ];

  home.file = {
    ".local/share/nvim/nix/kulala.nvim/" = {
      recursive = true;
      source = kulala-nvim;
    };
  };

}
