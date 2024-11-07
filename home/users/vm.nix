{ config, pkgs, lib, ... }:

{

  home.homeDirectory = "/Users/kron";

  home.packages = with pkgs; [
    # utils
    procps
    inotify-tools
  ];

  imports = [
    ./kron.nix
  ];
}
