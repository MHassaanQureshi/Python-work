from tkinter import *
from PIL import ImageTk , Image


root = Tk()
root.iconbitmap(r"C:\Users\Indus\Desktop\python projects\GUI\icon.ico")
my_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Indus\Desktop\python projects\GUI\uni.png"))
mylabel = Label(image=my_img)
mylabel.pack()




button = Button(root , text = "exit" , command=root.quit)
button.pack()
root.mainloop()