import os
import socket
import getpass
import ctypes, sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


# Check for admin and UAC prompt if needed
if not is_admin():
   ctypes.windll.shell32.ShellExecuteW(None, u"runas", str(sys.executable), str(__file__), None, 1)
   exit()


# Check for a subfolder
subfolder = "commands"
if not os.path.isdir(os.path.join(os.path.dirname(__file__), subfolder)):
    os.system("cls")
    input(    "\n\nCan't find the "
            + subfolder 
            + " folder that contains all the commands."
            + "\n\nPress enter to exit"
            )
    exit()


# Menu choices
choices = [ { "1" : { "Option 1" : "opt1.py" }},
            { "2" : { "Option 2" : "opt2.py"  }},
            { "3" : { "Option 3" : "opt3.py" }},
            { "4" : { "Option 4" : "opt4.py" }},
            { "z" : { "Option z" : "optz.py" }},
            { "y" : { "Option y" : "opty.py"  }},
            { "x" : {"Exit" : "menu.py"}},
            ]

            
# Menu formatting
hspace = "    "
vspace = "\n"
numsep = ") "

# Loop forever
while True:
    
    # Make Menu
    i = False
    os.system("cls")
    print(vspace)
    for choice in choices:
        for key, value in choice.items():
            for subkey, subval in value.items():
                if not key.isnumeric() and not i:
                    print("")
                    i = True
                print(hspace + key + numsep + subkey)
    answer = str(input(vspace + hspace + "Pick one..." + hspace))
    
    if(answer.upper() == "X"):
        break

    # Run file associated with the user input
    for choice in choices:
        for key, value in choice.items():
            if key == answer:
                for subkey, subval in value.items():
                    os.system("cls")
                    cmd = os.path.join(os.path.dirname(__file__), subfolder, subval)
                    print(vspace + hspace + "Running " + subval + "..." + vspace)
                    os.system(cmd)
    
    
