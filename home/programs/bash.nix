{ config, lib, pkgs, ... }:

{
  programs.bash = {
    enable = true;
    initExtra = /* bash */''
      # Switch to bash when there's arguments exist
      # such as `scp' or `sftp' or `ssh -t'
      if [ "$1" != "" ]; then
          exec -l ${pkgs.bash}/bin/bash "$@"
      fi

      ${pkgs.tmux}/bin/tmux attach || ${pkgs.tmux}/bin/tmux new
    '';
    bashrcExtra = /*bash*/''
      bind 'set mark-directories on'
      bind 'set mark-symlinked-directories on'
      bind 'set page-completions off'
      bind 'set show-all-if-ambiguous on'
      bind 'set visible-stats on'
      bind 'set completion-query-items 9001'
    '';
    shellAliases = {
      cat = "bat";
      grep = "rg";
      vim = "nvim";
      v = "nvim";
      vi = "nvim";
      forward = "ssh -M -fNT";
      gzip = "pigz";
      ls = "eza --icons --classify --group-directories-first --group --color=auto";
      l = "ls --git-ignore";
      la = "ls -a $argv";
      ll = "ls --header -l --time-style=long-iso -M -m";
      lla = "ll -a";
    };
  };
}

