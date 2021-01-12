#Windows 7
# set blank screensaver
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v SCRNSAVE.EXE /t REG_SZ /d C:\Windows\system32\scrnsave.scr /f
# set screen saver timeout
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaveTimeOut /t REG_SZ /d 300 /f
# right click Desktop>Personalize>Screen Saver>On resume, display logon screen
reg add "HKCU\Control Panel\Desktop" /V ScreenSaverIsSecure /T REG_SZ /F /D 1
reg add "HKCU\System\Power" /V PromptPasswordOnResume /T REG_SZ /F /D 1

# refresh registry
#rundll32.exe user32.dll, UpdatePerUserSystemParameters

#OLD shit
#$regPath1 = 'HKLM:\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\7516b95f-f776-4464-8c53-06167f40cc99\8EC4B3A5-6868-48c2-BE75-4F3044BE88A7'
#$keyName1 = 'Attributes'
#$keyValue1 = '1'
#$regPath2 = 'HKU:\.DEFAULT\Control Panel\Desktop'
#$keyName2 = 'LockScreenAutoLockActive'
#$keyValue2 = '1'
#init HKU
#New-PSDrive -name HKU -PSProvider Registry -Scope Global -Root HKEY_USERS
#commands
#Set-Itemproperty -path $regPath1 -Name $keyName1 -value $keyValue1
#Set-Itemproperty -path $regPath2 -Name $keyName2 -value $keyValue2
#Screen saver timeout under user = 600
#computer: Require a password when computer wakes
