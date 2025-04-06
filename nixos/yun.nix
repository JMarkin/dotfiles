{ config, lib, pkgs, ... }:

{
  imports =
    [
      ./hardware/yun.nix
      ./modules/common.nix
    ];

  networking.hostName = "yun-nixos";

  boot.loader.grub = {
    enable = true;
    device = "/dev/sda";
    # no need to set devices, disko will add all devices that have a EF02 partition to the list already
    # devices = [ ];
    efiSupport = true;
    efiInstallAsRemovable = true;
  };


  networking.useDHCP = lib.mkForce false;

  networking = {
    nameservers = [ "8.8.8.8" "2001:4860:4860::8888" ];

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
      address = "2a0d:6c2:6::1";
      interface = "ens192";
    };
  };


  system.stateVersion = "25.05";
}

