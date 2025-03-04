{ ... }:
{
  networking.wg-quick.interfaces = {
    wg0 = {
      address = [ "10.8.0.4/32"];
      dns = [ "10.8.0.1"];
      privateKeyFile = "/root/wireguard-keys/privatekey";

      postUp = ''
        ip rule add from 192.168.88.0/24 table main
      '';
      preDown = ''
        ip rule del from 192.168.88.0/24 table main
      '';

      peers = [
        {
          publicKey = "LXta7rmTHXbCZq+5BpE7FPthaqkdN+26XmZFEjEvmkM=";
          presharedKeyFile = "/root/wireguard-keys/preshared_from_peer0_key";
          allowedIPs = [ "0.0.0.0/0" ];
          endpoint = "192.168.88.28:51821";
          persistentKeepalive = 15;
        }
      ];
    };
  };
}
