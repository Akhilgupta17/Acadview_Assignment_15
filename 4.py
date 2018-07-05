from tkinter import *

def show_entry_fields():
   print("text is %s" % (e1.get()))

root = Tk()
Label(root, text="Write Something:").grid(row=0)
#Label(root, text="Last Name").grid(row=1)

e1 = Entry(root)
#e2 = Entry(root)

e1.grid(row=0, column=1)
#e2.grid(row=1, column=0)

Button(root, text='Quit', command=root.quit).grid(row=3, column=0, sticky=W,)
Button(root, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=E, )

mainloop( )