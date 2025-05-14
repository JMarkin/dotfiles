{
  description = "NixOS Configuration, original https://github.com/Kidsan/nixos-config";

  inputs = {
    nixpkgs.url = "nixpkgs/nixpkgs-unstable";
    nixos.url = "nixpkgs/nixos-unstable";

    home-manager.inputs.nixpkgs.follows = "nixpkgs";
    home-manager.url = "github:nix-community/home-manager/master";

    neovim-nightly-overlay.inputs.nixpkgs.follows = "nixpkgs";
    neovim-nightly-overlay.url = "github:nix-community/neovim-nightly-overlay";

    agenix.inputs.nixpkgs.follows = "nixpkgs";
    agenix.url = "github:ryantm/agenix";

    darwin.inputs.nixpkgs.follows = "nixpkgs";
    darwin.url = "github:lnl7/nix-darwin/master";

    mac-app-util.url = "github:hraban/mac-app-util";

    disko.url = "github:nix-community/disko";
    disko.inputs.nixpkgs.follows = "nixpkgs";

  };

  outputs =
    { self
    , nixpkgs
    , nixos
    , home-manager
    , darwin
    , mac-app-util
    , disko
    , agenix
    , ...
    } @ inputs:
    let
      overlays = [
        (import ./overlays/cgrc.nix)
        (import ./overlays/createnv.nix)
        (import ./overlays/vpn_slice.nix)
        # (import ./overlays/rllama)
      ];

      neovimNightly = [
        inputs.neovim-nightly-overlay.overlays.default
        (import ./overlays/neovide.nix)
      ];

      config = {
        allowUnfree = true;
      };

      nixosPackages = import nixos {
        system = "x86_64-linux";
        inherit config overlays;
      };

      x86Pkgs = import nixpkgs {
        system = "x86_64-linux";
        inherit config overlays;
      };

      x86PkgsNeovimNightly = import nixpkgs {
        system = "x86_64-linux";
        overlays = overlays ++ neovimNightly;
        inherit config;
      };

      darwinPkgs = import nixpkgs {
        system = "aarch64-darwin";
        config = { allowUnfree = true; };
        inherit overlays;
      };

      darwinPkgsNeovimNightly = import nixpkgs {
        system = "aarch64-darwin";
        config = { allowUnfree = true; };
        overlays = overlays ++ neovimNightly;
      };



    in
    {
      homeConfigurations = {
        "kron@kron-work.local" = home-manager.lib.homeManagerConfiguration {
          pkgs = darwinPkgsNeovimNightly;

          modules = [
            mac-app-util.homeManagerModules.default
            {
              home.homeDirectory = "/Users/kron";
            }
            ./home/users/kron_darwin.nix
          ];
        };
        "kron@nixos" = home-manager.lib.homeManagerConfiguration {
          pkgs = x86Pkgs;

          modules = [
            {
              home.homeDirectory = "/home/kron";
            }
            ./home/users/vm.nix
          ];
        };
        "kron@nixos-gw" = home-manager.lib.homeManagerConfiguration {
          pkgs = x86Pkgs;

          modules = [
            {
              home.homeDirectory = "/home/kron";
            }
            ./home/users/gw.nix
          ];
        };
      };

      nixosConfigurations = {
        vm86 = nixos.lib.nixosSystem {
          system = "x86_64-linux";
          pkgs = nixosPackages;
          modules = [
            agenix.nixosModules.default
            {
              environment.etc."nix/inputs/nixpkgs".source = inputs.nixos.outPath;
            }
            ./nixos/vm.nix
            home-manager.nixosModules.home-manager
          ];
        };
        /*
        nixos-rebuild switch --flake .#gw \
        --target-host gw-nix-home --verbose --use-remote-sudo
        */
        gw = nixos.lib.nixosSystem {
          system = "x86_64-linux";
          pkgs = nixosPackages;
          modules = [
            agenix.nixosModules.default
            {
              environment.etc."nix/inputs/nixpkgs".source = inputs.nixos.outPath;
            }
            ./nixos/gw.nix
            home-manager.nixosModules.home-manager
            {
              home-manager.useGlobalPkgs = true;
              home-manager.useUserPackages = true;

              home-manager.users.kron = { ... }: {
                home.homeDirectory = "/home/kron";

                imports = [
                  ./home/users/gw.nix
                ];
              };
            }
          ];
        };
        /*
        nixos-rebuild switch --flake .#yun_svr67279 \
        --target-host yun_svr67279 --verbose --use-remote-sudo
        */
        yun_svr67279 = nixos.lib.nixosSystem {
          system = "x86_64-linux";
          pkgs = nixosPackages;
          modules = [
            {
              environment.etc."nix/inputs/nixpkgs".source = inputs.nixos.outPath;
            }
            disko.nixosModules.disko
            agenix.nixosModules.default
            ./vps/yun_svr_67279
          ];
        };
      };

      darwinConfigurations = {
        "kron-work" = darwin.lib.darwinSystem {
          system = "aarch64-darwin";
          inputs = { inherit darwin nixpkgs; };
          pkgs = import nixpkgs {
            inherit config;
            system = "aarch64-darwin";
          };
          modules = [
            home-manager.darwinModules.home-manager
            ./darwin/macbook.nix
          ];
        };
      };


      devShell = {
        x86_64-linux = x86Pkgs.mkShell
          {
            nativeBuildInputs = [ x86Pkgs.bashInteractive ];
            buildInputs = with x86Pkgs; [
              nil
              nixpkgs-fmt
              vim-language-server
              ruff
              python312Packages.mypy
              lua-language-server
              stylua
              basedpyright
            ];
          };
        aarch64-darwin = darwinPkgs.mkShell
          {
            nativeBuildInputs = [ darwinPkgs.bashInteractive ];
            buildInputs = with darwinPkgs; [
              nil
              vim-language-server
              nixpkgs-fmt
              ruff
              python312Packages.mypy
              lua-language-server
              stylua
              basedpyright
            ];
          };
      };
    };

}
