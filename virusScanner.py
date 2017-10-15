#created by mnn at 10/2017

import virusDictionary, fileLoader

class virusScanner():
    def __init__(self):
        self.__virusDict = virusDictionary.virusDictionary()
        self.__fileLoader = fileLoader.fileLoader()
    # ----------------------------------

    def updateVirusDatabase(self):
        self.__virusDict.updateVirusDictionary()

    def scanDirectory(self, directory = './myfiles/*'):
        self.__fileLoader.loadFilesFromDir(directory) #using default myfiles dir
        listOfFiles = self.__fileLoader.getListOfFiles()
        listOfInfectedFiles = {}
        for fileAddress,fileHexCode in listOfFiles.items():
            print("Checking {} for viruses...".format(fileAddress))
            if self.__virusDict.checkIfIsThreat(fileHexCode):
                listOfInfectedFiles.update({fileAddress:fileHexCode})

        #----------------------------------)

vs = virusScanner()
vs.scanDirectory()

print("finished")