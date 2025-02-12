{ config, pkgs, lib, ... }:

{

  imports = [
    ./kron.nix
    ../programs/alacritty
    # ../programs/neovide.nix
  ];
  home.homeDirectory = "/Users/kron";



  home.packages = with pkgs; [
    docker
    docker-credential-helpers
    # lima
    colima
  ];

}

