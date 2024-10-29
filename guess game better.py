while(True):
    print("press Q to quit the game")
    a = input("enter number : ")
    if a == 'Q':
        break
    try:
        a = int(a)

        if a<6:
            print("you entered number less then 6")
        elif a > 6:
            print("you entered number Greater then 6")
    except Exception as E:
        print(f"you entered a wrong input {E}")
print("Thankyou for playing this game")
