import subprocess, re

def tempcheck():
    temp =subprocess.check_output(
        ["../usr/bin/vcgencmd", "measure_temp"]
    ).decode()
    temp = re.search(r'-?\d\.?\d*', temp) #use regex to obtain temperature
    return temp

def memcheck():
    mem = subprocess.check_output(
        ["../usr/bin/free", "-m"]
    ).decode()
    mem = re.findall(r'-?\d\-?\d*', mem)
    return mem
