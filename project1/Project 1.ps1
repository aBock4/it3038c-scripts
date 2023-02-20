#This is a powershell script
#This script tells the user the current user and the time

#set the current user to a variable
$user = $env:USERNAME

#set the current time (hour and minutes only) to a variable
$time = Get-Date -Format "hh:mm"

#print friendly message to console/host with current user and current time
Write-Host("The current user is: " + $user + ". The current time is: " + $time)