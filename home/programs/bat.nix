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
        rev = "57e1bff1c0df29d7ec0071baf49210c48fc4a98b";
        hash = "sha256-HhRrap1JBiFMcwHkR77JGqvay777bp281G6+xE+IoW8=";
      };
      file = "extras/bat/bamboo.tmTheme";
    };
  };
}
