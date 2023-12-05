range_of_items = range(0, 11)

for number in range_of_items:
    print(number, end=" ")
else:
    print("\nLoop 1 was finished with success")


print(" ========================== ")

for number in range_of_items:
    print(number, end=" ")
    if number == 6:
        break
else:
    print("Loop 2 was finished with success")


