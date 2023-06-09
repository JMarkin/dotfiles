FROM alpine

RUN adduser -s /usr/bin/fish -D kron && \
    mkdir -p /etc/sudoers.d && \
    echo "kron ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/kron && \
    chmod 0440 /etc/sudoers.d/kron && \
    mkdir -p /opt && chmod -R 777 /opt

RUN apk update && \
    apk add --no-cache build-base bash sudo git curl fish nodejs \
    lazygit btop unzip gettext tree-sitter tree-sitter-cli \
    gcc make openssl ctags npm re2 re2-dev \
    bat starship exa ripgrep fd skim zoxide delta neovim openssh-client-common \
    samurai python3 python3-dev py3-pip && \
    apk add --no-cache vivid --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/ && \
    pip install -U pip && \
    pip install pynvim pyre2

USER kron
ENV HOME=/home/kron
ENV SHELL /usr/bin/fish
WORKDIR $HOME

COPY --chown=kron . $HOME

RUN fish -c "curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && \
    fisher update"

RUN nvim --headless "+Lazy! sync" +qa

VOLUME $HOME
ENV TERM xterm-256color
ENTRYPOINT [ "/usr/bin/fish" ]
