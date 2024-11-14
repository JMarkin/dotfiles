# my fork with change source ip
self: super: {

  createnv = super.pkgs.vpn-slice {
    vpn-slice = super.fetchFromGitHub {
      owner = "Jmarkin";
      repo = "vpn-slice";
      rev = "37bc7aeb17636d065cc1c437437fbc9494b5f9b3";
      hash = "";
    };
  };
}



