import subprocess

def command_output(command):
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout.strip()
    return output

test = command_output("ipconfig")#get cpu temperature
 
#os.system("ipconfig") #get cpu memory
#os.system("ipconfig") #get storage

f = open("test.txt", "w")
f.write(test)
f.close()
