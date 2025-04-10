"""def add(a,b):
    return a + b
print(add(3, 5))"""

"""def subtract(a,b):
    return a - b
print(subtract(4,2))"""

"""def multiply(a,b):
    return a * b
print(multiply(5,5))"""

"""def divide(num1,num2):
    if num2 ==0:
        return"Error"
    else:
        return num1/num2
print(divide(10,2))"""


print("Simple Calculator")
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
    print("Invalid Choice")



"""Name =input("Enter Your Name:")
Age =input("Enter Your Age:")
print(f"My name is {Name}, and I am {Age} years old!")"""