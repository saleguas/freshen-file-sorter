import shutil
import os
import datetime
import yaml

# Making a class to move each file to the same location


class FileMover:

    def __init__(self, moveLocation):
        self.moveLocation = moveLocation
        if not os.path.exists(moveLocation):
            os.makedirs(moveLocation)

    def rename(self, fileName):
        nameTokens = os.path.splitext(fileName)
        # Add a seperator to the new file
        newFileName = ''.join(
            [nameTokens[0], '_', nameTokens[1]])
        return newFileName

    def move(self, fileLocation):
        fileName = os.path.basename(fileLocation)

        while os.path.isfile(os.path.join(self.moveLocation, fileName)):
            fileName = self.rename(fileName)

        newLocation = os.path.join(os.path.dirname(fileLocation), fileName)

        try:
            os.rename(fileLocation, newLocation)

            print("Moving {} to {}".format(newLocation, fileLocation))
            shutil.move(fileLocation, self.moveLocation)
        except:
            print("Couldn't move {}".format(fileLocation))


def sortbyType(path):
    srcLoc = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'config', 'filegroups.yml')
    distLoc = yamlLoc = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'config', 'filegroups.yml')

    filegroups = ''
    try:
        filegroups = yaml.load(
            open(srcLoc), Loader=yaml.FullLoader)
    except FileNotFoundError:
        filegroups = yaml.load(
            open(distLoc), Loader=yaml.FullLoader)
    filekeys = filegroups.keys()
    filePool = []
    for key in filekeys:
        for file in filegroups[key]:
            filePool.append(file)
    for file in os.listdir(path):
        fileExt = os.path.splitext(file)[1].replace('.', '')
        folderName = 'Others'
        for key in filekeys:
            for extension in filegroups[key]:
                if extension.lower() == fileExt.lower():
                    folderName = key
                    break
            if folderName != 'Others':
                break
        currentLoc = os.path.join(path, file)
        destination = os.path.join(path, folderName)
        fm = FileMover(destination)
        fm.move(currentLoc)


def sortByExtension(path):
    for file in os.listdir(path):
        fileExt = os.path.splitext(file)[1]
        currentLoc = os.path.join(path, file)
        if os.path.isfile(currentLoc):
            destination = os.path.join(path, "_" + fileExt)
            fm = FileMover(destination)
            fm.move(currentLoc)


# Sorts by either year, year and month, year month and day.
def sortByDate(path, precision):
    for file in os.listdir(path):
        currentLoc = os.path.join(path, file)
        if os.path.isfile(currentLoc):
            modified = os.path.getmtime(currentLoc)
            datename = ""
            if(precision == "Y"):
                datename = datetime.datetime.fromtimestamp(
                    modified).strftime('%Y')
            elif(precision == "M"):
                datename = datetime.datetime.fromtimestamp(
                    modified).strftime('%Y-%m')
            else:
                datename = datetime.datetime.fromtimestamp(
                    modified).strftime('%Y-%m-%d')
            print(datename)
            destination = os.path.join(path, "_" + datename)
            fm = FileMover(destination)
            fm.move(currentLoc)


def extract(originDir, currentDir):
    print(originDir, currentDir)
    # Start at the origin directory, list every file and folder
    for file in os.listdir(currentDir):
        # Update the path pointer to the current file(maybe folder)
        currentFolder = os.path.join(currentDir, file)
        # Ignore if it's a file
        if os.path.isdir(currentFolder):
            # Recursively run on the current folder
            extract(originDir, currentFolder)
            # List every file in the current folder
            for temp in os.listdir(currentFolder):
                fm = FileMover(originDir)
                fm.move(os.path.join(currentFolder, temp))
            try:
                os.rmdir(currentFolder)
            except OSError:
                print('Folder not empty')
                continue

def handleType(path, params):
    originDir = path[0]
    sortbyType(originDir)

def handleExtension(path, params):
    originDir = path[0]
    sortByExtension(originDir)

def handleDate(path, params):
    originDir = path[0]
    sortByDate(originDir, params)

def handleExtract(path, params):
    originDir, currentDir = path[0], path[0]
    extract(originDir, currentDir)

# def sortAlphabetically(path, precision):
#     for file in os.listdir(path):
#         currentLoc = path + "/" + file
#         fileExt = os.path.splitext(pathlib.Path(file))[0]
#         if os.path.isfile(currentLoc):
#             moved = False
#             for dir in os.listdir(path):
#                 if os.path.isdir(path + "/" + dir):
#                     if fileExt[0:precision] == dir[0:precision]:
#                         moved = True
#                         fm = FileMover()
#                         try:
#                             shutil.move(currentLoc, path + "/" + dir)
#                         except shutil.error:
#                             pass
#                 if not moved:
#                     try:
#                         os.mkdir(path + "/" + fileExt[0:precision])
#                         shutil.move(currentLoc, path + "/" +
#                                     fileExt[0:precision])
#                     except FileExistsError:
#                         pass
