#Tresure Island 

#Question:Using Conditional Statements Make A game Of Tresure Island

print("Welcome to Tresure Island")
print("your Mission is to find The Tresure")
print("You came Across Cross Road,Which Side You Will go\nEnter"+ "left"+"or"+"right")
y=input("Note Program is Case Sensitive\n Follow the exact Instructions")
if y=="left":
    print("You Fel Into A Lake Full Of Crocodile\nYou Are Dead!!!\nGAME OVER")
    pass
elif y=="right":
    print("You Came Across Another Turn\n Where do you want to turn"+"left or right")
    nm=input()
    if nm=="left":
        print("You Found The Trusure\nGAME OVER")
    else:
        print("You Are Dead\n GAME OVER")

        exit
else:
    print("Inavlid Input \n GAME OVER")
    exit
