#!/bin/bash

/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files avg_mapper.py,avg_reducer.py \
-input /mapreduce/averages/assignment_test.txt \
-output /mapreduce/averages/output03 \
-mapper avg_mapper.py \
-reducer avg_reducer.py 

