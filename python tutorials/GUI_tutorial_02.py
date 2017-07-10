from tkinter import *

root = Tk()

one = Label(root, text="one", bg="red", fg="white")
one.pack()
two = Label(root, text="two", fg="black", bg="white")
two.pack(fill=X)
three = Label(root, text="three", fg="white", bg="purple")
three.pack(side=LEFT, fill=Y)

root.mainloop()
