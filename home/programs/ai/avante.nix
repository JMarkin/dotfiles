{ pkgs, ... }:
{
  programs.neovim.plugins = [ pkgs.vimPlugins.avante-nvim ];
  home.file = {
    ".local/share/nvim/nix/avante.nvim/" = {
      recursive = true;
      source = pkgs.vimPlugins.avante-nvim;
    };
  };
}
