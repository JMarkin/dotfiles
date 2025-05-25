{ pkgs, ... }:
{

 
  programs.neovim.plugins = with pkgs.vimPlugins; [
    blink-cmp
    blink-pairs
    # blink-cmp-avante
    blink-compat
  ];

  home.file = with pkgs.vimPlugins; {
    ".local/share/nvim/nix/blink.cmp/" = {
      recursive = true;
      source = blink-cmp;
    };
    ".local/share/nvim/nix/blink.pairs/" = {
      recursive = true;
      source = blink-pairs;
    };
    # ".local/share/nvim/nix/blink-cmp-avante/" = {
    #   recursive = true;
    #   source = blink-cmp-avante;
    # };
    ".local/share/nvim/nix/blink.compat/" = {
      recursive = true;
      source = blink-compat;
    };
  };

}
