{ config, pkgs, lib, ... }:

{

  home.homeDirectory = "/home/kron";

  home.packages = with pkgs; [
    # utils
    procps
    inotify-tools
  ];

  imports = [
    ./kron.nix
  ];

  home.sessionVariables.OLLAMA_HOST = "192.168.88.15";
  home.sessionVariables.OLLAMA_PORT = "11434";
  home.sessionVariables.OLLAMA_URL = "http://192.168.88.15:11434";

}
