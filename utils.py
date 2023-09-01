import os

def clear():
    os.system("cls")

def checkFile(path):
    response = os.path.isfile(path)
    return response

def joinPath(x, y):
    newPath = os.path.join(x,y)
    return newPath