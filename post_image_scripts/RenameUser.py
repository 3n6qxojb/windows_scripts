import os
import time
import subprocess
import ctypes, sys
import win32com.client
from winreg import *


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


# Check for admin and UAC prompt if needed
if not is_admin():
   ctypes.windll.shell32.ShellExecuteW(None, u"runas", str(sys.executable), str(__file__), None, 1)
   exit()

# Rename the user
current_user = ""
while True:
    os.system('cls')
    first = input("\n  Enter the new user's first name: ").title()
    last = input("   Enter the new user's last name: ").title()
    new_user = first + "." + last
    choice = input(
          "\n\n  Is it OK to rename this current user ->>>  " + current_user
        + "\n                   ...to this new user ->>>  " + new_user
        + "\n\n    (y/n): "
        ).lower()
    if not choice == "y":
        continue
    # Rename user
    print('\n\n')
    os.system('wmic useraccount where Name="' + current_user + '" rename ' + new_user)
    os.system('wmic useraccount where Name="' + new_user + '" set FullName=' + new_user)
    time.sleep(3)
    break


# Disable autologin and Administrator account
os.system('cls')
print("\n>>> Disabling auto logon for Administrator")
# Connect to Task Scheduler
scheduler = win32com.client.Dispatch('Schedule.Service') #https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-schema-elements
scheduler.Connect()
root_folder = scheduler.GetFolder('\\')
task_def = scheduler.NewTask(0)
# Create trigger
TASK_TRIGGER_REGISTRATION = 7
trigger = task_def.Triggers.Create(TASK_TRIGGER_REGISTRATION)
# Create action
TASK_ACTION_EXEC = 0
action = task_def.Actions.Create(TASK_ACTION_EXEC)
action.ID = 'DO NOTHING'
action.Path = 'regedit.exe'
action.Arguments = '/s "' + os.path.join(os.path.dirname(__file__), 'AutoLogonDisable.reg') + '"'
# Set parameters
task_def.RegistrationInfo.Description = 'AutoLogonDisable.reg'
task_def.Settings.Enabled = True
task_def.Settings.StopIfGoingOnBatteries = False
task_def.Settings.DisallowStartIfOnBatteries = False
# Register task
# If task already exists, it will be updated
TASK_CREATE_OR_UPDATE = 6
TASK_LOGON_NONE = 0
root_folder.RegisterTaskDefinition(
    'AutoLogonDisable.reg',  # Task name
    task_def,
    TASK_CREATE_OR_UPDATE,
    '',  # No user
    '',  # No password
    TASK_LOGON_NONE)
time.sleep(1)


print(">>> Disabling Administrator account")
time.sleep(1)
os.system('net user "administrator" /active:no')
print(">>> All done...\n\n")
time.sleep(1)
# Prompt to reboot
print("   1) Reboot")
print("   2) Shutdown")
print("   3) Exit\n\n\n\n")
opt = input()
if opt == "1":
    os.system("shutdown /r /t 1")
if opt == "2":
    os.system("shutdown /s /t 1")


