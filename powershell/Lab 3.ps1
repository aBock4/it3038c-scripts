#function to get the IPv4Address of the host-machine
function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

#set the ipaddress to a variable
$IP = getIP

#set the current user to a variable
$user = $env:USERNAME

#set the hostname to a variable
$hostname = hostname

#set the Powershell version to a variable
$POWERSHELL = $HOST.Version.Major

#set the current date to a variable
$date = Get-Date -Format "dddd MM/dd/yyyy"

#set ipaddress, user, hostname, powershell version, and date to a variable with a friendly message
$BODY = "This machine's IP address is {0}" -f $IP + ". The current user is " + $user + ". The hostname is " + $hostname + ". The Powershell Version is: " + $POWERSHELL + ". Today's date is " + $date + "."

#send an email with all of the $BODY attributes
Send-MailMessage -To "leonardf@ucmail.uc.edu" -From "arbockhorst@gmail.com" -Subject "Adam Bockhorst's IT3038C Lab 3: Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)