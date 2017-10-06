# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import glob, os

counter = 0
blocksize = 1024

for fileName in glob.glob('./myfiles/*'): #for each FILE in FOLDER...
    #print counter
    counter += 1
    print(counter)
    # - - - -
    fileToAnalise = open(fileName, 'rb')
    blockToAnalise = fileToAnalise.read(os.stat(fileToAnalise).st_size) #reads whole file
    str = ""
    for ch in blockToAnalise:
        strTemp = hex(ord(ch))+"" #convert each character of the file (TODO?)
        strTemp = strTemp[2:]
        str += strTemp
    print(str) #print no resultado final
    
    



#fileToAnalise = open('one.txt', 'r')
#print fileToAnalise

print("Hello World")
