import os
import subprocess
import socket
import ctypes, sys
import time



# Functions
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def tvInstall(hostname):

    file_name = os.path.join(os.path.dirname(__file__), "")
    config_id = ''
    token = ''

    uninstall =  (    
                  'msiexec.exe /uninstall '
                + file_name
                + ' /qn'
                )
    install = (   'msiexec.exe /i '
                + file_name
                + ' /qn CUSTOMCONFIGID='
                + config_id
                + ' APITOKEN='
                + token
                + ' ASSIGNMENTOPTIONS="--grant-easy-access --reassign --alias ' + hostname + '"'
                )
    cmds = [uninstall,
            install,
            ]

    for cmd in cmds:
        print("Started ->>>>  " + cmd)
        crun = subprocess.Popen(cmd)
        crun.communicate()
        print("Finished ->>>>  " + cmd)
    print("Teamviewer install is finishing, please wait...")
    time.sleep(20)

# Check for admin and UAC prompt if needed
if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, u"runas", str(sys.executable), str(__file__), None, 1)
    exit()

# Loop until hostname is changed
while True:

    # Prompt to change the hostname
    os.system("cls")
    print("\n    Current hostname is: " + socket.gethostname()) 
    hostname = input("\n    Please enter the asset tag (example IT0001)...   ").upper()
    os.system("cls")

    # Check if hostname is weird
    length = len(hostname) == 6
    first2 = hostname[:2] == "IT"
    last4 = str(hostname[-4:]).isnumeric()
    proceed = "N"
    if not length or not first2 or not last4:
        print("\n    You entered a weird hostname:  " + hostname)
        proceed = input("    Change it anyway? (y/n)").upper()
        # Re-loop if user wants to try again
        if not proceed == "Y":
            continue
    
    # Put the new hostname on the screen
    print("\n")
    print("    Hostname will be changed from: " + socket.gethostname())
    print("                               to: " + hostname)
    ok = input("\n    Is that OK? (y/n):    ").upper()
    if not ok == "Y":
        continue
        
        
        
    # Change hostname as admin
    print("\n")
    subprocess.call(['powershell.exe', "Rename-Computer -NewName " 
                    + hostname])
    # sleep in case there is a powershell error
    time.sleep(4)
    os.system("cls")
   
    # Extend the C drive using DiskPart
    extend_file = os.path.join(os.path.dirname(__file__), "extend.txt")
    os.system("diskpart /s " + extend_file)
    time.sleep(4)
    os.system("cls")
    
    # Install Teamviewer
    print("\n")
    print("------------------------------------------------------")
    print(" INSTALLING TEAMVIEWER AND PUSHING HOSTNAME TO REMOTE ")
    print("------------------------------------------------------")
    tvInstall(hostname)
    print("------------------------------------------------------")
    print("   TEAMVIEWER INSTALL COMPLETE, PLEASE CHECK REMOTE   ")
    print("------------------------------------------------------")
    print("\n")
    
    # Prompt to reboot
    print("   1) Reboot")
    print("   2) Shutdown")
    print("   3) Exit\n\n\n\n")
    opt = input()
    if opt == "1":
        os.system("shutdown /r /t 1")
    if opt == "2":
        os.system("shutdown /s /t 1")
    break






