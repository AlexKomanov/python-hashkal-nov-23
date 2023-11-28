status_code = int(input("What is your status code: "))

match status_code:
    case 100:
        print("Your code is 100")
    case 200 | 201 | 202 | 203:
        print("Status code of 200 group")
    case 300:
        print("Status code of 300 group")
    case 400:
        print("Your code is 400")
    case _:
        print("The code is unknown")
