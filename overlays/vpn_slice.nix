# my fork with change source ip
self: super: {

  vpn-slice = super.vpn-slice.overrideAttrs {
    src = super.fetchFromGitHub {
      owner = "Jmarkin";
      repo = "vpn-slice";
      rev = "37bc7aeb17636d065cc1c437437fbc9494b5f9b3";
      hash = "sha256-OZ1fUHgjAnnMI7VU4SylUozV2yStohlSzIkr1gxUsgQ=";
    };
  };
}



