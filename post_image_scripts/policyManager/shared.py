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


