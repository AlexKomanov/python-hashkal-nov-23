range_of_items = range(0, 21)

for number in range_of_items:
    if number == 12:
        print(number)
        break
    if number % 3 == 0:
        continue
    print(number)

