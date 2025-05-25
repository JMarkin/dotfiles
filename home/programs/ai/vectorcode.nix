{ pkgs, ... }:
{
  home.packages = [
    pkgs.vectorcode
  ];

  home.file = {
    ".local/share/nvim/nix/VectorCode/" = {
      recursive = true;
      source = pkgs.vectorcode.src;
    };
  };
}
