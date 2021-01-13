@echo off

::change screensaver timeout to 0 min (disabed)
reg add "HKCU\Control Panel\Desktop" /v ScreenSaveTimeOut /t REG_SZ /d 0 /f
::turn off PW protect for screen saver
reg add "HKCU\Control Panel\Desktop" /v ScreenSaverIsSecure /t REG_SZ /f /d 0
reg add "HKCU\System\Power" /v PromptPasswordOnResume /t REG_SZ /f /d 0
::Make PW policy lenient
net accounts /MINPWLEN:0 /MINPWAGE:0 /MAXPWAGE:999
timeout /t 3

