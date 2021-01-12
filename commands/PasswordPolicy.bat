@echo off

::change screenaver to blank
reg add "HKCU\Control Panel\Desktop" /v SCRNSAVE.EXE /t REG_SZ /d "C:\Windows\System32\scrnsave.scr" /f
::change screensaver timeout to 5 min
reg add "HKCU\Control Panel\Desktop" /v ScreenSaveTimeOut /t REG_SZ /d 300 /f
::set password protect screensaver 1
reg add "HKCU\Control Panel\Desktop" /v ScreenSaverIsSecure /t REG_SZ /f /d 1
::set password protect screensaver 2
reg add "HKCU\System\Power" /v PromptPasswordOnResume /t REG_SZ /f /d 1
::add this file as exe to windows startup reg key
net accounts /MINPWLEN:8 /MINPWAGE:5 /MAXPWAGE:60 /UNIQUEPW:3 /LOCKOUTTHRESHOLD:30


