{ config, pkgs, lib, ... }:

{

  imports = [
    ./kron.nix

    ../programs/ghostty
    ../programs/neovide.nix
  ];



  home.packages = with pkgs; [
    docker
    docker-credential-helpers
    colima
    dbeaver-bin

    # st
  ];

}

