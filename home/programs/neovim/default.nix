{ config, pkgs, ... }:
let

  # treesitterWithGrammars = pkgs.vimPlugins.nvim-treesitter.withAllGrammars;
  treesitterWithGrammars = (pkgs.vimPlugins.nvim-treesitter.withPlugins (p: [
    # languages
    p.rust
    p.c
    p.cpp
    p.cuda
    p.python
    p.typescript
    p.javascript
    p.fish
    p.go
    p.lua
    p.html
    p.htmldjango
    p.css
    p.bash
    p.vue
    p.scss
    p.sql
    p.markdown
    p.json
    p.json5
    p.jsonc
    p.graphql
    p.commonlisp
    p.latex
    p.glsl
    p.nix
    # conf files
    p.ssh_config
    p.jsdoc
    p.yaml
    p.toml
    p.proto
    p.http
    p.hurl
    p.make
    p.cmake
    p.dockerfile
    p.ini
    p.vim
    p.vimdoc
    p.passwd
    p.requirements
    p.hcl
    p.xml
    p.nginx
    p.tmux
    p.udev
    # tools
    p.markdown_inline
    p.jq
    p.regex
    p.query
    p.comment
    p.rst

    # git
    p.gitcommit
    p.git_rebase
    p.gitignore
    p.git_config
    p.gitattributes

  ]));

  treesitter-parsers = pkgs.symlinkJoin {
    name = "treesitter-parsers";
    paths = treesitterWithGrammars.dependencies;
  };
  nvim-spell-ru-utf8-dictionary = builtins.fetchurl {
    url = "http://ftp.vim.org/vim/runtime/spell/ru.utf-8.spl";
    sha256 = "sha256:0kf5vbk7lmwap1k4y4c1fm17myzbmjyzwz0arh5v6810ibbknbgb";
  };
in
{
  home.packages = with pkgs; [

    # builder
    lua51Packages.lua
    lua51Packages.luarocks

    # lsp
    nginx-language-server
    lua-language-server
    rust-analyzer-unwrapped
    python312Packages.jedi-language-server
    bash-language-server
    biome

    # lsp features
    fswatch

    #tools
    ruff
    python312Packages.mypy
    python312Packages.sqlfmt
    stylua
    prettierd
    fixjson
    rustfmt
    codespell
    sqlfluff
    djlint

  ];

  programs.neovim = {
    enable = true;
    package = pkgs.neovim;
    vimAlias = true;
    viAlias = true;
    coc.enable = false;
    withNodeJs = true;

    plugins = [
      treesitterWithGrammars
    ];
  };

  home.file = {
    ".config/nvim".source = config.lib.file.mkOutOfStoreSymlink "${config.home.homeDirectory}/.dotfiles/home/programs/neovim/nvim";

    ".local/share/nvim/spell/ru.utf-8.spl".source = nvim-spell-ru-utf8-dictionary;
    ".local/share/nvim/nix/lua/runtimes.lua".text = /*lua*/''
      vim.opt.runtimepath:append("${treesitter-parsers}")
    '';

    # Treesitter is configured as a locally developed module in lazy.nvim
    # we hardcode a symlink here so that we can refer to it in our lazy config
    ".local/share/nvim/nix/nvim-treesitter/" = {
      recursive = true;
      source = treesitterWithGrammars;
    };
  };

}
