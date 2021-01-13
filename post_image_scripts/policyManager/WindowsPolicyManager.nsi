SilentInstall silent ;enable silent install
#ShowInstDetails show ;enable debug
OutFile "WindowsPolicyInstaller.exe" ;name the exe

Section
  StrCpy $INSTDIR "C:\MDM" ;name the output folder
  SetOutPath $INSTDIR
  File /r  '.\dist\WindowsPolicyManager'
  nsExec::ExecToLog 'C:\MDM\WindowsPolicyManager\WindowsPolicyManager.exe'
SectionEnd

