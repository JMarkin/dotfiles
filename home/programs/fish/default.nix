{ config, lib, pkgs, ... }:

{
  programs.tmux.shell = "${pkgs.fish}/bin/fish";

  home.file = {
    ".config/fish/conf.d/ssh_agent_start.fish".source = ./ssh_agent_start.fish;
  };

  home.sessionPath = [
    "$HOME/.local/bin"
  ];

  home.sessionVariables = {
    fish_color_autosuggestion = "d7ffaf";
    fish_color_cancel = "\x2d\x2dreverse";
    fish_color_command = "5fff00";
    fish_color_comment = "5C9900";
    fish_color_cwd = "green";
    fish_color_cwd_root = "red";
    fish_color_end = "8EEB00";
    fish_color_error = "60B9CE";
    fish_color_escape = "00a6b2";
    fish_color_history_current = "\x2d\x2dbold";
    fish_color_host = "normal";
    fish_color_host_remote = "yellow";
    fish_color_match = "\x2d\x2dbackground\x3dbrblue";
    fish_color_normal = "normal";
    fish_color_operator = "00a6b2";
    fish_color_param = "ffffaf";
    fish_color_quote = "d75f5f";
    fish_color_redirection = "7CB02C";
    fish_color_search_match = "bryellow\x1e\x2d\x2dbackground\x3dbrblack";
    fish_color_selection = "white\x1e\x2d\x2dbold\x1e\x2d\x2dbackground\x3dbrblack";
    fish_color_status = "red";
    fish_color_user = "brgreen";
    fish_color_valid_path = "\x2d\x2dunderline";
    fish_key_bindings = "fish_vi_key_bindings";
    fish_pager_color_completion = "normal";
    fish_pager_color_description = "B3A06D";
    fish_pager_color_prefix = "normal\x1e\x2d\x2dbold\x1e\x2d\x2dunderline";
    fish_pager_color_progress = "brwhite\x1e\x2d\x2dbackground\x3dcyan";
    fish_pager_color_selected_background = "\x2d\x2dbackground\x3dbrblack";

  };

  programs.fish = {
    enable = true;
    shellAliases = {
      cat = "bat";
      y = "yazi";
      # grc = "cgrc";
      grep = "rg";
      jq = "jaq";
      vim = "nvim";
      v = "nvim";
      vi = "nvim";
      change_ttl = "sudo sysctl -w net.inet.ip.ttl=65";
      forward = "ssh -M -fNT";
      gzip = "pigz";
      ls = "eza --icons --classify --group-directories-first --group --color=auto";
      l = "ls --git-ignore";
      la = "ls -a $argv";
      ll = "ls --header -l --time-style=long-iso -M -m";
      lla = "ll -a";
      rustic = "rustic -P ~/.config/rustic.toml";
    };
    plugins = [
      # { name = "grc"; src = pkgs.fishPlugins.grc.src; }
      {
        name = "cd-ls.fish";
        src = pkgs.fetchFromGitHub {
          owner = "mattmc3";
          repo = "cd-ls.fish";
          rev = "6133dcd09c53f9c39d0476bd4a58f4a05481e482";
          hash = "sha256-/7VVGZYaPbaGH2HZHMhpyMzkzZoM9/1CehijAzUlCis=";
        };
      }
      {
        name = "docker-fish-completions";
        src = pkgs.fetchFromGitHub {
          owner = "ankitsumitg";
          repo = "docker-fish-completions";
          rev = "6ea1444cbbe73bcba2f2ec7fc338c5ead924c6bf";
          hash = "sha256-AyT2D3sWxzf2K5bbH24dbEn7AdB7IVljUtp2YGHGRmY=";
        };
      }
      {
        name = "replay.fish";
        src = pkgs.fetchFromGitHub {
          owner = "jorgebucaran";
          repo = "replay.fish";
          rev = "d2ecacd3fe7126e822ce8918389f3ad93b14c86c";
          hash = "sha256-TzQ97h9tBRUg+A7DSKeTBWLQuThicbu19DHMwkmUXdg=";
        };
      }
      {
        name = "fish-eza";
        src = pkgs.fetchFromGitHub {
          owner = "plttn";
          repo = "fish-eza";
          rev = "36f57936ba3e921334ee313b25c3988258fb9771";
          hash = "sha256-f/JmwxOnLHq/FXIxI424AfOavlmv5/Ep5D2JEm0jFPE=";
        };
      }
      {
        name = "fish-kubectl-completions";
        src = pkgs.fetchFromGitHub {
          owner = "evanlucas";
          repo = "fish-kubectl-completions";
          rev = "ced676392575d618d8b80b3895cdc3159be3f628";
          hash = "sha256-OYiYTW+g71vD9NWOcX1i2/TaQfAg+c2dJZ5ohwWSDCc=";
        };
      }
    ];

    loginShellInit = /* bash */''
      if test -z "$SSH_AUTH_SOCK"
          if command -v ssh-agent >/dev/null
              eval (ssh-agent -c) >/dev/null
              set -Ux SSH_AUTH_SOCK $SSH_AUTH_SOCK
              set -Ux SSH_AGENT_PID $SSH_AGENT_PID
          end
      end

    '';

    interactiveShellInit = /*fish*/''
      set fish_greeting
      set -U fzf_fd_opts --hidden
      set -U fzf_preview_dir_cmd eza --all --color=always
      # set -U grc_plugin_ignore_execs ls cat
    '';

    functions = {
      set_docker.body = /*fish*/''
        if count $argv >/dev/null
            set -gx DOCKER_HOST $argv[1]
        else
            set -gx DOCKER_HOST unix:///var/run/docker.sock
        end
      '';
      open-vim.body = /*fish*/''
        if test -d $argv[1]
            cd $argv[1]
            vim
        else
            vim $argv
        end
      '';
      shh = /*fish*/ ''
        if [ -t 0 ]
            set CONTEXT ""
        else
            while read i; set CONTEXT "$CONTEXT""$i"\n; end
        end

        set -l QUERY $argv
        set -l PROMPT "$QUERY\n$CONTEXT"
        set -l OLLAMA_URL $OLLAMA_URL "http://localhost:11434"
        set -l SHELL_HELPER_MODEL $SHELL_HELPER_MODEL "shell-helper:latest"

        set -l PROMPT (echo "$PROMPT" | jaq -Rs)

        set -l CURL_DATA '{
            "model": "'$SHELL_HELPER_MODEL'",
            "stream": false,
            "prompt": '$PROMPT'
        }'

        curl -H "Content-Type: application/json" -H "Accept: application/json" \
            -s $OLLAMA_URL"/api/generate" \
            --data $CURL_DATA \
            | jaq -r '.response' | xargs -0 printf "%b"
      '';
    };
  };
}
