# tooling: dnSpy

# HTTP User-Agent used for C2 connections
In method PostIt
Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15

# HTTP method used to submit the command execution output
As above, POST

# Key used to en/decrypt C2 data
In Decryptor method,
youcanthackthissupersecurec2keys

# First HTTP URL used by the malware
In JuicyTomaTOY/Program, Main we see
http://mcgreedysecretc2.thm/reg

# Hardcoded value used by sleep function
In Main method
```csharp
int count = 15000;
...
Program.Sleeper(count);
```
15 seconds.

# C2 command the attacker uses to execute cmds via cmd.exe
In Main method
shell

# Domain used to download another binary
In Main method
URL: http://stash.mcgreedy.thm/spykit.exe
domain: stash.mcgreedy.thm

