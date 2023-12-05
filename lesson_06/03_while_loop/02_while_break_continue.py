number = 0

while number < 20:
    number += 1
    if number == 10:
        break
    if number % 5 == 0:
        continue
    print(number)
