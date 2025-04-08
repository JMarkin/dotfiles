{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  inputs.disko.url = "github:nix-community/disko";
  inputs.disko.inputs.nixpkgs.follows = "nixpkgs";
  inputs.nixos-facter-modules.url = "github:numtide/nixos-facter-modules";

  outputs =
    {
      nixpkgs,
      disko,
      nixos-facter-modules,
      ...
    }:
    {

      # Slightly experimental: Like generic, but with nixos-facter (https://github.com/numtide/nixos-facter)
      /*
      nix run github:nix-community/nixos-anywhere --  --flake .#yun_svr_67279 \
      --generate-hardware-config nixos-facter yun_svr_67279/facter.json root@IP
      */
      nixosConfigurations.yun_svr_67279 = nixpkgs.lib.nixosSystem {
        system = "x86_64-linux";
        modules = [
          disko.nixosModules.disko
          ./yun_svr_67279/anywhere.nix
          nixos-facter-modules.nixosModules.facter
          {
            config.facter.reportPath =
              if builtins.pathExists ./yun_svr_67279/facter.json then
                ./yun_svr_67279/facter.json
              else
                throw "Have you forgotten to run nixos-anywhere with `--generate-hardware-config nixos-facter ./facter.json`?";
          }
        ];
      };
    };
}
