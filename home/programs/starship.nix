{ config, lib, pkgs, ... }:
{
  programs.starship.enable = true;

  programs.starship.settings = {
    format = lib.concatStrings [
    "$time"
    "$username@$localip"
    "$memory_usage"
    "$directory"
    "$git_branch"
    "$git_state"
    "$git_status"
    "$cmd_duration"
    "$line_break"
    "$container"
    "$python"
    "$status"
    "$character"
    ];

    directory = {
      truncation_length = 3;
      truncate_to_repo = false;
    };

    character = {
      success_symbol = "[❯](purple)";
      error_symbol = "[❯](red)";
      vicmd_symbol = "[❮](green)";
    };

    git_branch = {
      format = "[$branch]($style)";
    };

    git_status = {
      format = "[[(*$conflicted$untracked$modified$staged$renamed$deleted)](218)($ahead_behind$stashed)]($style)";
    };

    git_state = {
      format = "\([$state( $progress_current/$progress_total)]($style)\) ";
    };

    cmd_duration = {
      format = "[$duration]($style) ";
    };

    python = {
      format = "[$virtualenv]($style) ";
    };

    time = {
      format = "[$time]($style)";
      disabled = false;
    };

    hostname = {
      format = "[$hostname]($style) ";
      ssh_only = false;
    };

    localip = {
      ssh_only = false;
      format = "[$localipv4]($style) ";
      disabled = false;
    };

    username = {
      format = "[$user]($style)";
      show_always = true;
    };

    memory_usage = {
      disabled = false;
      format = "[$ram]($style) ";
      threshold = -1;
    };

    status = {
      disabled = false;
    };
  };
}
