# disable build always time
self: super: {

  neovide = super.neovide.overrideAttrs {
    nativeCheckInputs = [ ];
    doCheck = false;
  };
}

