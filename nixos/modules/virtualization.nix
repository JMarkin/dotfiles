{ pkgs, ... }:
{

  environment.systemPackages = with pkgs; [
    nixos-shell
    virt-manager
    virt-viewer
    spice
    spice-gtk
    spice-protocol
    win-virtio
    win-spice
    gnome.adwaita-icon-theme
  ];

  users.users."kron".extraGroups = [ "libvirtd" ];

  virtualisation = {
    spiceUSBRedirection.enable = true;
    libvirtd = {
      enable = true;
      qemu = {
        swtpm.enable = true;
        ovmf = {
          enable = true;
          packages = [ pkgs.OVMFFull.fd ];
        };
      };
    };
  };
  services.spice-vdagentd.enable = true;
}
