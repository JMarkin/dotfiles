{ pkgs, ... }:
{
  services.openssh = {
    enable = true;
    ports = [ 324 ];
    settings = {
      X11Forwarding = true;
      PermitRootLogin = "no";
      PasswordAuthentication = false;
    };
  };
  programs.ssh.extraConfig = ''
    IPQoS none
  '';
  programs.mosh.enable = true;

  systemd.services.sshd.wantedBy = pkgs.lib.mkForce [ "multi-user.target" ];
}
