{ config, lib, pkgs, ... }:

{
  home.packages = [
    pkgs.glances
  ];
}
