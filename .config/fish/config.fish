set -U fish_greeting

# COLORS
set -U fish_color_autosuggestion d7ffaf
set -U fish_color_cancel \x2d\x2dreverse
set -U fish_color_command 5fff00
set -U fish_color_comment 5C9900
set -U fish_color_cwd green
set -U fish_color_cwd_root red
set -U fish_color_end 8EEB00
set -U fish_color_error 60B9CE
set -U fish_color_escape 00a6b2
set -U fish_color_history_current \x2d\x2dbold
set -U fish_color_host normal
set -U fish_color_host_remote yellow
set -U fish_color_match \x2d\x2dbackground\x3dbrblue
set -U fish_color_normal normal
set -U fish_color_operator 00a6b2
set -U fish_color_param ffffaf
set -U fish_color_quote d75f5f
set -U fish_color_redirection 7CB02C
set -U fish_color_search_match bryellow\x1e\x2d\x2dbackground\x3dbrblack
set -U fish_color_selection white\x1e\x2d\x2dbold\x1e\x2d\x2dbackground\x3dbrblack
set -U fish_color_status red
set -U fish_color_user brgreen
set -U fish_color_valid_path \x2d\x2dunderline
set -U fish_key_bindings fish_default_key_bindings
set -U fish_pager_color_completion normal
set -U fish_pager_color_description B3A06D
set -U fish_pager_color_prefix normal\x1e\x2d\x2dbold\x1e\x2d\x2dunderline
set -U fish_pager_color_progress brwhite\x1e\x2d\x2dbackground\x3dcyan
set -U fish_pager_color_selected_background \x2d\x2dbackground\x3dbrblack


# BIND

# bind "\e[1~" beginning-of-line
# bind "\e[4~" end-of-line
# bind "\e[5~" beginning-of-history
# bind "\e[6~" end-of-history
# bind "\e[7~" beginning-of-line
# bind "\e[3~" delete-char
# bind "\e[2~" quoted-insert
# bind "\e[5C" forward-word
# bind "\e[5D" backward-word
# bind "\e\e[C" forward-word
# bind "\e\e[D" backward-word
# bind "\e[1;5C" forward-word
# bind "\e[1;5D" backward-word
# bind "\e[8~" end-of-line
# bind "\eOH" beginning-of-line
# bind "\eOF" end-of-line
# bind "\e[H" beginning-of-line
# bind "\e[F" end-of-line

# ROOTS

set -Ux PYENV_ROOT /opt/pyenv
set -Ux CARGO_HOME /opt/cargo
set -Ux RUSTUP_HOME /opt/rustup
set -Ux POETRY_HOME /opt/poetry
set -Ux GOPATH /opt/go
set -Ux PACKER_CONFIG_DIR /opt/packer
set -Ux PACKER_CACHE_DIR /images/packer_cache

# PATH
fish_add_path /bin
fish_add_path /sbin
fish_add_path /usr/bin
fish_add_path /usr/sbin
fish_add_path /usr/local/bin
fish_add_path /usr/local/zfs/bin
fish_add_path /usr/local/sbin
fish_add_path /opt/homebrew/bin
fish_add_path /opt/homebrew/sbin
fish_add_path /opt/local/bin

fish_add_path $HOME/Android/platform-tools
fish_add_path $HOME/scripts
fish_add_path $HOME/.local/bin
fish_add_path $HOME/.cargo/bin
fish_add_path $HOME/.npm/bin
fish_add_path $HOME/.gem/ruby/3.0.0/bin
fish_add_path $HOME/.nix-profile/bin
# fish_add_path $HOME/.local/share/bob/nvim-bin

fish_add_path $GOPATH/bin
fish_add_path $POETRY_HOME/bin
fish_add_path $CARGO_HOME/bin
fish_add_path $PYENV_ROOT/bin

fish_add_path /usr/lib/ccache/bin

# ENVS

set -gx LANG C.UTF-8
set -gx LC_TYPE C.UTF-8
set -gx LC_ALL C.UTF-8

set -Ux OS (uname -s)

set -Ux LS_COLORS (vivid generate $HOME/.config/bamboo.yml)

set -Ux PYTHON_CONFIGURE_OPTS '--enable-optimizations --with-lto=full --with-computed-gotos --enable-ipv6 --enable-loadable-sqlite-extensions'
set -Ux PYTHON_CFLAGS '-O3 -march=native -fuse-ld=mold'

set -Ux PYTHONPYCACHEPREFIX /tmp/cpython

set -Ux PAGER bat
set -Ux MANPAGER 'nvim +Man!'
set -Ux EDITOR nvim
set -Ux VISUAL nvim

set -Ux VAGRANT_DEFAULT_PROVIDER libvirt

set -Ux AUTOSWITCH_DEFAULT_REQUIREMENTS ~/scripts/base_py_reqs.txt

set -Ux BAT_THEME bamboo

set -Ux ROCM_PATH /opt/rocm

set -Ux pure_show_jobs true
set -Ux pure_show_system_time true

# set -Ux HTTP_PROXY http://169.254.0.1:3128
# set -Ux HTTPS_PROXY http://169.254.0.1:3131
# IF CACHE PROXY
# set -Ux CURL_CA_BUNDLE ""
set -Ux OPENSSL_CONF "/etc/openssl.cnf"

# DISABLE TELEMETRY
set -Ux SCARF_ANALYTICS false
set -Ux DOTNET_CLI_TELEMETRY_OPTOUT 1

set -Ux npm_config_prefix $HOME/.npm

set -Ux FZF_DEFAULT_OPTS '--bind=shift-tab:up,tab:down'

set fzf_fd_opts --hidden
fzf_configure_bindings --git_status=\cg --history=\cr --git_log=\cl --directory=\cf --variables= --processes=


# ALIASES

function win10
    sudo virsh start win10_small
end

function cat
    bat $argv
end

function grep
    rg $argv
end

function vim -d 'vim alias for nvim'
    nvim $argv
end

function v -d 'short alias for nvim'
    nvim $argv
end



function open-vim
    if test -d $argv[1]
        cd $argv[1]
        vim
    else
        vim $argv
    end
end

function set_docker -d 'set docker host'
    if count $argv >/dev/null
        set -Ux DOCKER_HOST $argv[1]
    else
        set -Ux DOCKER_HOST unix:///var/run/docker.sock
    end
end

if test -n "$KITTY_WINDOW_ID"
    function ssh
        kitty +kitten ssh $argv
    end
end

function change_ttl
    sudo sysctl -w net.inet.ip.ttl=65
end

function forward
    ssh -M -fNT $argv[1]
end


function optimize-build
    set -gx CFLAGS "-O3 -march=native -fuse-ld=mold"
    set -gx CXXFLAGS "$CFLAGS"
    set -gx CPPFLAGS "$CFLAGS"
end


if command -v pigz >/dev/null
    function gzip
        pigz $argv
    end
end

function vpn-ocn -a name
    source ~/.config/vpn/$name.fish
    set -l cmd (string join ' ' '/opt/pyenv/shims/vpn-slice -vvv' $VPN_SLICE)
    echo $cmd
    sudo openconnect \
        --useragent="AnyConnect" \
        --pid-file=/tmp/openconnect_$name.pid -u $VPN_USER $VPN_URL -s $cmd

end

function vpn-ocn-down -a name
    sudo kill -INT (cat /tmp/openconnect_$name.pid)
end

# AUTODOTENV
function sourcedotenv
    set -gx DOTENV_WORK_DIR $PWD

    for i in (cat $DOTENV_WORK_DIR/.env)
        if test (echo $i | sed -E 's/^[[:space:]]*(.).+$/\\1/g') != "#"
            set arr (echo $i |tr = \n)
            if test $arr[1] != ""
                set -l value (echo $arr[2])
                set -gx $arr[1] $value
            end
        end
    end
end

function unsourcedotenv
    for i in (cat $DOTENV_WORK_DIR/.env)
        if test (echo $i | sed -E 's/^[[:space:]]*(.).+$/\\1/g') != "#"
            set arr (echo $i |tr = \n)
            if test $arr[1] != ""
                set -e $arr[1]
            end
        end
    end
    set -e DOTENV_WORK_DIR
end


function _dotenv --on-event fish_prompt --on-variable PWD
    if test -f .env && test -z $DOTENV_WORK_DIR
        sourcedotenv
        return
    end

    if test -z $DOTENV_WORK_DIR
        return
    end

    if not string match -q -- "*$DOTENV_WORK_DIR*" $PWD
        unsourcedotenv
        set -e DOTENV_WORK_DIR
    end

end

# _dotenv

# END AUTODOTENV

# AUTOVENV
function _activate
    source (head -n 1 .venv)/bin/activate.fish
end

function _create_poetry_venv
    poetry install $argv
    set -l venv_path (poetry env list --full-path | sort -k 2 | tail -n 1 | cut -d' ' -f1)
    echo "$venv_path" >.venv
    _activate
end


function _create_pdm_venv
    pdm install $argv
    set -l venv_path (dirname $(dirname $(pdm config python.path)))
    echo "$venv_path" >.venv
    _activate
end

function _create_virtualenv
    set -l venv_path $HOME/.virtualenvs/(basename $PWD)
    if command -v virtualenv
        virtualenv $venv_path
    else
        python -m venv $venv_path
    end
    echo "$venv_path" >.venv
    _activate
end

function mkvenv
    _dotenv
    set -gx VENV_WORK_DIR $PWD
    if test -f .venv
        _activate
        return
    else
        if test -z $VIRTUAL_ENV
            echo "$VIRTUAL_ENV" >.venv
        end
    end

    if test -f poetry.lock
        _create_poetry_venv
        # else if test -f pdm.lock
        #     _create_pdm_venv
    else
        _create_virtualenv
    end

end

function rmvenv
    set -e VENV_WORK_DIR
    if not test -f .venv
        return
    end

    set -l venv_path (head -n 1 .venv)
    deactivate
    rm -rf $venv_path
    rm -f .venv
end

function _switch_venv --on-event fish_prompt --on-variable PWD
    if test -f .venv && test -z $VIRTUAL_ENV
        mkvenv
        return
    end

    if test -z $VIRTUAL_ENV
        return
    end

    if not string match -q -- "$VENV_WORK_DIR*" $PWD
        deactivate
    end
end

# _switch_venv

if test -n $VIRTUAL_ENV
    set -gx PATH $VIRTUAL_ENV/bin $PATH
end

# END AUTOVENV


function flush_dns_cache -d "flush dns chache"
    sudo dscacheutil -flushcache
    sudo killall -HUP mDNSResponder
end

function yy
    set tmp (mktemp -t "yazi-cwd.XXXXXX")
    yazi $argv --cwd-file="$tmp"
    if set cwd (cat -- "$tmp"); and [ -n "$cwd" ]; and [ "$cwd" != "$PWD" ]
        cd "$cwd"
    end
    rm -f -- "$tmp"
end


if test -z "$SSH_AUTH_SOCK"
    if command -v ssh-agent >/dev/null
        eval (ssh-agent -c) >/dev/null
        set -Ux SSH_AUTH_SOCK $SSH_AUTH_SOCK
        set -Ux SSH_AGENT_PID $SSH_AGENT_PID
    end
end


if status --is-interactive
    zoxide init --cmd cd fish | source
    starship init fish | source
end
