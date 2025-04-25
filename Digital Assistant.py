#Simple Calculator Code
def simple_calculator():
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
    choice = input("Enter Choice(1/2/3/4):")
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
        restart = input("Would you like to use Digital Assistant again, Yes or No:").lower()
        if restart == "yes":
            print("Great!")
            break
        elif restart == "no":
            print("Shutting Down Digital Assistant...")
            exit()
        else:
            print("Invalid input, input must be a Yes or No response!")
            print("Try Again")

#Health Assistant Code
def health_assistant():
    print("Welcome to your Virtual Health Assistant!")
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
        print("I would speak with your doctor to learn how to properly increase your body weight.")
    elif bmi < 25:
        print("Health: Normal weight")
        print("Great Job!")
    elif bmi < 30:
        print("Health: Overweight")
        print("I would recommend starting a simple diet.")
    elif bmi < 40:
        print("Health: Obese")
        print("I would recommend talking to your doctor to learn how to healthily lose weight")
    else:
        print("Health: Severe Obesity")
        print("Talk to your doctor, you are at risk of heart diseases!")
    while True:
        restart = input("Would you like to use Digital Assistant again, Yes or No:").lower()
        if restart == "yes":
            print("Great!")
            break
        elif restart == "no":
            print("Shutting Down Digital Assistant...")
            exit()
        else:
            print("Invalid input, input must be a Yes or No response!")
            print("Try Again")

#Age Checker Code
def age_checker():
    print("Welcome to your Virtual Age Checker!")
    while True:
        user_input = input("How old are you?:")
        try:
            age = int(user_input)
            if age <=0:
                print(f"{age} is an invalid input, your age can't be negative.")
            else:
                break
        except ValueError:
            print(f"{user_input} is an invalid input, please enter your age using digits. (e.g., 14, 29, 36)")
    if age <=13:
        print(f"You are {age} years old, which makes you a child.")
    elif age <=17:
        print(f"You are {age} years old, which makes you a teenager.")
    elif age <=64:
        print(f"You are {age} years old, which makes you an adult.")
    elif age <=100:
        print(f"You are {age} years old, which makes you a senior citizen.")
    else:
        print(f"You are {age} years old, how are you still alive???")
    while True:
        restart = input("Would you like to use Digital Assistant again, Yes or No:").lower()
        if restart == "yes":
            print("Great!")
            break
        elif restart == "no":
            print("Shutting Down Digital Assistant...")
            exit()
        else:
            print("Invalid input, input must be a Yes or No response!")
            print("Try Again")

while True:
    print("Welcome to My Digital Assistant!")
    user = input("What is your name?:")
    while True:
        print(f"Sure {user}, Choose One of The Options Below:")
        while True:
            print("1. Health Tips")
            print("2. Simple Calculator")
            print("3. Age Checker")
            app = input("Which would you like?:").lower()
            if app == "1" or app == "1. health tips" or app == "one" or app == "health tips":
                (health_assistant())
            elif app == "2" or app == "2. simple calculator" or app == "two" or app == "simple calculator":
                (simple_calculator())
            elif app == "3" or app == "3. age checker" or app == "three" or app == "age checker":
                (age_checker())
            else:
                print("Invalid Option, Try Again.")