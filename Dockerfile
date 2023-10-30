FROM alpine

RUN apk update && apk add sudo && adduser -D kron && \
    mkdir -p /etc/sudoers.d && \
    echo "kron ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/kron && \
    chmod 0440 /etc/sudoers.d/kron && \
    mkdir -p /opt && chmod -R 777 /opt

USER kron
ENV HOME=/home/kron

WORKDIR /home/kron

COPY --chown=kron . .

RUN ./scripts/setup_alpine.sh
