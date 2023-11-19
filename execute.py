import os
import subprocess

if __name__ == "__main__":
    # Establish PYTHONPATH on the script location
    os.environ['PYTHONPATH'] = '.'

    # Execute main
    subprocess.run(["python", "src/main.py"], shell=True)