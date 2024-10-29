from tkinter import *
root = Tk()

e = Entry(root , width=50 , bg="blue" , fg = "white" , borderwidth=10)
e.pack()
e.insert(0 , "enter your name:")
def click():
    mylabel = Label(root , text = "hey!!!" + e.get())
    mylabel.pack()



mybutton = Button(root , text = "click for greeting.", command=click , fg="blue" ,bg = "black",padx=50 , pady=100)
mybutton.pack()

root.mainloop()