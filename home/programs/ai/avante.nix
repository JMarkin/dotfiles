{ pkgs, ... }:
{
  home.file = {
    ".local/share/nvim/nix/avante.nvim/" = {
      recursive = true;
      source = pkgs.vimPlugins.avante-nvim;
    };
  };
}
