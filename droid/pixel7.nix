{ config, lib, pkgs, ... }:

{
  imports =
    [
      ../nixos/modules/common.nix
    ];

  virtualisation.docker.enable = true;
  boot.kernelParams = [
    "console=ttyS0"
    "console=tty1"
  ];

  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;
  system.stateVersion = "24.05";
  environment.etcBackupExtension = ".bak";

  networking = {
    dhcpcd.enable = true;
    hostName = "nixos";
    firewall = {
      enable = false;
    };
  };

  # Configure home-manager
  home-manager = {
    config = ../home/users/vm.nix;
    backupFileExtension = "hm-bak";
    useGlobalPkgs = true;
  };
}
