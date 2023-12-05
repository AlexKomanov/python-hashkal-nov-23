start_num = int(input("Enter your first number: "))
end_num = int(input("Enter your second number: "))

for item in range(start_num, end_num + 1):
    print("I'm number ", item)
    if item % 3 == 0 and item % 5 == 0:
        print("FizzBuzz")
    elif item % 3 == 0:
        print("Fizz")
    elif item % 5 == 0:
        print("Buzz")
    else:
        print(item)
    # if item % 3 == 0:
    #     print("Fizz", end="")
    # if item % 5 == 0:
    #     print("Buzz", end="")
    # if item % 5 != 0 and item % 3 != 0:
    #     print(item)
