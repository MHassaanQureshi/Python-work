from tkinter import *
from PIL import ImageTk , Image


root = Tk()
root.iconbitmap(r"E:\python projects\GUI/icon.ico")
my_img = ImageTk.PhotoImage(Image.open(r"E:\python projects\GUI\pictures\1.png"))
my_img1 = ImageTk.PhotoImage(Image.open(r"E:\python projects\GUI\pictures\2.png"))
my_img2= ImageTk.PhotoImage(Image.open(r"E:\python projects\GUI\pictures\3.png"))
my_img3= ImageTk.PhotoImage(Image.open(r"E:\python projects\GUI\pictures\4.png"))
my_img4= ImageTk.PhotoImage(Image.open(r"E:\python projects\GUI\pictures\5.png"))
my_img5= ImageTk.PhotoImage(Image.open(r"E:\python projects\GUI\pictures\8.png"))
my_img6= ImageTk.PhotoImage(Image.open(r"E:\python projects\GUI\pictures\9.png"))
image_list = [ my_img5 , my_img6]


my_label = Label(image=my_img5)
my_label.grid(row = 0 , column=0 , columnspan=3)


def forward(imagenm):
    global button_back
    global button_forword
    global my_label
    my_label.grid_forget()
    my_label = Label(image=image_list[imagenm - 1])
    my_label.grid(row = 0 , column=0 , columnspan=3)
    button_back = Button(root , text ="<<" , command=lambda : back(imagenm - 1))
    button_back.grid(row = 1 , column = 0 )
    button_forword = Button(root , text =">>",command=lambda :forward(imagenm + 1))
    button_forword.grid(row = 1 ,column = 1)
    if imagenm == 0:
        button_forword = Button(root , text =">>",state=DISABLED)
    

def back(imagenm):
    global button_back
    global button_forword
    global my_label
    my_label.grid_forget()
    my_label = Label(image=image_list[imagenm - 1])
    my_label.grid(row = 0 , column=0 , columnspan=3)
    button_back = Button(root , text ="<<" , command=lambda : back(imagenm - 1))
    button_back.grid(row = 1 , column = 0 )
    button_forword = Button(root , text =">>",command=lambda :forward(imagenm + 1))
    button_forword.grid(row = 1 ,column = 1)
    if imagenm == 1:
        button_back= Button(root , text ="<<",state=DISABLED)
    



button_back = Button(root , text ="<<" , command=back ,state=DISABLED)
button_back.grid(row = 1 , column = 0 )
button_forword = Button(root , text =">>",command=lambda:forward(2))
button_forword.grid(row =1 ,column=1)
button = Button(root , text = "exit" , command=root.quit)
button.grid(row=1 , column=2)

root.mainloop()