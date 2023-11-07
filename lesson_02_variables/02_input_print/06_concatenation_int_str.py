name = input("Your name: ")
last_name = input("Your last name: ")
age = int(input("Your last age: "))

# print("Your name is " + name + ".\nYour last name is " + last_name + ".\nYour age is " + str(age))
# print("Your name is ", name, ".\nYour last name is ", last_name, ".\nYour age is ", age)
print(f"Your name is {name.upper()}, \nYour last name is {last_name.upper()}.\nNext year your age is {age+1}")
