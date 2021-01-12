Write-Host "    >>>> Flagging $env:UserName for password change"
$user=[ADSI]"WinNT://localhost/$env:UserName"
$user.passwordExpired = 1
Write-Host "    >>>> Setting $env:UserName to password"
$user.SetPassword("password")
$user.SetInfo()
Write-Host "    >>>> Done"
