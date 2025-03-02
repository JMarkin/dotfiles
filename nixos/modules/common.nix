{ pkgs, ... }:
{

  nix.extraOptions = ''
    experimental-features = nix-command flakes
  '';
  environment.variables = { EDITOR = "nvim"; };
  environment.systemPackages = with pkgs; [
    git
    wget
    curl
    tmux
    neovim
    home-manager
    wireguard-tools
  ];
  programs.neovim = {
    defaultEditor = true;
    enable = true;
    viAlias = true;
    vimAlias = true;
    configure = {
      customRC = ''
        set colorcolumn=+1
        set cursorlineopt=both
        set cursorline
        set splitright
        set splitbelow
        set number
        set relativenumber
        set virtualedit=block
        set guicursor=a:block
        set scrolloff=4
        set sidescrolloff=8
        set nowrap
        set linebreak
        set breakindent
        set syntax
        set mouse=a
        set fileencoding=utf-8
        set encoding=utf-8
        set hidden
        set noautochdir
        set bs=indent,eol,start
        set background=dark
        set tabstop=4
        set softtabstop=4
        set shiftwidth=4
        set expandtab
        set smartindent
        set autoindent
      '';
    };
  };
  services.avahi = {
    enable = true;
    nssmdns4 = true;
    openFirewall = true;
  };

  programs.git = {
    enable = true;
    config = {
      http = {
        "https://git.jmarkin.ru" = {
          sslVerify = false;
        };
      };
    };
  };


  imports = [
    ./ssh.nix
    ./user.nix
    ./fonts.nix
    ./locale.nix
    ./nix-options.nix
  ];
}
