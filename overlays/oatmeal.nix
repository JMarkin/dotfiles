# change by error patchelf
self: super: {

  nur.repos.dustinblackman.oatmeal = super.nur.repos.dustinblackman.oatmeal.overrideAttrs {
    installPhase = ''
      mkdir -p $out/bin
      cp -vr ./oatmeal $out/bin/oatmeal
      # ${super.patchelf}/bin/patchelf --set-interpreter $(cat $NIX_CC/nix-support/dynamic-linker) $out/bin/oatmeal
      mkdir -p $out/share/doc/oatmeal/copyright
      cp LICENSE $out/share/doc/oatmeal/copyright/
      cp THIRDPARTY.html $out/share/doc/oatmeal/copyright/
      installManPage ./manpages/oatmeal.1.gz
      installShellCompletion ./completions/*
    '';
  };
}
