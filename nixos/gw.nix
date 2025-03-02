{ config, lib, pkgs, ... }:

{
  imports =
    [
      ./hardware/gw.nix
      ./modules/common.nix
    ];

  boot.kernelParams = [
    "console=ttyS0"
    "console=tty1"
  ];

  boot.loader.grub.enable = true;
  boot.loader.grub.device = "/dev/vda";


  networking = {
    dhcpcd.enable = true;
    hostName = "nixos-gw";
    firewall = {
      enable = false;
    };
  };

  system.stateVersion = "25.05";
}

