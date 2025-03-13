#! /bin/bash
SCRIPT_NAME=$1
WORKDIR="./jobs"
export RAY_ADDRESS="http://raycluster-kuberay-head-svc.svc.cluster.local:8265"


if [ -z "$SCRIPT_NAME" ]; then
  echo "Usage: submit-job.sh job.py # [job.py located in ./jobs]"
  exit 1
fi


ray job submit --working-dir $WORKDIR --no-wait -- python $SCRIPT_NAME 
