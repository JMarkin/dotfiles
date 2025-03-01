{ config, pkgs, lib, ... }:

{

  imports = [
    ./minsetup.nix
    ../programs/neovim/minimal.nix
  ];

  home.packages = with pkgs; [
    vpn-slice
  ];

  home.file = {
    ".config/vpn/template.bash".text = /*bash*/''
      VPN_SLICE="%172.0.0.0/8 %192.168.0.0/24"
      VPN_USER="user"
      VPN_URL="url"
    '';
  };

  programs.bash.bashrcExtra = /*bash*/ ''
    
    vpn-ocn(){
      local name=$1
      local VPN_SLICE_PATH=$(which vpn-slice)

      source ~/.config/vpn/"$name".bash

      local cmd="$VPN_SLICE_PATH -vvv $VPN_SLICE"

      echo "$cmd"
      sudo OPENSSL_CONF=/home/kron/.config/openssl.cnf openconnect \
          --useragent="AnyConnect" \
          --pid-file=/tmp/openconnect_"$name".pid -u "$VPN_USER" "$VPN_URL" -s "$cmd"
    }
    vpn-ocn-down() {
      sudo kill -INT $(cat /tmp/openconnect_$name.pid)
    }
    '';

}
