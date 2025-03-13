#! /bin/bash
SCRIPT_NAME=$1
WORKDIR="./jobs"
RAY_ADDRESS="http://127.0.0.1:8265"


if [ -z "$SCRIPT_NAME" ]; then
  echo "Usage: submit-job.sh job.py # [job.py located in ./jobs]"
  exit 1
fi


ray job submit --working-dir $WORKDIR --address $RAY_ADDRESS -- python $SCRIPT_NAME 
