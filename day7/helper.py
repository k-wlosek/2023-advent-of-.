#!/usr/bin/env python3

domains = {}

with open('access.log') as f:
    for line in f:
        split = line.split(" ")
        domain = split[2].split(":")[0]
        status_code = split[5]
        if domain in domains:
            cnt = domains[domain][0]
            domains[domain] = (cnt + 1, status_code)
        else:
            domains[domain] = (1, status_code)
print(sorted(domains,key=lambda x: x[1][0]))