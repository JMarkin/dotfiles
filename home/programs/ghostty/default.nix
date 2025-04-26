{ config, lib, pkgs, ... }:

{
  programs.ghostty = {
    enable = true;
    package = null;
    settings = {
      theme = "light:bamboo_light,dark:bamboo";
      initial-command = "${pkgs.bash}/bin/bash";
      adjust-cell-height = "10%";
      copy-on-select = true;
      font-family = "JetBrainsMonoNL Nerd Font Mono";
      font-size = 13;
      font-thicken = true;
      cursor-style = "block";
      mouse-hide-while-typing = true;
      macos-non-native-fullscreen = "visible-menu";
      macos-option-as-alt = true;
      # macos-titlebar-style = "hidden";
      window-decoration = true;
      window-padding-y = 0;
      window-padding-x = 0;
      window-padding-color = "extend";
      window-padding-balance = true;
      window-save-state = "always";
      shell-integration-features = "no-cursor";
      quit-after-last-window-closed = true;
      confirm-close-surface = false;

      keybind = [
        "super+one=text:\\x02\\x31"
        "super+two=text:\\x02\\x32"
        "super+three=text:\\x02\\x33"
        "super+four=text:\\x02\\x34"
        "super+five=text:\\x02\\x35"
        "super+six=text:\\x02\\x36"
        "super+seven=text:\\x02\\x37"
        "super+eight=text:\\x02\\x38"
        "super+nine=text:\\x02\\x39"
        "super+t=text:\\x02\\x63"
        "super+w=text:\\x02\\x78"
        "super+d=text:\\x02\\x76"
        "super+shift+d=text:\\x02\\x73"
        "ctrl+q=close_window"

        # moving
        "ctrl+h=text:\\x02\\x08"
        "ctrl+j=text:\\x02\\x0a"
        "ctrl+k=text:\\x02\\x0b"
        "ctrl+l=text:\\x02\\x0c"
      ];
    };
  };

  home.file = {
    "./.config/ghostty/themes/bamboo".text = builtins.readFile
      (pkgs.fetchFromGitHub
        {
          owner = "ribru17";
          repo = "bamboo.nvim";
          rev = "d100fc78184ba9365fc6a4988518652e792cf6ec";
          hash = "sha256-3lsc55BkG11UZoCbGSkB6RQ2H329LDvY+UHE6YXxCzs=";
        } + "/extras/ghostty/bamboo");

    "./.config/ghostty/themes/bamboo_light".text = builtins.readFile
      (pkgs.fetchFromGitHub
        {
          owner = "ribru17";
          repo = "bamboo.nvim";
          rev = "d100fc78184ba9365fc6a4988518652e792cf6ec";
          hash = "sha256-3lsc55BkG11UZoCbGSkB6RQ2H329LDvY+UHE6YXxCzs=";
        } + "/extras/ghostty/bamboo_light");
  };
}
