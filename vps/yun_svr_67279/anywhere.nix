{ modulesPath
, lib
, pkgs
, ...
}:
{

  system.stateVersion = "25.05";

  imports = [
    (modulesPath + "/installer/scan/not-detected.nix")
    (modulesPath + "/profiles/qemu-guest.nix")
    ./network.nix
    ./boot.nix
  ];

  services.openssh = {
    enable = true;
    ports = [ 324 ];
  };

  environment.systemPackages = map lib.lowPrio [
    pkgs.curl
    pkgs.gitMinimal
  ];

  users.users.root.openssh.authorizedKeys.keys = [
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEeeoTM1Z5oLaD3jWddN4Pc0OcRw+eLOnyJPfde81o6j me@jmarkin.ru"
  ];

}
