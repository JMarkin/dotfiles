{ pkgs, ... }:
let

  mchub = pkgs.buildNpmPackage
    rec {
      pname = "mchub";
      version = "3.1.6";

      src = pkgs.fetchFromGitHub {
        owner = "ravitemer";
        repo = "mcp-hub";
        rev = "v${version}";
        hash = "sha256-GBW7hrWOATEBk8m7HjMEUSfv47ABazlVHsZ4CRQ8Z3M=";
      };

      npmDepsHash = "sha256-lIaP1ryUXIF1dI1iRSf56maHJf5WPPgJhEZCuQBGw0k=";
    };

  mchubnvim = pkgs.fetchFromGitHub {
    owner = "ravitemer";
    repo = "mcphub.nvim";
    rev = "v5.0.0";
    hash = "sha256-xXo7s5XCQ1+yoRrkaoqolwUlBJE6zMvmbOzACzVWK8E=";
  };
in
{
  home.packages = [
    pkgs.bun
    mchub
  ];

  home.file = {
    ".local/share/nvim/nix/mchub.nvim/" = {
      recursive = true;
      source = mchubnvim;
    };
  };

  # home.file = {
  #   ".config/mcphub/servers.json".text = /*json*/ ''
  #       {
  #       "mcpServers": {
  #         "TalkToFigma": {
  #             "command": "bunx",
  #             "args": ["cursor-talk-to-figma-mcp@latest"]
  #           }
  #         }
  #       }
  #   '';
  # };

}
