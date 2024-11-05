#!/usr/bin/env bash

cd /opt
rm -rf lua-language-server
git clone -b 3.10.4 https://github.com/LuaLS/lua-language-server
cd lua-language-server
./make.sh
mkdir -p ~/.local/bin
cd ~/.local/bin
rm -f lua-language-server
curl -o lua-language-server https://gist.githubusercontent.com/JMarkin/b6db04a6660bf8b65cd02937057fccc0/raw/2d2a0a2977e373d43b8ae3c7a30a82f88b83464b/lua-language-server
chmod +x ./lua-language-server
