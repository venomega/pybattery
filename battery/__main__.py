import os
import sys

if  os.system("which upower &> /dev/null"):
    print ("You need upower to be installed on system")
    exit(1)

a = []
b = []
buff = os.popen("upower --dump").read()

for line in buff.split("\n"):
    if "Device:" in line:  
        b.append(a)
        a = []
    if "model" in line:
        a.append(line.split(":")[-1].replace(" ",""))
    if "native-path" in line:
        a.append(line.split(":")[-1].replace(" ",""))
    if "percentage" in line:
        a.append(line.split(":")[-1].replace(" ",""))

for element in b:
    if len(element) > 1:
        if "-raw" in sys.argv:
            print (element[-1], end=" ")
        else:
            print (" ".join(element))

