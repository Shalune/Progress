from tkinter import *

#https://www.youtube.com/watch?v=RTM9tiV_HoY

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="beep", fg="red")
button2 = Button(topFrame, text="boop", fg="purple")
button3 = Button(topFrame, text="bope", fg="blue")
button4 = Button(topFrame, text="nope", fg="white")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
