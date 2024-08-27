import subprocess, re

def tempcheck():
    msg =subprocess.check_output(
        ["../usr/bin/vcgencmd", "measure_temp"]
    ).decode() #get cpu temperature
    temp = re.search(r'-?\d\.?\d*', msg) #use regex to obtain temperature
    return temp

def memcheck():
    msg = subprocess.check_output(
        ["../usr/bin/free", "-m"]
    ).decode() # get mem usage
    return msg

