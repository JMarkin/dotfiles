FROM alpine

RUN adduser -s /usr/bin/fish -D kron && \
    mkdir -p /etc/sudoers.d && \
    echo "kron ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/kron && \
    chmod 0440 /etc/sudoers.d/kron && \
    mkdir -p /opt && chmod -R 777 /opt

RUN apk update && \
    apk add --no-cache alpine-sdk build-base bash sudo git curl fish nodejs \
    lazygit btop htop openssh-client-common go cmake \
    libtool pkgconf coreutils unzip gettext-tiny-dev shadow perl tree-sitter tree-sitter-cli \
    gcc gdbm-dev libc-dev libffi libffi-dev libnsl-dev libtirpc-dev  \
    make ncurses ncurses-dev openssl openssl-dev patch zlib-dev bzip2 bzip2-dev sqlite-dev xz-dev \
    readline readline-dev rsync tmux musl-dev boost-dev samurai sccache ctags npm \
    bat starship exa ripgrep fd skim zoxide delta docker-cli docker-cli-compose && \
    apk add --no-cache vivid --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/

USER kron
ENV HOME=/home/kron
ENV SHELL /usr/bin/fish
WORKDIR $HOME


ENV PYTHON_VERSION 3.10.11
ENV PYENV_ROOT /opt/pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
ENV PYTHON_CONFIGURE_OPTS --enable-shared

# Install pyenv
RUN set -ex \
    && curl https://pyenv.run | bash \
    && pyenv update \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && pyenv rehash

ENV RUSTUP_HOME /opt/rustup
ENV CARGO_HOME /opt/cargo
ENV PATH ${CARGO_HOME}/bin:$PATH

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    rustup default stable


RUN git clone -b nightly https://github.com/neovim/neovim.git && \
    cd neovim && \
    make CMAKE_BUILD_TYPE=Release && \
    sudo make install && \
    cd ../ && sudo rm -rf neovim

COPY --chown=kron . $HOME

ENV POETRY_HOME=/opt/poetry

RUN fish -c "curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && \
    fisher update && \
    pip install -U pip && \
    pip install pynvim && \
    curl -sSL https://install.python-poetry.org | python3 -"

RUN git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm && \
    ~/.tmux/plugins/tpm/bin/install_plugins

RUN nvim --headless "+Lazy! sync" +qa
RUN nvim --headless "+Lazy! sync" +qa
RUN nvim "+InstallDefault" +qa

VOLUME $HOME
ENV TERM xterm-256color
ENTRYPOINT [ "/usr/bin/fish" ]
