self: super: {

  chromadb = super.chromadb.overrideAttrs {
    dependencies =
      with super.python3Packages;
      [
        pydantic-settings
      ] ++ super.chromadb.dependencies;
  };
  vectorcode = super.vectorcode.overrideAttrs {
    dependencies =
      with super.python3Packages;
      [
        chromadb
        httpx
        numpy
        pathspec
        psutil
        pygments
        sentence-transformers
        shtab
        tabulate
        transformers
        tree-sitter
        tree-sitter-language-pack
        lsprotocol
        pygls
        mcp
        pydantic-settings
      ];
  };
}
