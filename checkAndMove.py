import shutil
from datetime import datetime, timedelta
import time
from glob import glob
import os

debug = False # used for debugging

def debug_print(text):
    if debug is True:
        print (text)

def fileMover(filesStartA, filesEndB):
    debug_print("Got in the function")
    timeNow = datetime.now()
    oneDayOld =    timeNow - timedelta(hours = 24) 
    if not os.path.exists(os.path.dirname(filesStartA)) :
        debug_print ("failure")
        return
    for f in os.listdir(filesStartA):
        debug_print("File F: " + f)
        files = os.path.realpath(os.path.join(filesStartA, f)) 
        debug_print("File Files: " + files)
        if files.endswith('.txt'):
            filesToMove = datetime.fromtimestamp(os.path.getmtime(files)) 
            if filesToMove > oneDayOld:
                shutil.copy(files,filesEndB) 
                print (files, "Copied:  ", filesEndB)
            else:
                print (files, "Not Copied")


filesStartA = "/Users/seanbass/Desktop/A" #change / to \ if on windows instructor
filesEndB = "/Users/seanbass/Desktop/B"
fileMover(filesStartA, filesEndB)

