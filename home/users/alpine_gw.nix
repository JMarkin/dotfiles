{ config, pkgs, lib, ... }:

{

  imports = [
    ./vm.nix
  ];

  home.packages = with pkgs; [
    vpn-slice
    openconnect
  ];
}
