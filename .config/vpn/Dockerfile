FROM alpine:latest

ENV PYTHON_VERSION 3.10.11

RUN apk update && \
    apk add --no-cache alpine-sdk build-base bash sudo git curl fish nodejs \
    lazygit btop openssh openssh-client-common go cmake \
    libtool pkgconf coreutils unzip gettext-tiny-dev starship shadow perl tree-sitter tree-sitter-cli \
    gcc gdbm-dev libc-dev libffi libffi-dev libnsl-dev libtirpc-dev  \
    make ncurses ncurses-dev openssl openssl-dev patch zlib-dev bzip2 bzip2-dev sqlite-dev xz-dev \
    readline readline-dev rsync tmux musl-dev boost-dev samurai sccache ctags

RUN adduser -s /usr/bin/fish -D kron && \
    mkdir -p /etc/sudoers.d && \
    echo "kron ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/kron && \
    chmod 0440 /etc/sudoers.d/kron

USER kron
ENV HOME=/home/kron
ENV SHELL /usr/bin/fish
WORKDIR $HOME


# Set-up necessary Env vars for PyEnv
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
ENV PYTHON_CONFIGURE_OPTS --enable-shared

# Install pyenv
RUN set -ex \
    && curl https://pyenv.run | bash \
    && pyenv update \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && pyenv rehash

ENV PATH ${HOME}/.cargo/bin:$PATH

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    rustup default stable && \
    rustup component add rust-analyzer && \
    cargo install --locked cargo-update \
    vivid \
    zoxide \
    fd-find \
    exa \
    bat \
    starship \
    ripgrep \
    skim \
    git-delta \
    ptags

COPY --chown=kron . $HOME

RUN fish -c "curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && \
    fisher update"

RUN git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm && \
    ~/.tmux/plugins/tpm/bin/install_plugins

RUN git clone -b nightly https://github.com/neovim/neovim.git && \
    cd neovim && \
    make CMAKE_BUILD_TYPE=Release && \
    sudo make install && \
    cd ../ && rm -rf neovim


RUN nvim --headless "+Lazy! sync" +qa
RUN nvim --headless "+lua require('plugins.treesitter').ts_install()" +qa
RUN nvim --headless "+lua require('plugins.nullls').install_default()" +qa

VOLUME $HOME

