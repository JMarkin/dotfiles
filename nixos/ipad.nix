{ ... }:

{
  imports =
    [
      ./modules/common.nix
      ./modules/docker.nix
      ./modules/fonts.nix
      ./modules/desktop/services.nix
      ./modules/zram.nix
    ];

  virtualisation.diskSize = 20 * 1024;
  boot.kernelParams = [
    "console=tty0"
  ];

  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;

  networking = {
    dhcpcd.enable = true;
    hostName = "nixos-ipad";
    firewall = {
      enable = false;
    };
  };

  system.stateVersion = "25.05";
}

