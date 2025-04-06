{ config, lib, pkgs, ... }:

{
  imports =
    [
      ./hardware/yun.nix
      ./modules/common.nix
    ];

  networking.hostName = "yun-nixos";

  system.stateVersion = "25.05";
}

