age = int(input("What is your age: "))

if age >= 18:
    print("Your age is 18 or more.")
else:
    print("Your age is under 18")

print("Outside if-else...")

# Ternary

print("Your age is 18 or more.") if age >= 18 else print("Your age is under 18")
print("Outside ternary operator")
