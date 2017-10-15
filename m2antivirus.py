# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import glob, os

counter = 0
defaultBlockSize = 1024

for fileName in glob.glob('./myfiles/*'): #for each FILE in FOLDER...
    #print counter
    counter += 1
    #print('Analyzing file {0} of {1}'.format(counter, ))
    print(counter)
    # - - - -
    with open(fileName, 'rb') as fileToAnalise:
        #dataFromFile = fileToAnalise.readlines()
        dataFromFile = []
        for line in fileToAnalise:
            dataFromFile.append(line)
        print('file {0}: {1}', counter, dataFromFile)
    fileToAnalise.close()
print("Finish")
