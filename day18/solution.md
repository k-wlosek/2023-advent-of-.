
```bash
top
```
643 root 100%CPU a
`sudo kill 643`
respawned

```bash
systemctl list-unit-files | grep enabled
```
a-unkillable.service

```bash
systemctl status a-unkillable.service
```
Dec 19 13:53:59 tryhackme sudo[659]: Merry Christmas
Dec 19 13:56:01 tryhackme sudo[1813]: Merry Christmas

```bash
sudo systemctl stop a-unkillable.service
sudo systemctl disable a-unkillable.service

sudo rm -rf /etc/systemd/system/a
sudo rm -rf /etc/systemd/system/a-unkillable.service
```



# What is the name of the service that respawns the process after killing it?
a-unkillable.service

# What is the path from where the process and service were running?
/etc/systemd/system

# The malware prints a taunting message. When is the message shown? Choose from the options below.
# 1. Randomly
# 2. After a set interval
# 3. On process termination
# 4. None of the above
4
