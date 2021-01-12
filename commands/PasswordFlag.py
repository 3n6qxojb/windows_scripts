import os
import ctypes, sys
import subprocess


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


# Check for admin and UAC prompt if needed
if not is_admin():
   ctypes.windll.shell32.ShellExecuteW(None, u"runas", str(sys.executable), str(__file__), None, 1)
   exit()


os.system('cls')
print("\n    Working...")
subprocess.call(['powershell.exe', os.path.join(os.path.dirname(__file__), 'PasswordFlag.ps1')])

print("\nMaking PW policy strict...\n")
cmd = os.path.join(os.path.join(os.path.dirname(__file__), 'PasswordPolicy.bat'))
os.system(cmd)


print('\n\n')
# Prompt to reboot
print("   1) Reboot")
print("   2) Shutdown")
print("   3) Exit\n\n\n\n")
opt = input()
if opt == "1":
    os.system("shutdown /r /t 1")
if opt == "2":
    os.system("shutdown /s /t 1")