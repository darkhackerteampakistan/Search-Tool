#!/bin/bash

clear

echo "Installing JSON Search Tool..."

pkg update -y
pkg install python -y

echo "Starting Tool..."

python search.py
