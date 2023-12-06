num_1 = int(input("1: "))
num_2 = int(input("2: "))


def sum_of_nums(numb_1: int, numb_2: int):
    return numb_1 + numb_2


res = sum_of_nums(num_1, num_2)
print(res)

# res = sum_of_nums(num_2) # missing 1 required positional argument: