{pkgs, ...}:
{

  imports = [
    ./minsetup.nix
    ../programs/fish
    ../programs/neovim
    ../programs/direnv.nix
    ../programs/sway.nix
  ];

  home.homeDirectory = "/home/kron";
  home.packages = with pkgs; [
    jaq
    delta
    universal-ctags
    docker-compose
    dust
    tree-sitter
    ptags
    createnv
    dotenv-linter
    kubectl
    k9s


    ollama
    rustic
    rclone
  ];

  home.sessionVariables.OLLAMA_HOST = "192.168.88.15";
  home.sessionVariables.OLLAMA_PORT = "11434";
  home.sessionVariables.OLLAMA_URL = "http://192.168.88.15:11434";
}
