import subprocess, re, sqlite3

def tempcheck():
    temp =subprocess.check_output(
        ["../usr/bin/vcgencmd", "measure_temp"]
    ).decode()
    #temp = re.search(r'-?\d\.?\d*', msg) #use regex to obtain temperature
    return temp

def memcheck():
    msg = subprocess.check_output(
        ["../usr/bin/free", "-m"]
    ).decode()
    return msg
