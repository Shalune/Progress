from tkinter import *
import os

baseDir = 'C:'
desktop = baseDir +  os.path.join(os.environ["HOMEPATH"], "Desktop")
album = os.path.join(desktop, 'album\\')
placeInto = os.path.join(album, 'unsorted\\')

FileOptions = [ 'Images', 'Audio', 'Video', 'Documents']
FileTypes = {'Images' : [".png", ".jpg", ".bmp", ".gif"],
            'Audio' : [".mp3", ".wav", ".m4a"],
            'Video' : [".mp4", ".mov", ".wmv"],
            'Documents' : [".doc", ".docx", ".txt", ".pdf"]}


def cleanButton(fromFolderInput, toFolderInput, fileTypeDropDown):
    files = gatherFiles(fromFolderInput, fileTypeDropDown)
    toFolder = toFolderInput.get()
    moveFiles(files, toFolder)


def gatherFiles(fromFolderInput, dropDownVar):
    dir = fromFolderInput.get()
    fileTypes = FileTypes[dropDownVar.get()]
    images = []
    images = addFilesInDir(images, dir, fileTypes)
    return images


def addFilesInDir(images, dir, fileTypes):
    for file in os.listdir(dir):
        if isFileType(file, fileTypes):
            images.append(dir+'\\'+file)
    return images


def isFileType(file, fileTypes):
    for type in fileTypes:
        if file.endswith(type):
            return True
    return False


def moveFiles(files, toFolder):
    for oneFile in files:
        moveFile(oneFile, toFolder)


def moveFile(file, toFolder):
    oldFilePath = file
    newFilePath = file.replace(oldImageDir(file),toFolder + '\\')
    os.rename(oldFilePath, newFilePath)


def oldImageDir(image):
    return image[:image.rfind('\\')]


window = Tk()
fromFolder = Entry(window, text="Pull from...")
toFolder = Entry(window, text="Move to...")

dropDownVar = StringVar(window)
dropDownVar.set(FileOptions[0])
dropDown = OptionMenu(window, dropDownVar, *FileOptions)

button = Button(window, text="press")
button['command'] = lambda: cleanButton(fromFolder, toFolder, dropDownVar)

fromFolder.pack()
toFolder.pack()
dropDown.pack()
button.pack()
window.mainloop()