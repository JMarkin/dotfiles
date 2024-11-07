{ config, pkgs, lib, ... }:

{
  home.username = "kron";

  home.stateVersion = "24.05";

  programs.fastfetch.enable = true;
  programs.ripgrep.enable = true;
  programs.fd.enable = true;
  programs.fzf.enable = true;
  programs.zoxide.enable = true;
  programs.eza.enable = true;

  imports = [
    ../programs/git
    ../programs/bash.nix
    ../programs/tmux.nix
    ../programs/fish
    ../programs/bat.nix
    ../programs/htop.nix
    ../programs/neovim
    ../programs/direnv.nix
    ../programs/gpg.nix
    ../programs/starship.nix
    ../programs/nix-flake-templates
  ];

  home.file = {
    ".config/openssl.cnf".source = ../legacyconfig/openssl.cnf;
  };

  home.sessionVariables = {
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
  };

  programs.home-manager.enable = true;

}
