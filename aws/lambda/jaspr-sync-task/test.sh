#!/bin/bash
aws lambda invoke --function-name jaspr-sync-task --log-type Tail --payload file://data.json output.txt 
cat output.txt
rm output.txt
