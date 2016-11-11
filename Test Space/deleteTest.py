import os

def findAndDelete(directory,extension):
    deleteCommand = "find " + directory + " -name " + extension + " -type f -delete"
    os.system(deleteCommand)

findAndDelete(".","'*.poop'")
