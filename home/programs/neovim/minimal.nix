{ ... }:

{
  programs.neovim = {
    enable = true;
    vimAlias = true;
    viAlias = true;
    coc.enable = false;
    defaultEditor = true;
    vimdiffAlias = true;
    extraLuaConfig = (builtins.readFile ./nvim/lua/common.lua);
  };

  home.file = {
    ".config/nvim/colors" = {
      source = ./nvim/colors;
      recursive = true;
    };
  };
}
