{ pkgs, ... }:

{

  environment.systemPackages = with pkgs; [
    rustic
    rclone
    rsync
  ];

  home.files.".config/rustic.toml".text = /*toml*/''
      [repository]
      repository = "rclone:yandex:backups/wireguard"
      cache-dir = "/var/cache/rustic"

      [[backup.sources]]
      source = "/etc/wireguard_ui"

      [[backup.sources]]
      source = "/etc/wireguard"

# forget options
      [forget]
      keep-within-daily = "2 days"
      keep-monthly = 5
      keep-yearly = 2
    '';
}
