#The third problem is to calculate which average of numbers!

num1 = int(input("Enter the first value:"))
num2 = int(input("Enter the second value:"))
num3 = int(input("Enter the third value:"))

def average():
    return (num1 + num2 + num3) / 3

avg = average()

if avg < 5:
    print("I'm sorry, you failed.. Your note: {avg}")
elif avg <= 6.5:
    print("Unfortunately, you are in recovery. Your note: {avg}")
else:
    print("You passed! Your note: {avg}")