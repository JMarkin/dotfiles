#!/usr/bin/env bash

NAME=$1
PIP_ARGS=$2
BIN_NAME=$3

mkdir -p "${HOME}"/.local/bin
mkdir -p "${HOME}"/.local/share/py

VENV="${HOME}/.local/share/py/${NAME}"
if [[ -z $BIN_NAME ]]; then
    BIN="${HOME}/.local/bin/${NAME}"
    VENV_BIN="${VENV}/bin/${NAME}"
else
    VENV_BIN="${VENV}/bin/${BIN_NAME}"
    BIN="${HOME}/.local/bin/${BIN_NAME}"
fi


echo "remove previous ${BIN} ${VENV}"
rm -rf "${BIN}" "${VENV}"

echo "create venv ${VENV}"
python -m venv --copies "${VENV}"
#ls "${HOME}"/.local/share/py

echo "install ${NAME}"
"${VENV}"/bin/pip install -U pip
"${VENV}"/bin/pip install -U "${NAME}" "${PIP_ARGS}"

echo "link binary ${VENV_BIN} -> ${BIN}"
ln -s "${VENV_BIN}" "${BIN}"


