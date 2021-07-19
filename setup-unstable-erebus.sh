#! /bin/bash

echo "[Creating erebus configuration directory]"
mkdir -pv $HOME/.erebus/{config,keys}
echo "[Creating Erebus workspace directory]"
mkdir -pv $HOME/erebus/files
echo "[Installing requirements]"
pip install -r requirements.txt
echo "DONE"
