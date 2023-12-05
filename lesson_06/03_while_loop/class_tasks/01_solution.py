start_num = int(input("First num: "))
end_num = int(input("End num: "))

while start_num < end_num:
    if start_num == 7:
        break
    if start_num % 2 == 0:
        start_num += 1
        continue
    print(start_num)
    start_num += 1

