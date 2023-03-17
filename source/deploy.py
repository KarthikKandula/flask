# Imports
import subprocess

def runShellScript(script_path,arg1,arg2):
    print("Running shell script...")

    process = subprocess.Popen([script_path, arg1, arg2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output, error = process.communicate()

    if process.returncode == 0:
        print("Shell script executed successfully")
        # print(f"Output from shell script \n{error.decode() + output.decode()}")
    else:
        print("Shell script failed with error code", process.returncode)

    return error.decode() + output.decode()
