#The first problem is, discover if a disk number is even or odd!

number = int(input("Disk a number:"))

if number % 2 == 0:
    print(f"The number {number} is even!")
else:
    print(f"The number {number} is odd!")

#This is the first form, but also make using function:

num = int(input("Let's start the test, disk a number:"))

def verify():
    if num % 2 == 0:
        return True 


if verify():
    print(f"The number {num} is even!")
else:
    print(f"The number {num} is odd!")