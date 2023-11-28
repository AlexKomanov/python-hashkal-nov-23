age = int(input("What is your age: "))

if 18 < age < 67:
    print("Your age is more than 18 and less than 67.")
elif age == 18:
    print("Your age is exactly 18.")
elif age >= 67:
    print("Your age is 67 or more.")
else:
    print("Your age is under 18.")

print("Outside if-else-elif...")


