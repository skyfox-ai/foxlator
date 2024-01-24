#!/bin/bash

parent_dir=$(dirname "$0")
venv=$parent_dir/../venv
src_dir=$parent_dir/../src

source $venv/bin/activate
PYTHONPATH=$src_dir python3.10 $src_dir/foxlator/__main__.py $*
deactivate
