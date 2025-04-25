"""list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
i = 0
while i<len(list):
  print(list[i])
  i += 1"""


"""list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for y in list:
    print(y)
print("Loop Complete")"""


"""password = input("Enter Password:")
if password == "Kangaroo":
  print("Welcome Admin!")
elif password == "Dog":
  print("Welcome Student!")
else:
  print("Access Denied")"""


"""print("Colors of the Rainbow: Red, Orange, Yellow, ???, Blue, Indigo, Violet")
color = input("What Color is Missing in this Rainbow? ")
if color == "Green" or "green":#I tested the word "or" to see if this would accept both inputs and it worked
  print("That's Right!")
else:
  print("Sorry, that's not right!")"""

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



"""Name =input("Enter Your Name:")
Age =input("Enter Your Age:")
print(f"My name is {Name}, and I am {Age} years old!")"""


"""my_tup = [1, "Wonderful", True, 'wonderful', True, False, 1.0]
my_tup[5] = True
print(my_tup)"""


"""a = ['mary', 'had','a','little','lamb']
for i in range(len(a)):
    print(i, a[i])"""


"""for i in range(3):
    print(i)
#output = 0 1 2"""

"""for i in range(0,3):
    print(i)
#output = 0 1 2"""

"""for i in range(1,3):
    print(i)
#output = 1 2"""

"""for i in range(2,3):
    print(i)
#output = 2"""

"""for i in range(3,3):
    print(i)
#output = nothing because it starts and stops at 3"""

"""for i in range(1, 10, 2): #2 is the steps or number between numbers
    print(i)
#output = 1 3 5 7 9"""

"""for i in range(1, 10, 3): #3 is the steps or number between numbers
    print(i)
#output = 1 4 7 No 10 because 10 is the stop"""

"""for i in range(0, 21, 2):
    print(i)
#output 0 2 4 6 8 10 12 14 16 18 20 Try to print only even numbers 0 to 20"""

"""for i in range(-2, 20, 2):
    print(i+2)
#output 0 2 4 6 8 10 12 14 16 18 20 This method also works for printing even only from numbers 0 to 20"""

def health_assistant():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        print("Health: Underweight")
    elif bmi < 25:
        print("Health: Normal weight")
    elif bmi < 30:
        print("Health: Overweight")
    else:
        print("Health: Obese")

health_assistant()

