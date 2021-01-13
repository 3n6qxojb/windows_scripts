Clear-Host
Write-Host -ForegroundColor Yellow "===== CHECKING FOR WINDOWS UPDATE ====="
Do {
        Write-Host "`nPlease wait...`n"
        $net = test-connection www.google.com -quiet
        if ($net -eq $True)
        {Write-Host -ForegroundColor Green "System is online`n"}
        else {
                Write-Host -ForegroundColor Red "System is offline`n"
                Read-Host -Prompt "Please connect to the Internet and press Enter to continue"
             }
    }
Until ($net -eq $True)
Write-Host "Looking for latest updates to install. This computer may restart several times, please wait...`n"
Do {
        $error.clear()
        try 
            {Get-WUInstall –MicrosoftUpdate –AcceptAll –AutoReboot}
        catch {
                [void](Install-PackageProvider Nuget -Force)
                [void](Install-Module PSWindowsUpdate -Force)
                [void](Add-WUServiceManager -ServiceID 7971f918-a847-4430-9279-4a52d1efe18d -confirm:$false)
              }
    }
until (!$error)