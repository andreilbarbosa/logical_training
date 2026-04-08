#The third problem is to determine which average of numbers!

num1 = int(input("Enter the first value:"))
num2 = int(input("Enter the second value:"))
num3 = int(input("Enter the third value:"))

def average():
    return num1 + num2 + num3 / 3

if average() < 5:
    print("I'm sorry, you reprovad")
elif average() <= 6.5:
    print("Unfortunately, you are in the recuperation.")
else:
    print("You passed!")