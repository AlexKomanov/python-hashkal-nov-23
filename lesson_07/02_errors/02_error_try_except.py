x = 12
try:
    print("Before x")
    print(x / 0)
    print("After x")
except NameError as er:
    print("Please define a variable.")
except Exception as er:
    print(er)
