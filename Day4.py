#ROCK PAPER SCISSORS GAME
#Question:Create A Rock Paper Scissors Game using Random Mdoule in Python
import random
print("Welcome To Rock Paper Scissors Game")
x=random.randint(0,41)
userinput=int(input("Enter\n 1.For Rock\n2.For paper\n3.For Scisors\nEnter Your Input:"))
if (x<10):
    print("Stone")
    if userinput==2:
        print("You Win\n GAME OVER")
    elif userinput==3:
        print("System Wins\n TRY AGAIN")
    elif userinput==1:
        print("Draw\nTRY AGAIN")
    else:
        print("Please Check Your Input")
elif(x<20):
    print("Scisors")
    if userinput==1:
        print("You Win\n GAME OVER")
    elif userinput==2:
        print("System Wins\n TRY AGAIN")
    elif userinput==3:
        print("Draw\nTRY AGAIN")
    else:
        print("Please Check Your Input")
else:
    print("Paper")
    if userinput==3:
        print("You Win\n GAME OVER")
    elif userinput==1:
        print("System Wins\n TRY AGAIN")
    elif userinput==2:
        print("Draw\nTRY AGAIN")
    else:
        print("Please Check Your Input")