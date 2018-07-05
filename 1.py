from tkinter import *

root = Tk()
hwL = Label(root, text='Hello World!!')
hwL.pack()
exitB = Button(root, text='exit', width=25, \
               command=root.destroy)
exitB.pack()
root.mainloop()