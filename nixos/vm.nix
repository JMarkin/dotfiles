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
      ./modules/wg.nix
    ];

  virtualisation.docker.enable = true;
  boot.kernelParams = [
    "console=ttyS0"
    "console=tty1"
  ];

  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;
  systemd.services.nix-daemon.environment.TMPDIR = "/var/tmp/nix-daemon";

  boot.tmpOnTmpfs = true;

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

  fileSystems."/var/lib/docker" = {
    device = "/dev/vdb1";
    fsType = "ext4";
    options = [
      "noatime"
      "defaults"
    ];
  };


  system.stateVersion = "25.05";
}

