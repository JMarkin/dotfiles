local wezterm = require("wezterm")
local act = wezterm.action
local my_identify = "~/.ssh/id_ed25519_my"

return {
	font = wezterm.font("JetBrainsMonoNL Nerd Font Mono"),
	font_size = 13.0,
	line_height = 1.0,
	cell_width = 1.0,
	bold_brightens_ansi_colors = true,
	color_scheme = "OneDark (base16)",

	-- ssh_backend = "Ssh2",

	keys = {
		{
			key = "d",
			mods = "CMD|SHIFT",
			action = wezterm.action.SplitHorizontal({ domain = "CurrentPaneDomain" }),
		},
		{
			key = "d",
			mods = "CMD",
			action = wezterm.action.SplitVertical({ domain = "CurrentPaneDomain" }),
		},
		{ key = "UpArrow", mods = "CTRL", action = act.IncreaseFontSize },
		{ key = "DownArrow", mods = "CTRL", action = act.DecreaseFontSize },
		{
			key = "w",
			mods = "CMD",
			action = act.CloseCurrentPane({ confirm = false }),
		},
		{ key = "s", mods = "CMD", action = act.PaneSelect },
		{
			key = "h",
			mods = "ALT|SHIFT",
			action = act.AdjustPaneSize({ "Left", 5 }),
		},
		{
			key = "LeftArrow",
			mods = "ALT|SHIFT",
			action = act.AdjustPaneSize({ "Left", 5 }),
		},
		{
			key = "j",
			mods = "ALT|SHIFT",
			action = act.AdjustPaneSize({ "Down", 5 }),
		},
		{
			key = "DownArrow",
			mods = "ALT|SHIFT",
			action = act.AdjustPaneSize({ "Down", 5 }),
		},
		{ key = "k", mods = "ALT|SHIFT", action = act.AdjustPaneSize({ "Up", 5 }) },
		{ key = "UpArrow", mods = "ALT|SHIFT", action = act.AdjustPaneSize({ "Up", 5 }) },
		{
			key = "l",
			mods = "ALT|SHIFT",
			action = act.AdjustPaneSize({ "Right", 5 }),
		},
		{
			key = "RightArrow",
			mods = "ALT|SHIFT",
			action = act.AdjustPaneSize({ "Right", 5 }),
		},
		{
			key = "h",
			mods = "CTRL|SHIFT",
			action = act.ActivatePaneDirection("Left"),
		},
		{
			key = "LeftArrow",
			mods = "CTRL|SHIFT",
			action = act.ActivatePaneDirection("Left"),
		},
		{
			key = "l",
			mods = "CTRL|SHIFT",
			action = act.ActivatePaneDirection("Right"),
		},
		{
			key = "RightArrow",
			mods = "CTRL|SHIFT",
			action = act.ActivatePaneDirection("Right"),
		},
		{
			key = "k",
			mods = "CTRL|SHIFT",
			action = act.ActivatePaneDirection("Up"),
		},
		{
			key = "UpArrow",
			mods = "CTRL|SHIFT",
			action = act.ActivatePaneDirection("Up"),
		},
		{
			key = "j",
			mods = "CTRL|SHIFT",
			action = act.ActivatePaneDirection("Down"),
		},
		{
			key = "DownArrow",
			mods = "CTRL|SHIFT",
			action = act.ActivatePaneDirection("Down"),
		},
	},
}

