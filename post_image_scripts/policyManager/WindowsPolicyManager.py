import sys
#sys.path.insert(0, '..\\Shared')
import shared
import base64
import subprocess
import sys



#run a command on Windows, make the conosle output python readable,
# and log the results in a Python log
def dosCmd(cmd, input=None):
    cmd64 = base64.encodebytes(cmd.encode('utf-16-le')).decode('ascii').strip()
    stdin = None if input is None else subprocess.PIPE
    process = subprocess.Popen(["powershell.exe", "-NonInteractive", "-EncodedCommand", cmd64],
                                stdin=stdin,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
    if input is not None:
        input = input.encode(sys.stdout.encoding)
    output, stderr = process.communicate(input)
    return output


import os
import ctypes
import logging
import winreg



#hides dos window, comment for testing or it will close your command window :)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


STARTUPNAME = 'Policy Manager'
APPNAME = 'WindowsPolicyManager'
UFILE = 'startupRemove.cmd'
PATH = os.path.join('C:\\', 'MDM', 'WindowsPolicyManager')
logging.basicConfig(filename=os.path.join(PATH, APPNAME + '.log'), filemode='w', level=logging.INFO)


#log the cmd and remove unwanted characters
def cmdWrapper(cmd, input=None):
    output = shared.dosCmd(cmd, input)
    logging.info(cmd)
    logging.info(output)
    output = str(output)
    output = output.replace('\\n', '')
    output = output.replace('\\r', '')
    return output
    

#the user info dictionary that will be populated going forward
USERS = [#default user
        {'profile' : 'C:\\Users\\Default',
         'hive' : 'HKLM\DEFAULT',
         'hiveload' : True},
        #current user
        {'profile' : '',
         'hive' : 'HKCU',
         'hiveload' : False,}
        ]

    
#populate USER with each Windows user
i = 0
userkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                         'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList')
while True:
    try:
        sid = str(winreg.EnumKey(userkey, i))
        #only use non system sids which are over 8 characters
        if len(sid) > 8:
            subkey = winreg.OpenKey(
                        winreg.HKEY_LOCAL_MACHINE,
                        'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList\\'
                        + sid)
            profile = winreg.QueryValueEx(subkey, 'ProfileImagePath')
            hiveload = False
            try:
                logging.info(winreg.OpenKey(winreg.HKEY_USERS, sid))
            except:
                hiveload = True
            userD = {'profile' : profile[0],
                     'hive' : 'HKU\\' + sid,
                     'hiveload' : hiveload}
            USERS.append(userD)
            logging.info(userD)
        i+=1
    except WindowsError:
        logging.info('Found ' + str(i) + ' registry users')
        break


#load any needed hives
for user in USERS:
    if user['hiveload']:
        cmdWrapper('reg load ' + user['hive'] + ' "' + user['profile'] + '\\ntuser.dat"' )
    else:
        logging.info(user['hive'] + ' already loaded')


#clear startup reg key uninstall batch file before writing keys
with open(os.path.join(PATH, UFILE), 'w') as uf:
    uf.write('')


#Make user changes to Windows specific stuff
for user in USERS:
    #change screenaver to blank
    cmdWrapper('reg add "' + user['hive'] + '\Control Panel\Desktop" /v SCRNSAVE.EXE /t REG_SZ /d "C:\Windows\System32\scrnsave.scr" /f')
    #change screensaver timeout to 5 min
    cmdWrapper('reg add "' + user['hive'] + '\Control Panel\Desktop" /v ScreenSaveTimeOut /t REG_SZ /d 300 /f')
    #set password protect screensaver 1
    cmdWrapper('reg add "' + user['hive'] + '\Control Panel\Desktop" /v ScreenSaverIsSecure /t REG_SZ /f /d 1')
    #set password protect screensaver 2
    cmdWrapper('reg add "' + user['hive'] + '\System\Power" /v PromptPasswordOnResume /t REG_SZ /f /d 1')
    #add this file as exe to windows startup reg key
    cmdWrapper('reg add "' + user['hive'] + '\Software\Microsoft\Windows\CurrentVersion\Run" /v "' + STARTUPNAME + '" /t REG_SZ /d "' + os.path.join(PATH, APPNAME + '.exe') + '" /f')
    #generate an undo/redo file for running at startup
    with open(os.path.join(PATH, UFILE), 'a') as uf:
        undoCmd = 'reg delete "' + user['hive'] + '\Software\Microsoft\Windows\CurrentVersion\Run" /v "' + STARTUPNAME + '" /f\n'
        uf.write(undoCmd)
        logging.info('Wrote command below to file: ' + os.path.join(PATH, UFILE))
        logging.info(undoCmd)
    
    
#unload the hives we loaded
for user in USERS:
    if user['hiveload']:
        cmdWrapper('reg unload ' + user['hive'])


#change the password policy for all users on the computer
cmdWrapper('net accounts /MINPWLEN:8 /MINPWAGE:5 /MAXPWAGE:60 /UNIQUEPW:3 /LOCKOUTTHRESHOLD:30')

