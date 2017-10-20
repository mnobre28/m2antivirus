#created by mnn at 10/2017

import json, os, time

class virusDictionary():
    def __init__(self):
        self.__version = "0.0" #default value. is updated when the dictionary is loaded.
        self.__virusList = {} #virus dictionary, pairs made up of virusvalue:virusname
        self.__fileDirectory = os.path.normpath('./virusDatabase/virusDatabase.json')
        self.__updateDirectory = os.path.normpath('./updateDatabase/updatedVirusDatabase.json')
        self.loadVirusDictionary(self.__fileDirectory) #load outdated virus database
        #self.printVirusDictionary()

    def loadVirusDictionary(self, directoryOfFileToLoad = os.path.normpath('./virusDatabase/virusDatabase.json')):
        with open(directoryOfFileToLoad, "r") as file: #updating the list thats in memory
            temp = json.load(file)
            tempDictionary = dict(temp["virusData"]["signatures"][0])
            newestUpdateVersion = temp["virusData"]["version"][0]["currentVersion"]
            counter = 1
            if (newestUpdateVersion != self.__version):
                while counter < len(temp["virusData"]["signatures"]):
                    tempDictionary.update(temp["virusData"]["signatures"][counter])
                    counter += 1
                self.__virusList = tempDictionary #loads the json virus database
                self.__version = temp["virusData"]["version"][0][
                    "currentVersion"]  # changes version to current loaded version
                if (self.__version != "1.0"):
                    print("Updating threat database...")
                    time.sleep(1)
                    print("Updated to version: ", self.__version)
            else:
                print("\nVirus database already up to date.\n")
        #----------------------------------)
        file.close()
        with open(self.__fileDirectory, "w") as file: #updating json file
            json.dump(temp, file)
        file.close()


    def updateVirusDictionary(self, directoryOfFileToLoad = os.path.normpath('./updateDatabase/updatedVirusDatabase.json')):
        self.loadVirusDictionary(directoryOfFileToLoad)
        #only updates the dictionary thats running right now!
        #the old database will be loaded when the program restarts

    def printVirusDictionary(self):
        #print(self.__virusList["virusData"]["version"]["currentVersion"])
        #print(self.__virusList["virusData"]["signatures"][0]['trojan'])
        #print(self.__virusList['trojan'])
        #print(type(self.__virusList["virusData"]["signatures"]))
        #print(self.__virusList["version"])
        #print(self.__virusList["virusSignatures"])
        print("Virus database version: ", self.__version)
        print("Current threats: ")
        print(self.__virusList)

    def checkIfIsThreat(self, fileHexValue):
        #print("checking if threat")
        for virussignature, virusname in self.__virusList.items():
            if (virussignature in fileHexValue): #if a known virus is present in the file hex code...
                return (virussignature, virusname)
        return False