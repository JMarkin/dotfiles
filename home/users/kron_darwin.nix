{ config, pkgs, lib, ... }:

{

  imports = [
    ./kron.nix

    ../programs/alacritty
    ../programs/neovide.nix
    ../programs/ai
  ];



  home.packages = with pkgs; [
    docker
    docker-credential-helpers
    colima
    dbeaver-bin
  ];

}

