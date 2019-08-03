#!/bin/bash
zip lambda_function.zip lambda_function.py
aws lambda update-function-code --function-name jaspr-sync-task --zip-file fileb://lambda_function.zip
rm lambda_function.zip
