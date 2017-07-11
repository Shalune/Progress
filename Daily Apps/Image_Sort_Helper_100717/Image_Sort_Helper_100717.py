import os
from tkinter import *

dirSortFrom = 'C:\\Users\\Tyler E Main\\Desktop\\album\\unsorted\\'
dirAlbum = 'C:\\Users\\Tyler E Main\\Desktop\\album\\'
dirAlbumFolders = ['_art ref', '_mystuff', 'camera dump',
                   'characters', 'design', 'funny', 'gifs and stuff',
                   'HS', 'moments - feelings', 'my designs', 'narrative',
                   'scans', 'setting', 'stories', 'style']
startButtonText = "Start"
currentImageFile = ''
currentImageIndex = -1
folderButtons = []


def openImage(imageName):
    os.startfile(imageName)


def closePhotoViewer():
    os.system('TASKKILL /F /IM nomacs.exe')


def populateUI(window, startButton, imageFiles):
    startButton.pack_forget
    for folder in dirAlbumFolders:
        makeFolderButton(window, folder, imageFiles)
    for newButton in folderButtons:
        newButton.pack()


def makeFolderButton(window, folder, imageFiles):
    targetDir = dirAlbum + folder + '\\'
    newButton = Button(window, text=folder.replace(dirSortFrom, ''), command=lambda: folderButtonFn(currentImageFile, targetDir, imageFiles))
    folderButtons.append(newButton)


def runApp(window, startButton):
    imageFiles = getImageFiles()
    populateUI(window, startButton, imageFiles)
    loadNextImage(imageFiles)


def loadNextImage(imageFiles):
    global currentImageIndex, currentImageFile
    currentImageIndex += 1
    if imageFiles[currentImageIndex] is None:
        sys.exit()
    currentImageFile = imageFiles[currentImageIndex]
    openImage(imageFiles[currentImageIndex])


def getImageFiles():
    images = []
    for file in os.listdir(dirSortFrom):
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".bmp") or file.endswith(".gif"):
            images.append(dirSortFrom + file)
    return images


def folderButtonFn(imageFile, targetDir, imageFiles):
    moveImage(imageFile,targetDir)
    closePhotoViewer()
    loadNextImage(imageFiles)


def moveImage(imageFile, targetDir):
    oldFilePath = imageFile
    newFilePath = imageFile.replace(dirSortFrom, targetDir)
    os.rename(oldFilePath, newFilePath)


window = Tk()
startButton = Button(window, text=startButtonText)
startButton['command'] = lambda: runApp(window, startButton)
startButton.pack()
window.mainloop()
