from tkinter import *
from PIL import ImageTk , Image


root = Tk()
root.iconbitmap("icon.ico")
my_img = ImageTk.PhotoImage(Image.open("faislabad.png"))
mylabel = Label(image=my_img)
mylabel.pack()


root.mainloop()