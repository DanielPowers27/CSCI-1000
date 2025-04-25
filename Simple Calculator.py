
while True:
    print("Simple Calculator")
    while True:
        number_one = input("Enter First Number:")
        try:
            num1 = int(number_one)
            break
        except ValueError:
            print(f"{number_one} is an invalid input, please use numerical form.")
    while True:
        number_two = input("Enter Second Number:")
        try:
            num2 = int(number_two)
            break
        except ValueError:
            print(f"{number_two} is an invalid input, please use numerical form.")
    print("Choose your operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice =input("Enter Choice(1/2/3/4):")
    if choice == '1':
        result = num1 + num2
        print(f"Sum:{result}")
    elif choice == '2':
        result = num1 - num2
        print(f"Difference:{result}")
    elif choice == '3':
        result = num1 * num2
        print(f"Product:{result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"Quotient:{result}")
        else:
            print("Error: Cannot divide by zero")
    else:
        print("Invalid Choice")
    while True:
        restart = input("Would you like to use me again, Yes or No:").lower()
        if restart == "yes":
            print("Great!")
            break
        elif restart == "no":
            print("Shutting Down...")
            exit()
        else:
            print("Invalid input, input must be a Yes or No response!")
            print("Try Again")







#This was my original Calculator Code
"""print("Simple Calculator")
num1 =float(input("Enter First Number:"))
num2 =float(input("Enter Second Number:"))
print("Choose your operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice =input("Enter Choice(1/2/3/4):")
if choice == '1':
    result = num1 + num2
    print(f"Sum:{result}")
elif choice == '2':
    result = num1 - num2
    print(f"Difference:{result}")
elif choice == '3':
    result = num1 * num2
    print(f"Product:{result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"Quotient:{result}")
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid Choice")"""



#This was a test code to learn how to use f
"""Name =input("Enter Your Name:")
Age =input("Enter Your Age:")
print(f"My name is {Name}, and I am {Age} years old!")"""