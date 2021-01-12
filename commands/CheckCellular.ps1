Clear-Host
Write-Host "Testing Cellular modem for Internet connection...please wait`n"
Enable-NetAdapter c* -confirm:$false
disable-netadapter e*,w*,l* -confirm:$false
Start-Sleep -Seconds 5
# get Chrome process
$chrome = Get-Process chrome -ErrorAction SilentlyContinue
if ($chrome) 
  {
    # try gracefully first
    $chrome.CloseMainWindow()
    # kill after five seconds
    Start-Sleep -s 5
    if (!$chrome.HasExited) 
      {$chrome | Stop-Process -Force}
  }
$net = test-connection www.google.com -quiet
if ($net -eq $True) 
  {Write-Host -ForegroundColor Green "`nSIM Card is Active`n"}
else {
        Write-Host -ForegroundColor Red "`nSIM CARD IS NOT ACTIVE`n"
        Read-Host -Prompt "Please activate SIM card for this device. Press Enter to continue"
     }
enable-netadapter e*,w*,l* -confirm:$false