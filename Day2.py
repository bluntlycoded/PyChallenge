# Tip Calculator

#Question : Program Asks User For Total Bill Amount and Tip Percentage 
#and  no. of people to split the bill into and Prints the Total Bill Amount with Tip

# Solution:

print("Welcome to Tip calculator")
billamt=float(input("Enter The Total Bill Amount:"))
people=int(input("Enter No. Of people to split the bill into:"))
pertip=float(input("Enter The Percentage of the tip You Want to give:"))
wktip=(pertip/100)*billamt
total=billamt+wktip
print("Total Amount is:",total)
print("Each one should pay",(total/people))