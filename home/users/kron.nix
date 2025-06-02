{ config, pkgs, lib, ... }:

let
  rllama = pkgs.buildGoModule {
    name = "rllama";
    src = pkgs.fetchFromGitHub {
      owner = "DonTizi";
      repo = "rlama";
      rev = "v0.1.36";
      hash = "sha256-SzrnpAkh+SMzF9xOAxZXondRulwPRUZYHrhe3rf06bA=";
    };
    doCheck = false;
    vendorHash = "sha256-GHmLCgL79BdGw/5zz50Y1kR/6JYNalvOj2zjIHQ9IF0=";
  };

in
{

  imports = [
    ./minsetup.nix
    ../programs/fish
    ../programs/neovim
    ../programs/direnv.nix
    ../programs/ai
  ];


  home.packages = with pkgs; [
    # utils
    jaq
    delta
    docker-compose
    dust
    tree-sitter
    createnv
    dotenv-linter
    kubectl
    k9s

    universal-ctags
    ptags

    ollama

    rustic
    rclone
  ];

  programs.fastfetch.enable = true;


}
