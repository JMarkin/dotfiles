{ config, pkgs, ... }:
let

  nvim-spell-ru-utf8-dictionary = builtins.fetchurl {
    url = "http://ftp.gr.vim.org/pub/vim/runtime/spell/ru.utf-8.spl";
    sha256 = "sha256:0kf5vbk7lmwap1k4y4c1fm17myzbmjyzwz0arh5v6810ibbknbgb";
  };

in
{
  imports = [
    ./kulala.nix
    ./blink.nix
    ./treesitter.nix
  ];
  home.packages = with pkgs;
    [

      # builder
      lua51Packages.lua
      lua51Packages.luarocks

      # lsp
      bash-language-server

      # lsp features
      fswatch

      #tools
      nixpkgs-fmt
      fixjson
      codespell
    ];

  programs.neovim = {
    enable = true;
    # package = pkgs.neovim;
    vimAlias = true;
    viAlias = true;
    coc.enable = false;
    withNodeJs = true;
    defaultEditor = true;
    vimdiffAlias = true;
  };

  home.file = {
    ".config/nvim".source = config.lib.file.mkOutOfStoreSymlink "${config.home.homeDirectory}/.dotfiles/home/programs/neovim/nvim";

    ".local/share/nvim/site/spell/ru.utf-8.spl".source = nvim-spell-ru-utf8-dictionary;
  };

}
