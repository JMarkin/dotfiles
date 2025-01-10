{ config, lib, pkgs, ... }:

{
  programs.bash = {
    enable = true;
    initExtra = /* bash */''
      # Do not attach when using a local terminal emulator or tty
      # if [[ "$SSH_CLIENT" == "" || "$TMUX" != "" ]]; then
      #
      #   if [[ $(${pkgs.procps}/bin/ps --no-header --pid=$PPID --format=comm) != "fish" && -z ''${BASH_EXECUTION_STRING} ]]
      #   then
      #     shopt -q login_shell && LOGIN_OPTION='--login' || LOGIN_OPTION=""
      #     exec ${pkgs.fish}/bin/fish $LOGIN_OPTION
      #   fi
      # fi

      # Switch to bash when there's arguments exist
      # such as `scp' or `sftp' or `ssh -t'
      if [ "$1" != "" ]; then
          exec -l /bin/bash "$@"
      fi

      ${pkgs.tmux}/bin/tmux attach || ${pkgs.tmux}/bin/tmux new
      EXITSTATUS=$?
      echo -e "\033[0m"
      exit $EXITSTATUS
    '';
  };
}

