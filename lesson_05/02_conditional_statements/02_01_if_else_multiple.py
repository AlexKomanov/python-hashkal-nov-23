age = int(input("What is your age: "))
who_are_you = input("Who are you: ")

if age >= 18:
    if who_are_you == "male":
        print("male 18+")
    else:
        print("female 18+")
elif age < 18:
    if who_are_you == "male":
        print("male 18+")
    else:
        print("female 18+")
else:
    print("No one of the options")




