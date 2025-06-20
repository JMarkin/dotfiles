{ config, lib, pkgs, ... }:
{
  programs.starship.enable = true;

  programs.starship.enableTransience = true;
  programs.starship.settings = {
    format = lib.concatStrings [
      "$time"
      "$username@$hostname($localip)"
      "$directory"
      "$git_branch"
      "$git_state"
      "$git_status"
      "$cmd_duration"
      "$line_break"
      "$all"
      "$line_break"
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


    git_state = {
      disabled = false;
      format = "\\([$state( $progress_current/$progress_total)]($style)\\) ";
    };
    git_status.disabled = false;
    cmd_duration.disabled = false;


    time = {
      disabled = false;
      format = "[$time]($style) ";
    };

    hostname = {
      format = "[$hostname]($style)";
      ssh_only = false;
    };

    localip = {
      ssh_only = false;
      format = "[$localipv4]($style) ";
      disabled = false;
    };

    username = {
      show_always = true;
    };

    memory_usage = {
      disabled = false;
    };

    status.disabled = false;

    battery.disabled = true;
    os.disabled = true;

    aws.format = "\\[[$symbol($profile)(\\($region\\))(\\[$duration\\])]($style)\\]";

    bun.format = "\\[[$symbol($version)]($style)\\]";

    c.format = "\\[[$symbol($version(-$name))]($style)\\]";

    cmake.format = "\\[[$symbol($version)]($style)\\]";


    cobol.format = "\\[[$symbol($version)]($style)\\]";

    conda.format = "\\[[$symbol$environment]($style)\\]";

    crystal.format = "\\[[$symbol($version)]($style)\\]";

    daml.format = "\\[[$symbol($version)]($style)\\]";

    dart.format = "\\[[$symbol($version)]($style)\\]";

    deno.format = "\\[[$symbol($version)]($style)\\]";

    docker_context.format = "\\[[$symbol$context]($style)\\]";

    dotnet.format = "\\[[$symbol($version)(🎯 $tfm)]($style)\\]";

    elixir.format = "\\[[$symbol($version \\(OTP $otp_version\\))]($style)\\]";

    elm.format = "\\[[$symbol($version)]($style)\\]";

    erlang.format = "\\[[$symbol($version)]($style)\\]";

    fennel.format = "\\[[$symbol($version)]($style)\\]";

    fossil_branch.format = "\\[[$symbol$branch]($style)\\]";

    gcloud.format = "\\[[$symbol$account(@$domain)(\\($region\\))]($style)\\]";

    git_branch.format = "\\[[$symbol$branch]($style)\\]";

    git_status.format = "([\\[$all_status$ahead_behind\\]]($style))";

    golang.format = "\\[[$symbol($version)]($style)\\]";

    gradle.format = "\\[[$symbol($version)]($style)\\]";

    guix_shell.format = "\\[[$symbol]($style)\\]";

    haskell.format = "\\[[$symbol($version)]($style)\\]";

    haxe.format = "\\[[$symbol($version)]($style)\\]";

    helm.format = "\\[[$symbol($version)]($style)\\]";

    hg_branch.format = "\\[[$symbol$branch]($style)\\]";

    java.format = "\\[[$symbol($version)]($style)\\]";

    julia.format = "\\[[$symbol($version)]($style)\\]";

    kotlin.format = "\\[[$symbol($version)]($style)\\]";

    kubernetes.format = "\\[[$symbol$context( \\($namespace\\))]($style)\\]";

    lua.format = "\\[[$symbol($version)]($style)\\]";

    memory_usage.format = "\\[$symbol[$ram( | $swap)]($style)\\]";

    meson.format = "\\[[$symbol$project]($style)\\]";

    nim.format = "\\[[$symbol($version)]($style)\\]";

    nix_shell.format = "\\[[$symbol$state( \\($name\\))]($style)\\]";

    nodejs.format = "\\[[$symbol($version)]($style)\\]";

    ocaml.format = "\\[[$symbol($version)(\\($switch_indicator$switch_name\\))]($style)\\]";

    opa.format = "\\[[$symbol($version)]($style)\\]";

    openstack.format = "\\[[$symbol$cloud(\\($project\\))]($style)\\]";

    os.format = "\\[[$symbol]($style)\\]";

    package.format = "\\[[$symbol$version]($style)\\]";

    perl.format = "\\[[$symbol($version)]($style)\\]";

    php.format = "\\[[$symbol($version)]($style)\\]";

    pijul_channel.format = "\\[[$symbol$channel]($style)\\]";

    pulumi.format = "\\[[$symbol$stack]($style)\\]";

    purescript.format = "\\[[$symbol($version)]($style)\\]";

    python.format = "\\[[$symbol$pyenv_prefix($version})(\\($virtualenv\\))]($style)\\]";

    raku.format = "\\[[$symbol($version-$vm_version)]($style)\\]";

    red.format = "\\[[$symbol($version)]($style)\\]";

    ruby.format = "\\[[$symbol($version)]($style)\\]";

    rust.format = "\\[[$symbol($version)]($style)\\]";

    scala.format = "\\[[$symbol($version)]($style)\\]";

    spack.format = "\\[[$symbol$environment]($style)\\]";

    sudo.format = "\\[[as $symbol]($style)\\]";

    swift.format = "\\[[$symbol($version)]($style)\\]";

    terraform.format = "\\[[$symbol$workspace]($style)\\]";

    vagrant.format = "\\[[$symbol($version)]($style)\\]";

    vlang.format = "\\[[$symbol($version)]($style)\\]";

    zig.format = "\\[[$symbol($version)]($style)\\]";

    solidity.format = "\\[[$symbol($version)]($style)\\]";
  };
}
