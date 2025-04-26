{ pkgs, lib,... }:
{

  imports = [
    ./foot.nix
  ];

  fonts = {
    packages = with pkgs; [
      noto-fonts
      noto-fonts-cjk
      noto-fonts-emoji
      font-awesome
      source-han-sans
    ];
  };

  security.polkit.enable = true;
  security.pam.loginLimits = [
    { domain = "@users"; item = "rtprio"; type = "-"; value = 1; }
  ];

  wayland.windowManager.sway = {
    enable = true;
    wrapperFeatures.gtk = true; # Fixes common issues with GTK 3 apps
    config = {
      modifier = "Mod4";
      bars = [{
        command = "${pkgs.waybar}/bin/waybar";
      }];
      terminal = "foot";
      startup = [
        { command = "foot"; }
      ];
      focus = {
        forceWrapping = false;
        followMouse = false;
      };
      fonts = {
        names = [ "JetBrainsMonoNL Nerd Font Mono" ];
        size = 13;
      };
      gaps = {
        inner = 15;
      };
      input = {
        "type:touchpad" = {
          dwt = "enabled";
          tap = "enabled";
          natural_scroll = "enabled";
          middle_emulation = "enabled";
        };

        "type:pointer" = {
          natural_scroll = "enabled";
        };

        "type:mouse" = {
          natural_scroll = "disabled";
        };
      };
      window = {
        border = 3;
        titlebar = false;
        commands = [
          {
            command = "opacity 1.0, border pixel 3, inhibit_idle fullscreen";
            criteria = {
              class = ".*";
            };
          }
          {
            command = "opacity 1.0, border pixel 3, inhibit_idle fullscreen";
            criteria = {
              app_id = ".*";
            };
          }
          {
            command = "resize set 650 450";
            criteria = {
              app_id = "snippetexpandergui";
            };
          }
          {
            command = "floating enable, sticky enable";
            criteria = {
              title = "Picture-in-Picture";
            };
          }
          {
            command = "floating enable, sticky enable";
            criteria = {
              title = ".*Sharing Indicator.*";
            };
          }
          {
            command = "floating enable, sticky enable, resize set 650 450";
            criteria = {
              title = ".*Syncthing Tray.*";
            };
          }
        ];
      };
    };
    swaynag = {
      enable = true;
      settings = {
        "<config>" = {
          edge = "top";
          message-padding = 5;
        };
      };
    };
  };

  home.packages = with pkgs; [
    grim # screenshot functionality
    slurp # screenshot functionality
    wl-clipboard # wl-copy and wl-paste for copy/paste from stdin / stdout
    mako # notification system developed by swaywm maintainer
  ];

}
