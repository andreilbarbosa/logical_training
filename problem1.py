#The first problem is, discover if a disk number is even or odd!

number = int(input("Disk a number:"))

if number % 2 == 0:
    print(f"The number {number} is even!")
else:
    print(f"The number {number} is odd!")
