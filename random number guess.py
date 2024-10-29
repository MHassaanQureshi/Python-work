import random
def guess(randomNO , you):
    if randomNO  == you:
       print("you guessed it correct")
    elif randomNO > you:
        print("you number is lesser")
    elif randomNO < you:
        print("you number is greater")



print("computer is selecting a number .........")
randomNO = random.randint(1 , 100)
you = int(input("select your number :"))
a = guess(randomNO,you)

