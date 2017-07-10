from tkinter import *
import os

desktop = 'C:\\Users\\Tyler E Main\\Desktop\\'
placeInto = 'C:\\Users\\Tyler E Main\\Desktop\\album\\unsorted\\'


def cleanButton():
    images = gatherImages()
    moveImages(images)
    return


def gatherImages():
    images = []
    for file in os.listdir(desktop):
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".bmp") or file.endswith(".gif"):
            images.append(desktop+file)
    return images


def moveImages(images):
    #
    for image in images:
        moveFile(image)
    return


def moveFile(image):
    oldFilePath = image
    newFilePath = image.replace(desktop,placeInto)
    os.rename(oldFilePath, newFilePath)
    return


window = Tk()
button = Button(window, text="press", command=cleanButton)
button.pack()

window.mainloop()