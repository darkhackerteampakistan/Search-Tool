#!/bin/bash

clear

echo "Installing JSON Search Tool..."

pkg update -y
pkg install python -y

pip install -r requirements.txt

echo "Installation Complete"

python search.py
