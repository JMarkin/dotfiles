{ config, lib, pkgs, ... }:

{
  home.packages = with pkgs; [
    alacritty
  ];
  programs.alacritty = {
    enable = true;
    settings = {
      general = {
        import = [
          "~/.config/alacritty/keys.toml"
          "~/.config/alacritty/bamboo.toml"
        ];
      };
      cursor = {
        blink_interval = 500;
        unfocused_hollow = false;
        style = {
          blinking = "Always";
          shape = "Block";
        };
      };
      env = {
        TERM = "xterm-256color";
      };
      mouse = {
        hide_when_typing = true;
        bindings = [
          {
            action = "PasteSelection";
            mouse = "Middle";
          }
        ];
      };
      window = {
        decorations = "buttonless";
        dynamic_padding = false;
        dynamic_title = true;
        option_as_alt = "OnlyLeft";
        padding = {
          x = 2;
          y = 2;
        };
      };
      terminal = {
        osc52 = "CopyPaste";
      };
      font = {
        size = 13;
        normal = {
          family = "JetBrainsMonoNL Nerd Font Mono";
          style = "Regular";
        };
        bold = {
          family = "JetBrainsMonoNL Nerd Font Mono";
          style = "Bold";
        };
        italic = {
          family = "JetBrainsMonoNL Nerd Font Mono";
          style = "Italic";
        };
        bold_italic = {
          family = "JetBrainsMonoNL Nerd Font Mono";
          style = "Bold Italic";
        };
      };
    };
  };

  home.file = {
    "./.config/alacritty/bamboo.toml".text = builtins.readFile
      (pkgs.fetchFromGitHub
        {
          owner = "ribru17";
          repo = "bamboo.nvim";
          rev = "d100fc78184ba9365fc6a4988518652e792cf6ec";
          hash = "sha256-3lsc55BkG11UZoCbGSkB6RQ2H329LDvY+UHE6YXxCzs=";
        } + "/extras/alacritty/bamboo.toml");

    "./.config/alacritty/keys.toml".source = ./keys.toml;
  };
}
