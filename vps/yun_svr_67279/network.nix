{lib, ...}:
{
  networking.useDHCP = lib.mkForce false;
  networking.hostName = "svr67279";

  networking = {
    nameservers = [ "8.8.8.8" "2001:4860:4860::8888" ];

    interfaces.ens192 = {
      ipv6.addresses = [{
        address = "2a0d:6c2:26:2ee::";
        prefixLength = 55;
      }];
      ipv4.addresses = [{
        address = "185.250.180.20";
        prefixLength = 24;
      }];
    };
    defaultGateway = {
      address = "185.250.180.1";
      interface = "ens192";
    };
    defaultGateway6 = {
      address = "fe80::1";
      interface = "ens192";
    };
  };

  networking.firewall = {
    enable = true;
    allowedTCPPorts = [ 80 443 324 5201 ];
  };
}
