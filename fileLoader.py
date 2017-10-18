#created by mnn at 10/2017

import hashlib, glob, time, os

class fileLoader():
    def __init__(self):
        self.__quarantineAddress = ('./quarantine/')
        self.__listOfFiles = {}
        #self.loadFiles()
    # ----------------------------------

    def loadFilesFromDir(self, directory = './myfiles/*'):
        counter = 0
        hasher = hashlib.md5()
        for fileName in glob.glob(directory):  # for each FILE in FOLDER...
            with open(fileName, 'rb') as fileToLoad:
                counter += 1
                #print("Reading file {} of {}...".format(counter, len(os.listdir(directory[:-1]))))
                buffer = fileToLoad.read()
                hasher.update(buffer)
                #print(hasher.hexdigest())
                self.__listOfFiles.update({fileName:hasher.hexdigest()})
                #print("adding {} file-hexcode combo to scan list".format({fileName:hasher.hexdigest()}))
                #time.sleep(1)

    def printListOfHexas(self):
        print(self.__listOfFiles)

    def getListOfFiles(self):
        return self.__listOfFiles