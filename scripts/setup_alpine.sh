#!/bin/bash

cd $HOME

sudo chmod 700 ~/.ssh
sudo chmod 600 ~/.ssh/authorized_keys

sudo mkdir -p /opt && sudo chmod -R 777 /opt
sudo mkdir -p /projects && sudo chmod -R 777 /projects


# packages
sudo apk update && \
sudo apk add --no-cache alpine-sdk build-base bash sudo git curl fish nodejs \
lazygit btop htop openssh go cmake mold samurai clang clang-extra-tools llvm16 \
libtool pkgconf coreutils unzip gettext-tiny-dev shadow perl tree-sitter tree-sitter-cli \
gcc gdbm-dev libc-dev libffi libffi-dev libnsl-dev libtirpc-dev  \
make ncurses ncurses-dev openssl openssl-dev patch zlib-dev bzip2 bzip2-dev sqlite-dev xz-dev \
readline readline-dev rsync tmux musl-dev boost-dev sccache ctags npm docker \
bat starship ripgrep fd skim zoxide delta fzf procps

 sudo usermod -aG docker kron



export PYTHON_VERSION=3.11.6
export PYENV_ROOT=/opt/pyenv
export PATH=$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
export PYTHON_CONFIGURE_OPTS='--enable-optimizations --with-lto=full --with-computed-gotos --enable-ipv6 --enable-loadable-sqlite-extensions'
export PYTHON_CFLAGS='-O3 -march=native -fuse-ld=mold'

set -ex \
    && curl https://pyenv.run | bash \
    && pyenv update \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && pyenv rehash

eval "$(pyenv init -)"

pip install -U pip
pip install pynvim

export RUSTUP_HOME=/opt/rustup
export CARGO_HOME=/opt/cargo
export PATH=$CARGO_HOME/bin:$PATH

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
rustup default stable

cp ~/.config/alpine/cargo $CARGO_HOME/config

cargo install bob-nvim cargo-nextest du-dust ptags vivid eza rustic-rs cargo-update

bob install nightly
bob install stable
bob use nightly

export POETRY_HOME=/opt/poetry
curl -sSL https://install.python-poetry.org | python3 -

fish -c "curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher update"

