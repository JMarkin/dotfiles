set fish_greeting

if status is-interactive
    # Commands to run in interactive sessions can go here
end

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


# ENVS

set -Ux OS (uname -s)

set -Ux LS_COLORS (vivid generate jellybeans)

set -Ux PYTHON_CONFIGURE_OPTS --enable-shared
set -Ux PYTHONPYCACHEPREFIX /tmp/cpython

set -Ux PAGER bat
set -Ux EDITOR nvim
set -Ux VISUAL nvim

set -Ux VAGRANT_DEFAULT_PROVIDER libvirt

set -Ux AUTOSWITCH_DEFAULT_REQUIREMENTS $HOME/scripts/base_py_reqs.txt

set -Ux BAT_THEME "TwoDark"

set -Ux pure_show_jobs true
set -Ux pure_show_system_time true


set -gx PYENV_ROOT "$HOME/.pyenv"
set -Ux PYTHON2 "$HOME/.pyenv/shims/python2"
set -Ux PYTHON3 "$HOME/.pyenv/shims/python3"

# set -Ux HTTP_PROXY http://169.254.0.1:3128
# set -Ux HTTPS_PROXY http://169.254.0.1:3131
# set -Ux CURL_CA_BUNDLE ""
set -Ux OPENSSL_CONF "/home/kron/.config/openssl.cnf"

# DISABLE TELEMETRY
set -Ux SCARF_ANALYTICS false
set -Ux DOTNET_CLI_TELEMETRY_OPTOUT 1

set -Ux npm_config_prefix $HOME/.npm

# PATH
set -e PATH

set -gx PATH /bin $PATH
set -gx PATH /usr/bin $PATH
set -gx PATH /usr/local/bin $PATH
set -gx PATH /usr/local/sbin $PATH

set -gx PATH $HOME/go/bin $PATH
set -gx PATH $HOME/Android/platform-tools $PATH
set -gx PATH $HOME/scripts $PATH
set -gx PATH $HOME/.local/bin $PATH
set -gx PATH $HOME/.poetry/bin $PATH
set -gx PATH $HOME/.cargo/bin $PATH
set -gx PATH $HOME/.npm/bin $PATH

set -gx PATH $PYENV_ROOT/libexec/pyenv $PATH
set -gx PATH $PYENV_ROOT/libexec $PATH
set -gx PATH $PYENV_ROOT/shims $PATH
set -gx PATH $PYENV_ROOT/bin $PATH


set -gx PATH /usr/lib/ccache/bin/ $PATH


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

if test -n "$WEZTERM_PANE"
    function ssh
        wezterm ssh $argv
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

function openconnect -a name
    source ~/.config/vpn/$name.fish
    set -l cmd (string join ' ' 'vpn-slice -vvv' $VPN_SLICE)
    echo $cmd
    sudo openconnect --os=win --local-hostname="yurymarkin.local" \
    --useragent="Cisco AnyConnect Secure Mobility Client Version 4.10.05111"\
    --version-string="4.10.05111"\
    --pid-file=/tmp/openconnect_$name.pid --background -u $VPN_USER $VPN_URL -s $cmd
end

function openconnect-down -a name
    sudo kill -INT (cat /tmp/openconnect_$name.pid)
end



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
    if test -f .venv
        _activate
        return
    end

    if test -f poetry.lock
        _create_poetry_venv
    else
        _create_virtualenv
    end

end

function rmvenv
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

    if not string match -q -- "*$VIRTUAL_ENV*" $PWD
        deactivate
    end
end

# _switch_venv

if test -n $VIRTUAL_ENV
    set -gx PATH $VIRTUAL_ENV/bin $PATH
end

# END AUTOVENV

# AUTODOTENV
function sourcedotenv
    set -g DOTENV_WORK_DIR $PWD

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

pyenv init - | source
starship init fish | source
