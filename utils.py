import subprocess

def runProcess(process):
    print("Running process: " + str(process))
    try:
        subprocess.Popen(process)
    except:
        print("Failed to run " + str(process))
