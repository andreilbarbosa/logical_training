#The second problem is to determine which number is greater!

number1 = int(input("Enter the first number:"))

number2 = int(input("Enter the second number:"))

if number1 > number2:
    print(f"The first number ({number1}) is greater than second number ({number2})!")
elif number1 == number2:
    print(f"Both numbers is the same! First number ({number1}) and second number ({number2}).")
else:
    print(f"The second number ({number2}) is greater than the first number ({number1})!")


#This is the first form, but also make using ternary:


if number1 == number2:
    print(f"Both numbers is the same! First number ({number1}) and second number ({number2}).")
else:
    result = number1 if number1 > number2 else number2
    if result == number2:
        print(f"The second number ({number2}) is greater than the first number ({number1})!")
    else:
        print(f"The first number ({number1}) is greater than second number ({number2})!")