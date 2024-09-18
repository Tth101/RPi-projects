import subprocess, re

def tempcheck():
    temp =subprocess.check_output(
        ["../usr/bin/vcgencmd", "measure_temp"]
    ).decode()
    temp = re.search(r'\d*\.\d+', temp) #Use regex to obtain temperature value
    return temp.group(0)

def memcheck():
    mem = subprocess.check_output(
        ["../usr/bin/free"]
    ).decode()
    mem = re.findall(r'-?\d\-?\d*', mem) #Use regex to obtain memory values
    return mem
    #Turn to string since sqlite3 returns re.match not supported
