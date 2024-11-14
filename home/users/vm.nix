{ config, pkgs, lib, ... }:

{

  home.homeDirectory = "/home/kron";

  home.packages = with pkgs; [
    # utils
    procps
    inotify-tools
  ];

  imports = [
    ./kron.nix
  ];
}
