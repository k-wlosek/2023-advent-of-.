#!/bin/bash

cut -d ' ' -f2 access.log | sort | uniq -c | awk 'END {print NR}'

cut -d ' ' -f3 access.log | cut -d ':' -f1 | sort | uniq -c | awk 'END {print NR}'

python3 helper.py

cut -d ' ' -f3 access.log | cut -d ':' -f1 | sort | uniq -c | sort -n | tail -n 10

grep '#domain found in previous step' access.log | head -n 5

grep '#domain found in previous step' access.log | awk 'END {print NR}'

grep '#domain found in previous step' access.log | cut -d ' ' -f5 | cut -d '=' -f2 | base64 -d | grep "{"
