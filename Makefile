nix-update:
	nix flake update
	home-manager switch --flake ~/.dotfiles

nvim-update:
	nvim --headless "+Lazy! update" +qa

update: nix-update nvim-update

