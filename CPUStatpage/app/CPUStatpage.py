import subprocess, re
#def file_write(content):
    #f = open("stats.txt", "w")
   # f.write(content)
    #f.close()

def tempcheck():
    msg =subprocess.check_output(
        ["../usr/bin/vcgencmd", "measure_temp"]
    ).decode()#get cpu temperature
    temp = re.search(r'-?\d\.?\d*', msg) #use regex to obtain temperature
    out = float(temp.group())
    return out

def memcheck():
    msg = "ipconfig"#get cpu temperature
    mem = re.search(r'-?\d\.?\d*', msg)#use regex to obtain temperature
    out = float(mem.group())
    return out

#def init_file():
    #file_write(tempcheck())

#os.system("ipconfig") #get cpu memory
#os.system("ipconfig") #get storage
