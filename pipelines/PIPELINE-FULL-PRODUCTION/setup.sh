#!/bin/bash

set -x
python3.7 -m venv todo-list-aws
source todo-list-aws/bin/activate
python -m pip install --upgrade pip
python -m pip install awscli~=1.27.0
python -m pip install aws-sam-cli~=1.67.0
# For integration testing
python -m pip install pytest~=7.2.0
python -m pip install --force-reinstall cryptography~=38.0.0
pwd