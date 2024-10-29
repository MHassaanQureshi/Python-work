#password manager
name = input("please varify your name: ")
if name == "hassaan" or "laiba":
    print("welcome " +name)
else:
    print("invalid name!!!!")
    quit()
master_pass = input("Enter Program Password: ")
if master_pass == "hassaan23":
    print("you can process though")
else:
    print("invalid password!!")
    print("program ended!!!!")

    quit()
def view():
    with open('password.txt' , 'r') as f:
        for line in f.readlines():
            print(line)



def add():
    acc = input("enter Account name: ")
    password = input("enter password: ")

    with open('password.txt' , 'a') as f:
        f.write("account no :" +acc +" \n password: " +password + "\n")

while True:
    print("What do you want to do add or view your password file ")
    command = input("type view to view or add to add in file or Q to exit ")
    if command == "add":
        add()
    elif command == "view":
        view()
    elif command == "Q":
        print("thank you "  + name)
        break

