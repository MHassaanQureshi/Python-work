from tkinter import *
root = Tk()

e = Entry(root , width=30 , borderwidth=10)
e.grid(row = 0 , column = 0 ,columnspan=3 , padx=10 , pady=10)

def add(numbers):
    current = e.get()
    e.delete(0, END)
    e.insert(0 , str(current) +str(numbers))
def clear():
    e.delete(0 , END)

def button_add():
    firstnum = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(firstnum)
    e.delete(0 , END)


def button_sub():
    firstnum = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(firstnum)
    e.delete(0, END)

def button_mul():
    firstnum = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(firstnum)
    e.delete(0, END)
def button_div():
    firstnum = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(firstnum)
    e.delete(0, END)
def equal():
    secondnum = e.get()
    e.delete(0 , END)
    if math == "addition":
        e.insert(0, f_num + int(secondnum))
    elif math == "substraction":
        e.insert(0, f_num - int(secondnum))
    elif math == "multiplication":
        e.insert(0, f_num * int(secondnum))
    elif math == "division":
        e.insert(0, f_num / int(secondnum))

button_1 = Button(root,text = "1" ,padx = 40 , pady = 20 , command=lambda :add(1)).grid(row= 1 , column = 0)
button_2 = Button(root,text = "2" ,padx = 40 , pady = 20 , command =lambda : add(2)).grid(row= 1 , column = 1)
button_3 = Button(root,text = "3" ,padx = 40 , pady = 20 ,command =lambda : add(3)).grid(row= 1 , column = 2)
button_4 = Button(root,text = "4" ,padx = 40 , pady = 20 ,command =lambda : add(4)).grid(row= 2 , column = 0)
button_5 = Button(root,text = "5" ,padx = 40 , pady = 20 ,command = lambda : add(5)).grid(row= 2 , column = 1)
button_6 = Button(root,text = "6" ,padx = 40 , pady = 20, command =lambda : add(6)).grid(row= 2 , column = 2)
button_7 = Button(root,text = "7" ,padx = 40 , pady = 20, command =lambda : add(7)).grid(row= 3 , column = 0)
button_8 = Button(root,text = "8" ,padx = 40 , pady = 20, command =lambda : add(8)).grid(row= 3 , column = 1)
button_9 = Button(root,text = "9" ,padx = 40 , pady = 20,command = lambda : add(9)).grid(row= 3 , column = 2)
button_0 = Button(root,text = "0" ,padx = 40 , pady = 20, command =lambda : add(0)).grid(row= 4 , column = 0)

button_add = Button(root,text = "+" ,padx = 40 , pady = 20 ,command=button_add).grid(row= 4 , column = 1)
button_clear = Button(root,text = "clear" ,padx = 138, pady = 20 , command=clear).grid(row= 6 , column = 0 ,columnspan = 3)
button_equal = Button(root,text = "=" ,padx = 40 , pady = 20 , command=equal).grid(row= 4, column = 2)
button_substract = Button(root,text = "-" ,padx = 42 , pady = 20 ,command=button_sub).grid(row= 5, column = 0)
button_divide = Button(root,text = "/" ,padx = 42 , pady = 20  ,command = button_div).grid(row= 5, column = 1)
button_multiply = Button(root,text = "*" ,padx = 42 , pady = 20 ,command= button_mul).grid(row= 5, column = 2)



root.mainloop()