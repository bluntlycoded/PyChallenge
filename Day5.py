#PyPassword Generator
#Question:Take Input Of Length Of Password From User,How Many Charecters How Many Symbols And How Many Numbers 
#Then Input A random Password For The User

#Solution:

import random
n=int(input("Enter the length of password: "))
s=int(input("Enter the number of symbols: "))
c=int(input("Enter the number of characters: "))
d=int(input("Enter the number of digits: "))
password=""
for i in range(0,s):
    password+=random.choice("!@#$%^&*()")
for i in range(0,c):
    password+=random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(0,d):
    password+=random.choice("0123456789")
password=list(password)
random.shuffle(password)
password="".join(password)
print("Your password is:",password[0:n])
