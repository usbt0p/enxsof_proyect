import os
import subprocess

if __name__ == "__main__":
    # Establecer PYTHONPATH antes de ejecutar tu programa principal
    os.environ['PYTHONPATH'] = '.'

    # Ejecutar tu programa principal (supongamos que es main.py)
    subprocess.run(["python", "src/main.py"], shell=True)
