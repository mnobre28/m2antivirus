#created by mnn at 10/2017

import virusDictionary, fileLoader, time, shutil

class virusScanner():
    def __init__(self):
        self.__virusDict = virusDictionary.virusDictionary()
        self.__fileLoader = fileLoader.fileLoader()
        self.__quarantineDirectory =  ('./quarantine/')
    # ----------------------------------

    def updateVirusDatabase(self):
        self.__virusDict.updateVirusDictionary()

    def undoUpdateVirusDatabase(self):
        self.__virusDict.undoUpdate()
        print("Antivirus version is now 1.0.")

    def printVirusDictionary(self):
        self.__virusDict.printVirusDictionary()

    def scanDirectory(self, directory = './myfiles/*'):
        self.__fileLoader.loadFilesFromDir(directory) #using default myfiles dir
        listOfFiles = self.__fileLoader.getListOfFiles()
        listOfInfectedFiles = {} #fileaddress and virusname
        #listOfViruses = []
        print("\nStarting scan of {}".format(directory))
        for fileAddress,fileHexCode in listOfFiles.items():
            print("Checking {} for viruses...".format(fileAddress))
            time.sleep(1)
            resultOfCheck = self.__virusDict.checkIfIsThreat(fileHexCode)
            if resultOfCheck:
                print("Threat found! Signature {} in file {}.".format(resultOfCheck[1], fileAddress))
                listOfInfectedFiles.update({fileAddress:resultOfCheck[1]})
                #print(type(resultOfCheck))
                #print(resultOfCheck)
                #listOfViruses.append(resultOfCheck[0]) #put virus name here
            else:
                print("No threats found.")
            print("Scan completed.")
        self.quarantineInfectedFiles(listOfInfectedFiles)

        #----------------------------------)

    def quarantineInfectedFiles(self, listOfInfectedFiles):
        print("\n")
        for fileAddress, virusName in listOfInfectedFiles.items():
            print("Moving {} to quarantine: infected with {}".format(fileAddress, virusName))
            shutil.move(fileAddress, self.__quarantineDirectory)
        print("All infected files moved.")

    def undoQuarantine(self):
        tempFileLoader = fileLoader.fileLoader()
        tempFileLoader.loadFilesFromDir('./quarantine/*')  # using default myfiles dir
        listOfFiles = tempFileLoader.getListOfFiles()
        for fileAddress, fileHexCode in listOfFiles.items():
            print("Moving {} back to MyFiles.".format(fileAddress))
            shutil.move(fileAddress, './myfiles/')
        print("Quarantile folder clear.")

    def showQuarantine(self):
        tempFileLoader = fileLoader.fileLoader()
        tempFileLoader.loadFilesFromDir('./quarantine/*')  # using default myfiles dir
        listOfFiles = tempFileLoader.getListOfFiles()
        print("\nFiles quarantined:")
        count = 0
        for fileAddress, fileHexCode in listOfFiles.items():
            count += 1
            print("{}. {}".format(count, fileAddress))
        if (count == 0):
            print("No files in quarantine.")
        print("\n")


