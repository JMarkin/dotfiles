{ config, pkgs, lib, ... }:

{

  programs.home-manager.enable = true;
  home.activation.report-changes = config.lib.dag.entryAnywhere ''
    ${pkgs.nvd}/bin/nvd --nix-bin-dir=${pkgs.nix}/bin diff $oldGenPath $newGenPath
  '';

  home.username = "kron";

  home.stateVersion = "25.05";


  home.homeDirectory = "/home/kron";

  home.packages = with pkgs; [
    zip
    xz
    unzip
    p7zip
    gnused
    gnutar
    gawk
    zstd
    gnupg
    pigz
    curl
    man
    ps
    iperf3
    dnsutils
    termshark

    neovim
  ];

  programs.ripgrep.enable = true;
  programs.fd.enable = true;
  programs.fzf.enable = true;
  programs.zoxide.enable = true;
  programs.eza.enable = true;
  programs.btop.enable = true;

  programs.neovim = {
    enable = true;
    vimAlias = true;
    viAlias = true;
    coc.enable = false;
    defaultEditor = true;
    vimdiffAlias = true;
    extraLuaConfig = (builtins.readFile ../programs/neovim/nvim/lua/common.lua);
  };

  home.file = {
    ".config/nvim/colors" = {
      source = ../programs/neovim/nvim/colors;
      recursive = true;
    };
    ".config/openssl.cnf".source = ../legacyconfig/openssl.cnf;
  };


  imports = [
    ../programs/git
    ../programs/bash.nix
    ../programs/tmux.nix
    ../programs/bat.nix
    ../programs/gpg.nix
    ../programs/starship.nix
  ];

  home.sessionVariables = {
    NIX_PATH = "${config.home.homeDirectory}/.shells:nixpkgs=flake:nixpkgs$\{NIX_PATH:+:$NIX_PATH}";
    EDITOR = "nvim";
    VISUAL = "nvim";
    PAGER = "bat";
    MANPAGER = "nvim +Man!";
    LS_COLORS = (builtins.readFile ../legacyconfig/ls_colors);
    CLICOLOR = 1;
    PYTHONPYCACHEPREFIX = "/tmp/cpython";
    OPENSSL_CONF = "${config.home.homeDirectory}/.config/openssl.cnf";

    SCARF_ANALYTICS = "false";
    DOTNET_CLI_TELEMETRY_OPTOUT = "1";

    FZF_DEFAULT_OPTS = "--bind=shift-tab:up,tab:down";
    LIBRARY_PATH = ''${lib.makeLibraryPath [pkgs.libiconv]}''${LIBRARY_PATH:+:$LIBRARY_PATH}'';
  };
}
