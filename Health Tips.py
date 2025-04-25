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
health_assistant()

"""Choose = input("Choose an option").lower()
if Choose == "health tips":
    start:(health_assistant())"""