{ pkgs, lib, ... }:
{
  system.stateVersion = 5;
  system.activationScripts.postUserActivation.text = ''
    # activateSettings -u will reload the settings from the database and apply them to the current session,
    # so we do not need to logout and login again to make the changes take effect.
    /System/Library/PrivateFrameworks/SystemAdministration.framework/Resources/activateSettings -u
  '';

  environment.systemPackages = with pkgs; [
    vim
    home-manager
  ];



  programs.fish.enable = true;
  environment.shells = [ pkgs.fish ];
  users.users.kron.shell = pkgs.fish;

  documentation.enable = false;
  documentation.doc.enable = false;
  documentation.info.enable = false;
  documentation.man.enable = true;

  # Auto upgrade nix package and the daemon service.
  nix.enable = true;
  nix.package = pkgs.nixVersions.latest;
  nix.settings.trusted-users = [ "root" "kron" ];
  nix.extraOptions = ''
    auto-optimise-store = true
    extra-platforms = aarch64-darwin x86_64-darwin
    experimental-features = nix-command flakes
  '';
  nix.optimise.automatic = true;

  nix.gc = {
    automatic = lib.mkDefault true;
    interval.Weekday = 0;
    options = lib.mkDefault "--delete-older-than 7d";
  };

  # fonts.fontDir.enable = true;
  fonts.packages = [
    pkgs.nerd-fonts.jetbrains-mono
  ];

  home-manager.backupFileExtension = "old";

}

