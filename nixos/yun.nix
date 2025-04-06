{ config, lib, pkgs, ... }:

{
  imports =
    [
      ./hardware/yun.nix
      ./modules/common.nix
    ];

  networking.hostName = "yun-nixos";

  boot.loader.grub = {
    # no need to set devices, disko will add all devices that have a EF02 partition to the list already
    # devices = [ ];
    efiSupport = true;
    efiInstallAsRemovable = true;
  };

  boot.loader.grub.devices = "/dev/sda2";

  networking.useDHCP = lib.mkForce false;

  networking = {
    interfaces.ens192 = {
      ipv6.addresses = [{
        address = "2a0d:6c2:6:282::";
        prefixLength = 47;
      }];
      ipv4.addresses = [{
        address = "193.46.218.44";
        prefixLength = 24;
      }];
    };
    defaultGateway = {
      address = "193.46.218.1";
      interface = "ens192";
    };
    defaultGateway6 = {
      address = "fe80::1";
      interface = "2a0d:6c2:6::1";
    };
  };


  system.stateVersion = "25.05";
}

