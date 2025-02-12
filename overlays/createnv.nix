self: super: {

  createnv = super.rustPlatform.buildRustPackage {
    pname = "createnv";
    version = "0.0.4";

    src = super.fetchFromGitHub {
      owner = "cuducos";
      repo = "createnv";
      # v0,0.4
      rev = "cf9b5dea8ed120462c50794322a53fd2d29ab9be";
      hash = "sha256-vyKfNzV0v3fnthB2hl3glADcfo04IfqR4qzAa+VwBV8=";
    };
    useFetchCargoVendor = true;
    cargoHash = "sha256-9JIQxu5kqMl4WEisvE/wFJV16KKQqJPQKcSuATUbh7c=";

    doCheck = false;

    meta = {
      description = "createnv";
      homepage = "https://github.com/cuducos/createnv";
      changelog = "";
      mainProgram = "createnv";
    };
  };
}


