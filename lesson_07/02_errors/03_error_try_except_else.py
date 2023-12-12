x = 12
try:
    print("Before x")
    print(x / 2)
    print("After x")
except NameError as er:
    print("Please define a variable.")
except Exception as er:
    print(er)
else:
    print("Else Block - everything was OK.")
