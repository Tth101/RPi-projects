import subprocess, re

def command_output(command):
    result = subprocess.run(command, capture_output=True, text=True) #avoid using shell = false?
    out = result.stdout.strip()
    return out

def file_write(content):
    f = open("stats.txt", "w")
    f.write(content)
    f.close()

def tempcheck():
    msg = command_output("vcgencmd measure_temp") #get cpu temperature
    temp = re.search(r'-?\d\.?\d*', msg) #use regex to obtain temperature
    out = float(temp.group())
    return out

def memcheck():
    msg = command_output("ipconfig")#get cpu temperature
    mem = re.search(r'-?\d\.?\d*', msg)#use regex to obtain temperature
    out = float(mem.group())
    return out

def init_file():
    file_write(tempcheck())

#os.system("ipconfig") #get cpu memory
#os.system("ipconfig") #get storage
