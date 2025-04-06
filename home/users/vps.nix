{ config, pkgs, lib, ... }:

{

  imports = [
    ./minsetup.nix
    ../programs/fish
    ../programs/neovim
    ../programs/direnv.nix
  ];


  home.packages = with pkgs; [
    # utils
    jaq
    rsync
    delta
    rustic
    rclone

    # networking tools
    mtr
    socat
    nmap

  ];

  programs.fastfetch.enable = true;


}
