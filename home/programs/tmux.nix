{ config, pkgs, ... }:
let
  smartsplits = pkgs.fetchFromGitHub {
    owner = "mrjones2014";
    repo = "smart-splits.nvim";
    rev = "184985c87c4dd1383d66963131df9a35297089f5";
    sha256 = "sha256-JnqlXUEBVyoLiPUkVHZCrO2B/PMF/luir1+U7TbpAX8=";
  };

  tmux-smart-splits = pkgs.tmuxPlugins.mkTmuxPlugin
    ({
      pluginName = "smart-splits.nvim";
      version = "unstable-2025-05-02";
      rtpFilePath = "smart-splits.tmux";
      src = smartsplits;
    });
in
{


  home.file = {
    ".local/share/nvim/nix/smart-splits.nvim/" = {
      recursive = true;
      source = smartsplits;
    };
  };

  programs.tmux = {
    enable = true;
    escapeTime = 5;
    baseIndex = 1;
    clock24 = true;
    keyMode = "vi";
    terminal = "tmux-256color";
    plugins = with pkgs; [
      tmuxPlugins.yank
      tmuxPlugins.better-mouse-mode
      tmuxPlugins.prefix-highlight

      tmux-smart-splits

    ];
    extraConfig = /*tmux*/''
      # if multiple clients are attached to the same window, maximize it to the
      # bigger one
      set-window-option -g aggressive-resize

      setw -g pane-base-index 1

      # re-number windows when one is closed
      set -g renumber-windows on

      # word separators for automatic word selection
      setw -g word-separators ' @"=()[]-:,.'
      setw -ag word-separators "'"

      # Show times longer than supposed
      set -g display-panes-time 2000

      # tmux messages are displayed for 4 seconds
      set -g display-time 4000

      # {n}vim compability
      set -g default-terminal "screen-256color"
      set-option -a terminal-features "xterm-256color:RGB"
      # set -ga terminal-overrides ',xterm-256color:Ms=\\E]52;c;%p2%s\\7'
      # set -as terminal-overrides ',*:Setulc=\E[58::2::%p1%{65536}%/%d::%p1%{256}%/%{255}%&%d::%p1%{255}%&%d%;m'
      set -g set-clipboard on
      # Split horiziontal and vertical splits, instead of % and ". We also open them
      # in the same directory.  Because we use widescreens nowadays, opening a
      # vertical split that takes half of the screen is not worth. For vertical we
      # only open 100 lines width, for horizontal it's 30 columns.
      bind-key s split-window -v -p 20 -c '#{pane_current_path}'
      bind-key v split-window -h -p 50 -c '#{pane_current_path}'

      # Pressing Ctrl+Shift+Left (will move the current window to the left. Similarly
      # right. No need to use the modifier (C-b).
      bind-key -n C-S-Left swap-window -t -1
      bind-key -n C-S-Right swap-window -t +1

      # Source file
      unbind r
      bind r source-file ~/.config/tmux/tmux.conf \; display "Reloaded!"

      # Update default binding of `Enter` and `Space to also use copy-pipe
      unbind -T copy-mode-vi Enter
      unbind -T copy-mode-vi Space

      bind-key -T edit-mode-vi Up send-keys -X history-up
      bind-key -T edit-mode-vi Down send-keys -X history-down

      # setup 'v' to begin selection as in Vim
      bind-key -T copy-mode-vi 'v' send-keys -X begin-selection

      # copy text with `y` in copy mode
      bind-key -T copy-mode-vi 'y' send -X copy-selection-and-cancel

      # copy text with mouse selection without pressing any key
      bind-key -T copy-mode-vi MouseDragEnd1Pane send -X copy-selection-and-cancel

      # emacs key bindings in tmux command prompt (prefix + :) are better than
      # vi keys, even for vim users
      set -g status-keys emacs

      # focus events enabled for terminals that support them
      set -g focus-events on

      # Sync panes (Send input to all panes in the window). When enabled, pane
      # borders become red as an indication.
      bind C-s if -F '#{pane_synchronized}' \
                           'setw synchronize-panes off; \
                            setw pane-active-border-style fg=colour63,bg=default; \
                            setw pane-border-format       " #P "' \
                         'setw synchronize-panes on; \
                          setw pane-active-border-style fg=red; \
                          setw pane-border-format       " #P - Pane Synchronization ON "'

      # Have a very large history
      set -g history-limit 100000

      # Mouse mode on
      set -ag terminal-overrides 'xterm*:smcup@:rmcup@'
      set -g mouse on
      set -g @scroll-speed-num-lines-per-scroll 2

      # Set title
      set -g set-titles on
      set -g set-titles-string "#T"

      # Equally resize all panes
      bind-key = select-layout even-horizontal
      bind-key | select-layout even-vertical


      bind-key x kill-pane


      set-option -g status on
      set-option -g status-interval 3
      set-option -g status-justify left
      set-option -g status-keys vi
      set-option -g status-position top
      set-option -g status-style fg=colour136,bg=colour235
      set-option -g status-left-length 100
      set-option -g status-left-style default
      set-option -g status-left "#[fg=red]#{prefix_highlight} #S #[fg=green]#H #[default] "
      set-option -g status-right-length 200
      set-option -g status-right-style default
          # wg_lang="#(defaults read ~/Library/Preferences/com.apple.HIToolbox.plist AppleCurrentKeyboardLayoutInputSourceID | awk -F. '{print $4}')"
      set-option -g status-right "#[fg=red,dim,bg=default] #(uptime | cut -f 4-5 -d ' ' | cut -f 1 -d ',') "
      set-option -ag status-right " #[fg=white,bg=default]%H:%M:%S"
      set-window-option -g window-status-style fg=colour244
      set-window-option -g window-status-style bg=default
      set-window-option -g window-status-format "#I #[underscore]#{?#{==:#{window_panes},1},,+}#[bold]#W#[nobold]:#{=|-24|…;s|$HOME|~|:pane_current_path}"
      set-window-option -g window-status-current-style fg=red
      set-window-option -g window-status-current-style bg=default
      set-window-option -g window-status-current-format "#[bold,fg=red]#W#[nobold]:#{=|-24|…;s|$HOME|~|:pane_current_path}"

      # smart-splits
      set -g @smart-splits_no_wrap "" # to disable wrapping. (any value disables wrapping)

      set -g @smart-splits_move_left_key  'C-h' # key-mapping for navigation.
      set -g @smart-splits_move_down_key  'C-j' #  --"--
      set -g @smart-splits_move_up_key    'C-k' #  --"--
      set -g @smart-splits_move_right_key 'C-l' #  --"--

      set -g @smart-splits_resize_left_key  'M-h' # key-mapping for resizing.
      set -g @smart-splits_resize_down_key  'M-j' #  --"--
      set -g @smart-splits_resize_up_key    'M-k' #  --"--
      set -g @smart-splits_resize_right_key 'M-l' #  --"--

    '';
  };

}
