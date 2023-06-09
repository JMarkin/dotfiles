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

bind "\e[1~" beginning-of-line
bind "\e[4~" end-of-line
bind "\e[5~" beginning-of-history
bind "\e[6~" end-of-history
bind "\e[7~" beginning-of-line
bind "\e[3~" delete-char
bind "\e[2~" quoted-insert
bind "\e[5C" forward-word
bind "\e[5D" backward-word
bind "\e\e[C" forward-word
bind "\e\e[D" backward-word
bind "\e[1;5C" forward-word
bind "\e[1;5D" backward-word
bind "\e[8~" end-of-line
bind "\eOH" beginning-of-line
bind "\eOF" end-of-line
bind "\e[H" beginning-of-line
bind "\e[F" end-of-line

# PATH
set -e PATH

set -gx PATH /bin $PATH
set -gx PATH /sbin $PATH
set -gx PATH /usr/bin $PATH
set -gx PATH /usr/sbin $PATH
set -gx PATH /usr/local/bin $PATH
set -gx PATH /usr/local/sbin $PATH

set -gx PATH $HOME/go/bin $PATH
set -gx PATH $HOME/Android/platform-tools $PATH
set -gx PATH $HOME/scripts $PATH
set -gx PATH $HOME/.local/bin $PATH
set -gx PATH $HOME/.poetry/bin $PATH
set -gx PATH $HOME/.cargo/bin $PATH
set -gx PATH $HOME/.npm/bin $PATH
set -gx PATH /opt/cargo/bin $PATH


set -gx PYENV_ROOT "/opt/pyenv"
set -Ux PYTHON2 "$PYENV_ROOT/shims/python2"
set -Ux PYTHON3 "$PYENV_ROOT/shims/python3"

set -gx PATH $PYENV_ROOT/libexec/pyenv $PATH
set -gx PATH $PYENV_ROOT/libexec $PATH
set -gx PATH $PYENV_ROOT/shims $PATH
set -gx PATH $PYENV_ROOT/bin $PATH


set -gx PATH /usr/lib/ccache/bin/ $PATH


# ENVS

set -gx LANG C.UTF-8
set -gx LC_TYPE C.UTF-8
set -gx LC_ALL C.UTF-8

set -Ux OS (uname -s)

set -Ux LS_COLORS (vivid generate jellybeans)

set -Ux PYTHON_CONFIGURE_OPTS --enable-shared
set -Ux PYTHONPYCACHEPREFIX /tmp/cpython

set -Ux PAGER bat
set -Ux EDITOR nvim
set -Ux VISUAL nvim

set -Ux VAGRANT_DEFAULT_PROVIDER libvirt

set -Ux AUTOSWITCH_DEFAULT_REQUIREMENTS ~/scripts/base_py_reqs.txt

set -Ux BAT_THEME "Monokai Extended"

set -Ux pure_show_jobs true
set -Ux pure_show_system_time true

# set -Ux HTTP_PROXY http://169.254.0.1:3128
# set -Ux HTTPS_PROXY http://169.254.0.1:3131
# IF CACHE PROXY
# set -Ux CURL_CA_BUNDLE ""
set -Ux OPENSSL_CONF "/home/kron/.config/openssl.cnf"

# DISABLE TELEMETRY
set -Ux SCARF_ANALYTICS false
set -Ux DOTNET_CLI_TELEMETRY_OPTOUT 1

set -Ux npm_config_prefix $HOME/.npm

set fzf_preview_dir_cmd exa --all --color=always
set fzf_fd_opts --hidden

# ALIASES
function sudo
    command sudo -E $argv
end

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

function sudo
    command sudo -E $argv
end


function optimize-build-kron-pc
    set -gx CXXFLAGS "-O3 -march=znver3"
    set -gx CFLAGS "-O3 -march=znver3"
end

function optimize-build-mac-m1
    set -gx CXXFLAGS "-O3 -mcpu=apple-m1"
    set -gx CFLAGS "-O3 -mcpu=apple-m1"
end



if command -v pigz >/dev/null
    function gzip
        pigz $argv
    end
end

function vpn-ocn -a name
    source ~/.config/vpn/$name.fish
    set -l cmd (string join ' ' 'vpn-slice -vvv' $VPN_SLICE)
    echo $cmd
    sudo openconnect --os=win --local-hostname="yurymarkin.local" \
    --useragent="Cisco AnyConnect Secure Mobility Client Version 4.10.05111"\
    --version-string="4.10.05111"\
    --pid-file=/tmp/openconnect_$name.pid --background -u $VPN_USER $VPN_URL -s $cmd

    sudo systemctl restart dnsmasq
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


function _dotenv --on-variable PWD
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

function _switch_venv --on-variable PWD
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


# START LS utils

if command -v exa >/dev/null

    function ls
        exa --icons --classify --group-directories-first --time-style=long-iso --group --color=auto $argv
    end

    function l
        ls --git-ignore $argv
    end

    function la
        ls -a $argv
    end

    function ll
        ls --header --long $argv
    end

    function lla
        ll -a $argv
    end
end

# END LS utils


function backup_projects -d "backup_projects to yandex"
    rustic -P projects backup
end

function backup -d "backup to yandex"
    rustic -P projects backup
    rustic -P common backup
end

function flush_dns_cache -d "flush dns chache"
    sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
end

# pyenv init - | source
zoxide init --cmd cd fish | source
starship init fish | source


