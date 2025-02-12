update:
	nix flake update
	home-manager switch --flake ~/.dotfiles
	nvim --headless "+Lazy! update" +qa
