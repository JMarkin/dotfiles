{ config, pkgs, lib, ... }:

{

  imports = [
    ./kron.nix
    ../programs/alacritty
  ];
  home.homeDirectory = "/Users/kron";



  home.packages = with pkgs; [
    neovide
    postgresql_15

    alacritty

    docker
    docker-credential-helpers
    lima
  ];

}

