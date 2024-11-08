{
  outputs = { self }: {

    templates.simple = {
      path = ./simple;
      description = "A simple dev flake";
    };

    templates.python = {
      path = ./python;
      description = "A simple Python dev flake";
    };

    templates.default = self.templates.simple;
  };
}
