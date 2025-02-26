{ config, lib, pkgs, ... }:

{
  programs.bat.enable = true;
  programs.bat.config = {
    theme = "bamboo";
  };
  programs.bat.themes = {
    bamboo = {
      src = pkgs.fetchFromGitHub {
        owner = "ribru17";
        repo = "bamboo.nvim";
        rev = "d100fc78184ba9365fc6a4988518652e792cf6ec";
        hash = "sha256-3lsc55BkG11UZoCbGSkB6RQ2H329LDvY+UHE6YXxCzs=";
      };
      file = "extras/bat/bamboo.tmTheme";
    };
  };
}
