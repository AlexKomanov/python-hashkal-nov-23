num_1 = 5
num_2 = 10


def sum_of_nums(numb_1: int, numb_2: int = 0):
    return numb_1 + numb_2


res = sum_of_nums(num_1, 0)
print(res)

res = sum_of_nums(num_2)
print(res)
