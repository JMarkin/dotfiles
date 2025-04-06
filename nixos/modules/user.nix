_:
{
  users.users.kron = {
    isNormalUser = true;
    description = "kron";
    extraGroups = [ "networkmanager" "wheel" "video" "docker" ];
    openssh.authorizedKeys.keys = [
      "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICpUjhFFCAPWM/rols99hoDdxmrC0m3rbqU1hW62SDcO kron@kron-work.local"
      "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICMuwmdPJtSrVMyw//J35xAFTlvc3n8YFTgJvuAP6l0m kron@jmarkin.ru"
      "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEeeoTM1Z5oLaD3jWddN4Pc0OcRw+eLOnyJPfde81o6j me@jmarkin.ru"
    ];
  };
}
