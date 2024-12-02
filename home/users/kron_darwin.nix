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
    floorp-bin
  ];

  programs.firefox = {
    enable = true;

    # IMPORTANT: use a package provided by the overlay (ends with `-bin`)
    # see overlay.nix for all possible packages
    package = pkgs.floorp-bin; # Or use pkgs.librewolf for Librewolf or pkgs.floorp-bin for Floorp
  };

}

