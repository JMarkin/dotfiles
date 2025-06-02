{ pkgs
, lib
, ...
}:
let

  version = "2025-04-21";

  src = pkgs.fetchFromGitHub {
    owner = "Saghen";
    repo = "blink.pairs";
    rev = "fc905a47a4b44b072c7f73c5a63ffb5574f671c5";
    hash = "sha256-MlCi1IMhpaEUdQH7E1okrzL//juds6gVfbqEDHwZf5Q=";
  };

  rustPlatform = pkgs.makeRustPlatform {
    cargo = pkgs.rust-bin.selectLatestNightlyWith (toolchain: toolchain.default);
    rustc = pkgs.rust-bin.selectLatestNightlyWith (toolchain: toolchain.default);
  };

  blink-pairs-lib = rustPlatform.buildRustPackage {
    pname = "blink-pairs";
    inherit version src;

    useFetchCargoVendor = true;
    cargoHash = "sha256-j+zk0UMjvaVgsdF5iaRVO4Puf/XtGu08Cs92jKPaM1g=";

    nativeBuildInputs = [
      pkgs.pkg-config
    ];
  };

  blink-pairs-my = pkgs.vimUtils.buildVimPlugin {
    pname = "blink.pairs";
    inherit version src;

    preInstall =
      let
        ext = pkgs.stdenv.hostPlatform.extensions.sharedLibrary;
      in
      ''
        mkdir -p target/release
        ln -s ${blink-pairs-lib}/lib/libblink_pairs${ext} target/release/
      '';

    passthru = {
      updateScript = pkgs.nix-update-script {
        attrPath = "vimPlugins.blink-pairs.blink-pairs-lib";
      };

      # needed for the update script
      inherit blink-pairs-lib;
    };

    meta = {
      description = "Rainbow highlighting and intelligent auto-pairs for Neovim";
      homepage = "https://github.com/Saghen/blink.pairs";
      changelog = "https://github.com/Saghen/blink.pairs/blob/${src.tag}/CHANGELOG.md";
      license = lib.licenses.mit;
      maintainers = with lib.maintainers; [ isabelroses ];
    };
  };


in
{


  programs.neovim.plugins = with pkgs.vimPlugins; [
    # blink-cmp
    blink-pairs-my
    # blink-cmp-avante
    # blink-compat
  ];

  home.file = with pkgs.vimPlugins; {
    # ".local/share/nvim/nix/blink.cmp/" = {
    #   recursive = true;
    #   source = blink-cmp;
    # };
    ".local/share/nvim/nix/blink.pairs/" = {
      recursive = true;
      source = blink-pairs-my;
    };
    # ".local/share/nvim/nix/blink-cmp-avante/" = {
    #   recursive = true;
    #   source = blink-cmp-avante;
    # };
    # ".local/share/nvim/nix/blink.compat/" = {
    #   recursive = true;
    #   source = blink-compat;
    # };
  };

}
