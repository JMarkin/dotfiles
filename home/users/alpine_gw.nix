{ config, pkgs, lib, ... }:

{

  imports = [
    ./vm.nix
  ];

  home.packages = with pkgs; [
    vpn-slice
  ];

  home.file = {
    ".config/vpn/template.fish".source = ../legacyconfig/vpn/template.fish;
  };

  programs.bash = {
    enable = true;
    initExtra = /* bash */''
      # Define colors
      YELLOW="\033[0;93m"
      GREEN="\033[0;32m"
      CYAN="\033[0;36m"
      RED="\033[0;31m"
      NC="\033[0m"

# Do not attach when using a local terminal emulator or tty
      if [ "$SSH_CLIENT" == "" ]; then
              tmux new
              exit $?
      fi

# Switch to bash when there's arguments exist
# such as `scp' or `sftp' or `ssh -t'
      if [ "$1" != "" ]; then
              exec -l /bin/bash "$@"
      fi

# Add a pause for displaying motd
      echo -e "\n$GREEN[ Press any key to continue ]\n$YELLOW"
      read -n 1 -s -r
      tmux attach || tmux new
      EXITSTATUS=$?
      echo -e $NC
      exit $EXITSTATUS
    '';
  };
}
