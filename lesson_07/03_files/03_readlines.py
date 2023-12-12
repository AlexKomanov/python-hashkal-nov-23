file = open('example.txt', "r")
all_lines = file.readlines()

for line in all_lines:
    print(line)

file.close()

