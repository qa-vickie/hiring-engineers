#!/bin/bash

DD_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
echo $DD_DIR

cp ${DD_DIR}/checks.d/vickie_test.py  /etc/dd-agent/checks.d/vickie_test.py
cp ${DD_DIR}/conf.d/vickie_test.yaml  /etc/dd-agent/conf.d/vickie_test.yaml
 
