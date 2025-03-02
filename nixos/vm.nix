# Edit this configuration file to define what should be installed on
# your system. Help is available in the configuration.nix(5) man page, on
# https://search.nixos.org/options and in the NixOS manual (`nixos-help`).

{ config, lib, pkgs, ... }:

{
  imports =
    [
      # Include the results of the hardware scan.
      ./hardware/vm.nix
      ./modules/common.nix
    ];

  virtualisation.docker.enable = true;
  boot.kernelParams = [
    "console=ttyS0"
    "console=tty1"
  ];

  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;

  networking = {
    dhcpcd.enable = true;
    hostName = "nixos";
    firewall = {
      enable = false;
    };
  };

  fileSystems."/projects" = {
    device = "projects";
    fsType = "virtiofs";
    options = [
      "rw"
      "noatime"
      "_netdev"
    ];
  };


  system.stateVersion = "25.05";
}

