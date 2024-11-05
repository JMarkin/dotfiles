{ config, pkgs, lib, ... }:

{
  home.username = "kron";
  home.homeDirectory = "/home/kron";
  
  home.stateVersion = "24.05";

  home.packages = with pkgs; [
    neofetch

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
    
    # utils
    procps
    jaq
    iotop
    htop
    ethtool
    pciutils
    usbutils
    rsync
    delta
    sccache
    universal-ctags
    man
    docker-compose
    dust
    tree-sitter
    rustic-rs
    ptags
    mold
    gnumake
    inotify-tools

    # networking tools
    mtr
    iperf3
    dnsutils
    socat
    nmap

    # lang
    llvm_18
    rustc
    cargo
    go
    nodejs_22
  ];

  programs.ripgrep.enable = true;
  programs.fd.enable = true;
  programs.fzf.enable = true;
  programs.yazi.enable = true;
  programs.zoxide.enable = true;
  programs.eza.enable = true;
  programs.bat.enable = true;

  imports = [
    ../programs/git
    ../programs/bash.nix
    ../programs/tmux.nix
    ../programs/fish
    ../programs/neovim
    ../programs/direnv.nix
    ../programs/gpg.nix
    ../programs/starship.nix
  ];

  home.file = {
    ".config/openssl.cnf".source = ./openssl.cnf;
  };

  home.sessionVariables = {
    EDITOR = "nvim";
    VISUAL = "nvim";
    PAGER = "bat";
    MANPAGER = "nvim +Man!";
    LS_COLORS = (builtins.readFile ./ls_colors);
    CLICOLOR = 1;
    PYTHONPYCACHEPREFIX = "/tmp/cpython";
    OPENSSL_CONF = "${config.home.homeDirectory}/.config/openssl.cnf";

    SCARF_ANALYTICS="false";
    DOTNET_CLI_TELEMETRY_OPTOUT="1";

    FZF_DEFAULT_OPTS="--bind=shift-tab:up,tab:down";
  };

  programs.home-manager.enable = true;

}
