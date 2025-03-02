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

    # nur = {
    #   url = "github:nix-community/NUR";
    #   inputs.nixpkgs.follows = "nixpkgs";
    # };

    mac-app-util.url = "github:hraban/mac-app-util";

    #impermanence.url = "github:nix-community/impermanence/63f4d0443e32b0dd7189001ee1894066765d18a5";

    #disko.inputs.nixpkgs.follows = "nixpkgs";
    #disko.url = "github:nix-community/disko/master";

    # secrets.inputs.nixpkgs.follows = "nixpkgs";
    # secrets.url = "git+ssh://forgejo@git.home/kidsan/secrets.git?ref=main";

    # nixpkgs-wayland.url = "github:nix-community/nixpkgs-wayland";
    # nixpkgs-wayland.inputs.nixpkgs.follows = "nixpkgs";

  };

  outputs = { self, nixpkgs, nixos, home-manager, agenix, darwin, mac-app-util, ... } @ inputs:
    let
      overlays = [
        (import ./overlays/cgrc.nix)
        (import ./overlays/createnv.nix)
        (import ./overlays/jedi_language_server.nix)
        (import ./overlays/vpn_slice.nix)
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

      x86PkgssNeovimNightly = import nixpkgs {
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
        "kron@alpine-gw" = home-manager.lib.homeManagerConfiguration {
          pkgs = x86Pkgs;

          modules = [
            {
              home.homeDirectory = "/home/kron";
            }
            ./home/users/alpine_gw.nix
          ];
        };
        "kron@nixos" = home-manager.lib.homeManagerConfiguration {
          pkgs = x86PkgssNeovimNightly;

          modules = [
            {
              home.homeDirectory = "/home/kron";
            }
            ./home/users/vm.nix
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
            # secrets.nixosModules.tln or { }
            home-manager.nixosModules.home-manager
            {
              home-manager.extraSpecialArgs = {
                pkgs = x86Pkgs;
              };
              home-manager.users.kron = import ./home/users/vm.nix;
            }
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
              basedpyright
            ];
          };
      };
    };

}
