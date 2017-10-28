#created by mnn at 10/2017

import fileLoader, virusDictionary, virusScanner, os


#initiate variables==
#clear = lambda: os.system('cls') #clear screen
fileLoader = fileLoader.fileLoader()
virusDictionary = virusDictionary.virusDictionary()
virusScanner = virusScanner.virusScanner()

#text variables======
textMainMenu = ("Select an option:\n1- Scan myFiles\n2- Show quarantine\n3- Update antivirus\n4- Show antivirus version\n0- Reset to defaults.\n\nOption:  ")
textReturn = ("Press any key to return.\n\n")
#===


#case 1
def scanMyFiles():
    virusScanner.scanDirectory()

#case 2
def showQuarantine():
    virusScanner.showQuarantine()

#case 3
def updateVirusDatabase():
    virusScanner.updateVirusDatabase()

#case 4
def showVirusDictionary():
    virusScanner.printVirusDictionary()

#case 0
def restoreDefaults():
    print("\nReturning to defaults...")
    #clear quarantine
    virusScanner.undoQuarantine()
    #undo update
    virusScanner.undoUpdateVirusDatabase()

#switch
def switcher(number):
    if (number == "1"):
        scanMyFiles()
    elif (number == "2"):
        showQuarantine()
    elif (number == "3"):
        updateVirusDatabase()
    elif (number == "4"):
        showVirusDictionary()
    elif (number == "0"):
        restoreDefaults()

#se o antivirus nao encontrar um virus em ./quarantine\Chrysanthemum.jpg
#pode ser por causa das classes os? o programa foi feito em windows
while (True):
    userInput = input(textMainMenu)
    switcher(userInput)
    userInput = input(textReturn)

