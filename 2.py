from tkinter import *
window = Tk()
window.title("Button Action")
window.geometry('350x200')
lbl = Label(window, text="")
lbl.pack()
def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me", command=clicked)
btn.pack()
window.mainloop()