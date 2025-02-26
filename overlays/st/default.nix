# my st config
self: super: {

  st = super.st.overrideAttrs
    (oldAttrs:
      let
        configFile = super.writeText "config.def.h" (builtins.readFile ./config.h);
        configMk = super.writeText "config.mk" (builtins.readFile ./config.mk);
        patchFile = super.writeText "patches.def.h" (builtins.readFile ./patches.h);
      in
      {
        pname = "st-flexipatch";
        version = "0.9.2";
        src = super.fetchFromGitHub {
          owner = "bakkeby";
          repo = "st-flexipatch";
          rev = "08b53c4960186ca64978a8463a2648336a42bd3e";
          sha256 = "sha256-2M3IunLBqtJBPFmQDUvl1WmBSi0ESQ4kdZND//tgYgE=";
        };

        buildInputs = oldAttrs.buildInputs ++ (with super; [ 
          harfbuzz 
          libsixel 
          imlib2
        ]);

        

        postPatch = ''
          cp ${configFile} config.def.h
          cp ${patchFile} patches.def.h
          cp ${configMk} config.mk
        ''
        + super.lib.optionalString super.stdenv.hostPlatform.isDarwin ''
          substituteInPlace config.mk --replace "-lrt" ""
        '';

      });
}

