{ config, pkgs, lib, ... }:

{

  imports = [
    ./minsetup.nix
    ../programs/fish
    ../programs/neovim
    ../programs/direnv.nix
    ../programs/nix-flake-templates
  ];


  home.packages = with pkgs; [
    # utils
    jaq
    rsync
    delta
    universal-ctags
    docker-compose
    dust
    tree-sitter
    rustic
    rclone
    ptags
    gnumake
    hyperfine
    createnv
    dotenv-linter
    kubectl
    k9s
    # nur.repos.dustinblackman.oatmeal
    # cgrc

    # networking tools
    mtr
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

    # for rustc
    iconv
    libiconv

    # llm
    # vectorcode

  ];

  programs.fastfetch.enable = true;


}
