{ config, pkgs, lib, ... }:

let
  startShip = pkgs.fetchFromGitHub {
    owner = "Rolv-Apneseth";
    repo = "starship.yazi";
    rev = "d1cd0a38aa6a2c2e86e62a466f43e415f781031e";
    sha256 = "sha256-XiEsykudwYmwSNDO41b5layP1DqVa89e6Emv9Qf0mz0=";
  };
in
{
  programs.yazi = {
    enable = true;
    initLua = /* lua */''
      require("starship"):setup()
    '';
    plugins = {
      starship = startShip;
    };
    settings = {
      keymap = {
        manager = {
          prepend_keymap = [
            {
              on = [ "<Tab>" ];
              run = "enter";
              desc = "enter the child directory";
            }
            {
              on = [ "<BackTab>" ];
              run = "leave";
              desc = "enter the child directory";
            }
          ];
        };
        input = {
          prepend_keymap = [
            {
              on = [ "<Esc>" ];
              run = "close";
              desc = "Cancel input";
            }
          ];
        };
      };
    };
  };
}

