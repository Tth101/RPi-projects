import subprocess, re

def command_output(command):
    result = subprocess.run(command, capture_output=True, text=True) #avoid using shell = false?
    out = result.stdout.strip()
    return out

def tempcheck():
    msg = command_output("ipconfig")#get cpu temperature
    temp = re.search(r'-?\d\.?\d*', msg)#use regex to obtain temperature
    out = float(temp.group())
    return out

def memcheck():
    msg = command_output("ipconfig")#get cpu temperature
    mem = re.search(r'-?\d\.?\d*', msg)#use regex to obtain temperature
    out = float(mem.group())
    return out

def init_text_file():
    tempcheck()
 




#os.system("ipconfig") #get cpu memory
#os.system("ipconfig") #get storage

f = open("test.txt", "w")
f.write(temp)
f.close()
