{ ... }:

{
  imports =
    [
      ./hardware/vm.nix
      ./modules/common.nix
      ./modules/wg.nix
      ./modules/virtualization.nix
      ./modules/docker.nix
    ];

  boot.kernelParams = [
    "console=ttyS0"
    "console=tty1"
  ];

  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;
  systemd.services.nix-daemon.environment.TMPDIR = "/var/tmp/nix-daemon";

  boot.tmp.useTmpfs = true;

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

  fileSystems."/opt" = {
    device = "opt";
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

  fileSystems."/var/tmp/nix-daemon" = {
    device = "/dev/vdc1";
    fsType = "ext4";
    options = [
      "noatime"
      "defaults"
    ];
  };

  fileSystems."/nix" = {
    device = "/dev/vdc2";
    fsType = "ext4";
    neededForBoot = true;
    options = [ "noatime" ];
  };

  boot.kernel.sysctl = {
    "fs.inotify.max_user_watches" = 524288;
    "fs.file-max" = 2097152;
  };
  systemd.extraConfig = "DefaultLimitNOFILE=1024:1048576";


  system.stateVersion = "25.05";
}

