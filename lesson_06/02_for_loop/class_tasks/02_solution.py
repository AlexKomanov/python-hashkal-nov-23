for i in range(1, 10):
    print(i, end=" ")
    for j in range(1, 10):
        # print("{:2d}".format(i * j), end=" ")  #  double-digit numbers
        print(i * j, end="\t")
    print()
