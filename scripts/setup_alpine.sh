#!/bin/bash

USER=${USER:-root}

cd $HOME

sudo chmod 700 ~/.ssh
sudo chmod 600 ~/.ssh/authorized_keys

sudo mkdir -p /opt && sudo chmod -R 777 /opt
sudo mkdir -p /projects && sudo chmod -R 777 /projects


# packages
sudo apk update && \
sudo apk add --no-cache alpine-sdk build-base bash sudo git curl fish nodejs \
lazygit htop openssh go cmake mold samurai clang clang-extra-tools llvm16 \
libtool pkgconf coreutils unzip gettext-tiny-dev shadow perl tree-sitter tree-sitter-cli \
gcc gdbm-dev libc-dev libffi libffi-dev libnsl-dev libtirpc-dev  \
make ncurses ncurses-dev openssl openssl-dev patch zlib-dev bzip2 bzip2-dev sqlite-dev xz-dev \
readline readline-dev rsync tmux musl-dev boost-dev sccache ctags npm docker \
bat starship ripgrep fd zoxide delta fzf procps mandoc man-pages docker-cli-compose python3 py3-pip

sudo usermod -aG docker ${USER}


git clone https://github.com/neovim/neovim.git /opt/neovim
cd /opt/neovim
make CMAKE_BUILD_TYPE=Release
sudo make install
cd -


export PYENV_ROOT=/opt/pyenv
export PATH=$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

set -ex \
    && curl https://pyenv.run | bash \
    && pyenv update \
    && pyenv rehash

export RUSTUP_HOME=/opt/rustup
export CARGO_HOME=/opt/cargo
export PATH=$CARGO_HOME/bin:$PATH

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
rustup default stable

cp ~/.config/alpine/cargo $CARGO_HOME/config

cargo install cargo-nextest du-dust ptags vivid eza rustic-rs cargo-update

cargo install --locked --git https://github.com/sxyazi/yazi.git yazi-fm

export POETRY_HOME=/opt/poetry
curl -sSL https://install.python-poetry.org | python3 -

fish -c "curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher update"
fish -c "bat cache --build"

