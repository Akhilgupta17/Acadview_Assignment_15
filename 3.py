from tkinter import *

root = Tk()
root.title('My App')
root.configure(background='#EEEEEE')
frame = Frame(root, bg='skyblue')
frame.grid(row=1,column=1)

userL = Label(frame, text='User Name')
userL.grid(row=1, column=0, sticky=E)
def clicked() :
    userL.configure(text='Changed')

submitB = Button(frame, text='Change', bg='yellow',\
                 activebackground='red', \
                 activeforeground='white', command=clicked)
exitB = Button(frame, text='Log Out', \
               command=root.destroy)
submitB.grid(row=2, column=0, sticky=W)
exitB.grid(row=2, column=1, sticky=E)

root.mainloop()