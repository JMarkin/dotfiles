{ config, lib, pkgs, ... }:

{
  home.packages = [
    pkgs.neovide
  ];
  programs.neovide = {
    enable = true;
    settings = {
      neovim-bin = "${pkgs.neovim}/bin/nvim";
      frame = "buttonless";
      grid = "300x60";
      tabs = false;
      fork = true;

      font = {
        normal = [ "JetBrainsMonoNL Nerd Font Mono" ];
        size = 13;
      };
    };
  };
}

