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
subprocess.call(['powershell.exe', os.path.join(os.path.dirname(__file__), 'SIMCheck.ps1')])
input("\nDone. Press any key to exit.")
