from tkinter import *
import os

baseDir = 'C:'
desktop = baseDir +  os.path.join(os.environ["HOMEPATH"], "Desktop")
album = os.path.join(desktop, 'album\\')
placeInto = os.path.join(album, 'unsorted\\')


def cleanButton():
    images = gatherImages()
    moveImages(images)
    return


def gatherImages():
    images = []
    images = addImagesInDir(images, desktop)
    images = addImagesInDir(images, album)
    return images


def addImagesInDir(images, dir):
    for file in os.listdir(dir):
        if isImage(file):
            images.append(dir+file)
    return images


def isImage(file):
    if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".bmp") or file.endswith(".gif"):
        return True
    return False


def moveImages(images):
    for image in images:
        moveFile(image)
    return


def moveFile(image):
    oldFilePath = image
    newFilePath = image.replace(oldImageDir(image),placeInto)
    os.rename(oldFilePath, newFilePath)
    return


def oldImageDir(image):
    return image[:image.rfind('\\')]


window = Tk()
button = Button(window, text="press", command=cleanButton)
button.pack()

window.mainloop()