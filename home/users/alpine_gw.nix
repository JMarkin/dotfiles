{ config, pkgs, lib, ... }:

{

  imports = [
    ./vm.nix
  ];

  home.packages = with pkgs; [
    vpn-slice
    openconnect
  ];

  home.file = {
    ".config/vpn/template.fish".source = ../legacyconfig/vpn/template.fish;
  };
}
