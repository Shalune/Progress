import os
from tkinter import *

baseDir = 'C:'
dirAlbum = os.path.join(os.environ["HOMEPATH"], 'Desktop\\album\\')
dirSortFrom = os.path.join(dirAlbum, 'unsorted\\')
dirAlbumFolders = ['_art ref', '_mystuff', 'camera dump',
                   'characters', 'design', 'funny', 'gifs and stuff',
                   'HS', 'informative', 'moments - feelings', 'my designs', 'narrative',
                   'scans', 'setting', 'stories', 'style', 'other']
startButtonText = "Start"
currentImageFile = ''
currentImageIndex = -1
folderButtons = []


def main():
    window = Tk()
    startButton = Button(window, text=startButtonText)
    startButton['command'] = lambda: runApp(window, startButton)
    startButton.pack()
    window.mainloop()


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
    os.rename(baseDir + oldFilePath, baseDir + newFilePath)


if __name__ == "__main__":
    main()