{ pkgs
, ...
}:
{
  services = {
    dbus = {
      packages = with pkgs;[
        gcr
      ];
    };

    gnome = {
      gnome-keyring = {
        enable = true;
      };
    };

    pipewire = {
      enable = true;
      alsa = {
        enable = true;
        support32Bit = false;
      };
      jack.enable = false;
      pulse.enable = true;
      wireplumber = {
        enable = true;
      };
    };

    xserver = {
      enable = true;
      desktopManager = {
        xterm = {
          enable = false;
        };
      };
      displayManager = {
        lightdm = {
          enable = false;
          greeter = {
            enable = false;
          };
        };
      };
      excludePackages = [
        pkgs.xterm
      ];
    };
  };
}
