from tkinter import *
import os

baseDir = 'C:'
desktop = baseDir +  os.path.join(os.environ["HOMEPATH"], "Desktop")
publicDesktop = os.path.join(baseDir, '\\Users\\Public\\Desktop')
placeInto = os.path.join(desktop, 'scripts\\shortcut pile')


def main():
    window = Tk()
    button = Button(window, text="press", command=cleanButton)
    button.pack()
    window.mainloop()


def cleanButton():
    shortcuts = gatherShortcuts()
    moveFiles(shortcuts)
    return


def gatherShortcuts():
    shortcuts = []
    shortcuts = addShortcutsInDir(desktop, shortcuts)
    shortcuts = addShortcutsInDir(publicDesktop, shortcuts)
    return shortcuts


def addShortcutsInDir(dir, shortcuts):
    result = shortcuts
    for file in os.listdir(dir):
        if isShortcut(file):
            result.append(dir+'\\'+file)
    return result


def isShortcut(file):
    if file.endswith(".lnk") or file.endswith(".url") or file.endswith(".appref-ms"):
        return True
    return False


def moveFiles(files):
    for file in files:
        moveFile(file)
    return


def moveFile(file):
    oldFilePath = file
    print(oldFilePath)
    newFilePath = file.replace(oldDir(file),placeInto)
    os.rename(oldFilePath, newFilePath)
    return


def oldDir(file):
    return file[:file.rfind('\\')]


if __name__ == "__main__":
    main()