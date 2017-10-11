#created by mnn at 10/2017

import hashlib, glob, time, os

class virusScanner():
    def __init__(self):
        self.__directory = ('./myfiles/*') #for each FILE in FOLDER...
        self.__listOfFiles = []
        self.loadFiles()
    # ----------------------------------

    def loadFiles(self, directory = './myfiles/*'):
        counter = 0
        hasher = hashlib.md5()
        for fileName in glob.glob(directory):  # for each FILE in FOLDER...
            with open(fileName, 'rb') as fileToAnalise:
                counter += 1
                print("Reading file {} of {}...".format(counter, len(os.listdir(directory[:-1]))))
                buffer = fileToAnalise.read()
                hasher.update(buffer)
                print(hasher.hexdigest())
                time.sleep(1)


    def convertToHash(self, p):
        pass
        #----------------------------------)

vs = virusScanner()