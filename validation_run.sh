#!/bin/bash

#clean previous executable
make clean

#make all
make all

#remove previous systemtap result file
sudo rm out

#run test along with systemtap tracing functionality
sudo stap context_switch.stp -o out -c './cs_test 100000'

#parse output of systemtap
python3 ./context_switch.py out
 
