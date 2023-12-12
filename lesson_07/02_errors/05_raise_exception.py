age = int(input("What is your age? "))

try:
    print("Checking your details...")
    if age < 18:
        raise Exception("Person under 18 is not allowed!")
    print("Welcome to our store")
except Exception as err:
    print(f"{err = }")
finally:
    print("Byeee!")
