#created by mnn at 10/2017

import json, os

class virusDictionary():
    def __init__(self):
        self.__version = "0"
        self.__virusList = {} #virus dictionary, pairs made up of virusvalue:virusname
        self.__fileDirectory = os.path.normpath('./virusDatabase/virusDatabase.json')
        self.loadVirusDictionary()
        self.printVirusDictionary()

    def loadVirusDictionary(self):
        with open(self.__fileDirectory, "r") as file:
            #self.__virusList = json.load(file)
            temp = json.load(file)
            tempDictionary = dict(temp["virusData"]["signatures"][0])
            counter = 1
            while counter < len(temp["virusData"]["signatures"]):
                tempDictionary.update(temp["virusData"]["signatures"][counter])
                counter += 1
            self.__virusList = tempDictionary #loads the json virus database
            self.__version = temp["virusData"]["version"][0]["currentVersion"] #changes version to current loaded version
            #print(self.__version)
        #----------------------------------)

    def printVirusDictionary(self):
        #print(self.__virusList["virusData"]["version"]["currentVersion"])
        #print(self.__virusList["virusData"]["signatures"][0]['trojan'])
        #print(self.__virusList['trojan'])
        #print(type(self.__virusList["virusData"]["signatures"]))
        #print(self.__virusList["version"])
        #print(self.__virusList["virusSignatures"])
        pass

    def checkIfIsThreat(self, threat):
        pass

vd = virusDictionary()