#random1.py

i=1
while i>0:

    import random


    fruit=["apple","mango","grapes","pineapple"]
    a=(random.choice(fruit))
    b=(random.choice(fruit))
    print(fruit)
    c=input("Please enter a item in the above list any two:")
    d=input("Please enter a item in the above list any two:")
    print("we guess---->",a,b)
    print("you guess---->",c,d)
    if a&b in c&d:
        print("you guess correct")
        print("if you want to play again")
        e=input("please enter yes/no")
        f="no"
        if e in f:
             print("thank you for playing")
             i=0
             break

        else:
            print("thank you for playing again")

        

    else:
        print("unless correct please play the game")
