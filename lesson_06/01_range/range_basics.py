# print(range(10))
# print(range(2, 10))


last_number = int(input("Choose your last number: "))

for number in range(last_number):
    if number % 2 == 0:
        print(number, end=" ")
