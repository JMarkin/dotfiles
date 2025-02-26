{ config, pkgs, lib, ... }:

{

  imports = [
    ./kron.nix
    # ../programs/alacritty
    ../programs/ghostty
    ../programs/neovide.nix
  ];
  home.homeDirectory = "/Users/kron";



  home.packages = with pkgs; [
    docker
    docker-credential-helpers
    colima
    dbeaver-bin

    # st
  ];

}

