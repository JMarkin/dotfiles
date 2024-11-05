{ pkgs, ... }:
{
  system.stateVersion = 5;
  environment.systemPackages = [
    pkgs.vim
  ];

  environment.shells = [ pkgs.fish ];
  users.users.kron.shell = pkgs.fish;
  environment.loginShell = pkgs.fish;

  documentation.enable = false;
  documentation.doc.enable = false;
  documentation.info.enable = false;
  documentation.man.enable = true;

  # Auto upgrade nix package and the daemon service.
  services.nix-daemon.enable = true;
  nix.package = pkgs.nixVersions.latest;
  programs.zsh.enable = true;
  programs.zsh.promptInit = "";
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

