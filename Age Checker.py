print("Welcome In")
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