while True:
    def add(a,b):
        return a + b
    def subtract(a,b):
        return a - b
    def multiply(a,b):
        return a * b
    def divide(a,b):
        return a/b
    print("Simple Calculator")
    num1 = int(input("What is your first number?:"))
    num2 = int(input("What is your second number?:"))
    print("Choose an Operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    Choice = input("Which would you like to use 1/2/3/4? ")
    if Choice == "1":
        print(num1,"+",num2,"=",add(num1,num2))
    elif Choice == "2":
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif Choice == "3":
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif Choice == "4":
        if num2 != 0:
            print((num1,"/",num2,"=",divide(num1,num2)))
        else:
            print("Error: Divided by zero")
    else:
        print("Invalid Choice")
    Restart = input("Would you like to try again? Yes or No?: ").lower()
    if Restart == "yes":
        print("Great!")
        print("Rebooting Now...")
    else:
        print("Shutting Down...")
        exit()