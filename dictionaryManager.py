#created by mnn at 10/2017

import virusDictionary

class dictionaryManager():
    def __init__(self):
        self.__virusDictionary

    # ----------------------------------

    def updateDictionary(self, p):
        pass
        # ----------------------------------)

    def checkForUpdates(self, updateVersion):
        if self.__systemVersion != updateVersion:
            print("Threat database is not up to date.")
            print("Updating to latest version...")
            # replace dictionary w the newest TODO
            self.__systemVersion = updateVersion

        # ----------------------------------)