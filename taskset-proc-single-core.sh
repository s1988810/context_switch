#!/bin/bash
# Taskset cs_test process to a single core specifically to core 0 

pId=`pgrep cs_test`

#get the process id from the pId variable

while read -r line
do
    taskset -pc 0 $line

done < <(pId)



