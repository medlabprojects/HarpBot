import subprocess
import os
import sys

# Determine the Python executable location
python_path = ""
for p in sys.path:
    if "site-packages" in p:
        print(p)
        python_path = os.path.abspath(os.path.join(p, '../..'))

# Error check
if len(python_path) == 0:
    print("Couldn't find Python path!")
    sys.exit(1)


print("Found Python path: " + python_path)
print(python_path)

tmp = subprocess.check_output("dir " + python_path, shell=True).decode().strip()
if "python.exe" in tmp:
    print("Found Python executable!")
else:
    print("Couldn't find Python executable!")
    sys.exit(1)

python_exe = os.path.join(python_path, "python.exe")

# Install numpy
print("Installing numpy...")
install_cmd = python_exe + " -m pip install numpy"
proc = subprocess.Popen(install_cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, shell=True)
proc.wait()
stdout, stderr = proc.communicate()
print(stdout)

# Install matplotlib
print("Installing matplotlib...")
install_cmd = python_exe + " -m pip install matplotlib"
proc = subprocess.Popen(install_cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, shell=True)
proc.wait()
stdout, stderr = proc.communicate()
print(stdout)

# Install pyserial
print("Installing pyserial...")
install_cmd = python_exe + " -m pip install pyserial"
proc = subprocess.Popen(install_cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, shell=True)
proc.wait()
stdout, stderr = proc.communicate()
print(stdout)

