{ config, pkgs, lib, ... }:

{

  imports = [
    ./minsetup.nix
    ../programs/fish
    ../programs/neovim
    ../programs/direnv.nix
    ../programs/nix-flake-templates
  ];


  home.packages = with pkgs; [
    # utils
    jaq
    rsync
    delta
    universal-ctags
    docker-compose
    dust
    tree-sitter
    rustic
    rclone
    ptags
    createnv
    dotenv-linter
    kubectl
    k9s

    # networking tools
    mtr
    socat
    nmap

    ollama

  ];

  programs.fastfetch.enable = true;


}
