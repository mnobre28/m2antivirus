#created by mnn at 10/2017

import virusDictionary, fileLoader, time

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
        listOfViruses = {}
        for fileAddress,fileHexCode in listOfFiles.items():
            print("Checking {} for viruses...".format(fileAddress))
            time.sleep(1)
            resultOfCheck = self.__virusDict.checkIfIsThreat(fileHexCode)
            if resultOfCheck:
                print("Threat found! Signature {} in file {}.".format(resultOfCheck[1], fileAddress))
                listOfInfectedFiles.update({fileAddress:fileHexCode})
                #print(type(resultOfCheck))
                #print(resultOfCheck)
                listOfViruses.update({resultOfCheck[0]:resultOfCheck[1]})
            else:
                print("No threats found.")

        #----------------------------------)

    def quarantineInfectedFiles(self):
        print("TODO")

vs = virusScanner()
vs.scanDirectory()

print("finished")