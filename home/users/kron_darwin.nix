{ config, pkgs, lib, ... }:

{

  imports = [
    ./kron.nix
  ];
  home.homeDirectory = "/Users/kron";


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
    wget

    # utils
    procps
    jaq
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
    gnumake
    # cgrc

    # networking tools
    mtr
    iperf3
    dnsutils
    socat
    nmap

    # lang
    llvm
    clang
    mold
    rustc
    cargo
    go
    nodejs_22
  ];

}

