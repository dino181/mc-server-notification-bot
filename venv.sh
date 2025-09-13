#!/bin/bash

ENV_DIR=.venv
ENV=$ENV_DIR/bin/activate

if [ ! -f $ENV ]; then
	echo "Env does not exist. Creating new one in $ENV_DIR..."
	python3 -m venv $ENV_DIR 
fi

echo "Activating venv: $ENV"
source $ENV
