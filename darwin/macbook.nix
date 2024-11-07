{ pkgs, ... }:
{
  system.stateVersion = 5;
  environment.systemPackages = [
    pkgs.vim
    pkgs.home-manager
  ];


  programs.fish.enable = true;
  environment.shells = [ pkgs.fish ];
  users.users.kron.shell = pkgs.fish;

  documentation.enable = false;
  documentation.doc.enable = false;
  documentation.info.enable = false;
  documentation.man.enable = true;

  # Auto upgrade nix package and the daemon service.
  services.nix-daemon.enable = true;
  nix.package = pkgs.nixVersions.latest;
  nix.settings.trusted-users = [ "root" "kron" ];
  nix.extraOptions = ''
    extra-platforms = aarch64-darwin x86_64-darwin
    experimental-features = nix-command flakes
  '';

  # fonts.fontDir.enable = true;
  fonts.packages = [
    pkgs.jetbrains-mono
    (pkgs.nerdfonts.override { fonts = [ "JetBrainsMono" ]; })
  ];

}

