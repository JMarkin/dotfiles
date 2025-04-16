{ pkgs, ... }:
let

  mchub = pkgs.buildNpmPackage
    rec {
      pname = "mchub";
      version = "3.0.3";

      src = pkgs.fetchFromGitHub {
        owner = "ravitemer";
        repo = "mcp-hub";
        rev = "v${version}";
        hash = "sha256-0WeNfEYdW6gBzQiDa18zIMCFFzrd5ZZ4PZ8SZFrA//o=";
      };

      npmDepsHash = "sha256-eW+MueL35mBDlide15zKZIMIDLef0b2IkxrlwZeI9oQ=";
    };
in
{
  home.packages = [
    pkgs.bun
    mchub
  ];

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
