{ pkgs, ... }:

{
  imports =
    [
      ./hardware.nix
      ./network.nix
      ./boot.nix
      ./disk.nix
      ../../nixos/modules/common.nix
    ];

  environment.systemPackages = with pkgs; [
    rsync
    curl
    gitMinimal
    iperf3
    dnsutils
    termshark
    mtr
    ps
    btop
    cfspeedtest
  ];

  system.stateVersion = "25.05";
}

