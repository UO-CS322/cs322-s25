#!/bin/bash

# If the venv directory does not exist, create it and install requirements. 
# Tested with python 3.10 - 3.13
if [ ! -d "venv" ]; then
    python3 -m venv venv
    venv/bin/pip install --upgrade pip
    venv/bin/pip install -r Duckies/requirements.txt
    echo "Successfully installed all requirements"
fi
