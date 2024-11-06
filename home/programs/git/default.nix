{ config, lib, pkgs, ... }:

{
  home.packages = with pkgs; [
    python3
  ];

  programs.git = {
    enable = true;
    userName = "jmarkin";
    userEmail = "me@jmarkin.ru";
    ignores = [
      ".direnv/"
      ".go/"
      ".cargo/"
      ".npm/"
    ];
    lfs = {
      enable = true;
      skipSmudge = true;
    };
    hooks = {
      prepare-commit-msg = ./commitprefix.py;
    };
    delta = {
      enable = true;
      options = {
        decorations = {
          commit-decoration-style = "blue ol";
          commit-style = "raw";
          file-style = "omit";
          hunk-header-decoration-style = "blue box";
          hunk-header-file-style = "red";
          hunk-header-line-number-style = "#067a00";
          hunk-header-style = "file line-number syntax";
        };
        features = "decorations";
        whitespace-error-style = "22 reverse";
      };
    };
    extraConfig = {
      core = {
        fscache = true;
        packedGitLimit = "512m";
        packedGitWindowSize = "512m";
      };

      pull = {
        rebase = false;
      };
      http = {
        sslVerify = false;
        postBuffer = "157286400";
      };

      merge = {
        conflictstyle = "diff3";
      };

      push = {
        autoSetupRemote = true;
      };

      pack = {
        window = 1;
        deltaCacheSize = "2047m";
        packSizeLimit = "2047m";
        windowMemory = "2047m";
      };
    };
  };
}
