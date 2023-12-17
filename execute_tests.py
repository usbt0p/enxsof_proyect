import sys
sys.path.insert(0, '.')

import os
import subprocess

if __name__ == "__main__":
    # Establish PYTHONPATH on the script location
    os.environ['PYTHONPATH'] = '.'

    #Check for Windows or Linux and Execute Main
    python_command = "python3" if sys.platform != "win32" else "python"
    subprocess.run([python_command, "src/main.py"], shell=False)


    