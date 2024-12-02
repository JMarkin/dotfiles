{ pkgs, lib, ... }:
{
  system.stateVersion = 5;
  system.activationScripts.postUserActivation.text = ''
    # activateSettings -u will reload the settings from the database and apply them to the current session,
    # so we do not need to logout and login again to make the changes take effect.
    /System/Library/PrivateFrameworks/SystemAdministration.framework/Resources/activateSettings -u
  '';

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

  nix.gc = {
    automatic = lib.mkDefault true;
    options = lib.mkDefault "--delete-older-than 7d";
  };
  nix.settings = {
    auto-optimise-store = false;
  };

  # fonts.fontDir.enable = true;
  fonts.packages = [
    pkgs.nerd-fonts.jetbrains-mono
  ];


  # postgres for testings

  system.activationScripts.preActivation = {
    enable = true;
    text = ''
      if [ ! -d "/var/lib/postgresql/" ]; then
        echo "creating PostgreSQL data directory..."
        sudo mkdir -m 750 -p /var/lib/postgresql/
        chown -R kron:staff /var/lib/postgresql/
      fi
    '';
  };

  services.postgresql.initdbArgs = [ "-U kron" "--pgdata=/var/lib/postgresql/15" "--auth=trust" "--no-locale" "--encoding=UTF8" ];
  services.postgresql.package = pkgs.postgresql_15;
  services.postgresql.enable = true;

  launchd.user.agents.postgresql.serviceConfig = {
    StandardErrorPath = "/tmp/postgres.error.log";
    StandardOutPath = "/tmp/postgres.log";
  };
}

