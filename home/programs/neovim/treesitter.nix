{ pkgs, ... }:
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
    # currently not working
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

in
{

  programs.neovim.plugins = [
    treesitterWithGrammars
    pkgs.vimPlugins.nvim-treesitter-context
  ];
  home.file = {
    ".local/share/nvim/nix/nvim-treesitter-context/" = {
      recursive = true;
      source = pkgs.vimPlugins.nvim-treesitter-context;
    };

    ".local/share/nvim/nix/nvim-treesitter/" = {
      recursive = true;
      source = treesitterWithGrammars;
    };

    ".local/share/nvim/nix/nvim-treesitter/parser" = {
      recursive = true;
      source = "${treesitter-parsers}/parser";
    };
  };

}
