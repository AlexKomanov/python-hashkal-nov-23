age = int(input("What is your age: "))

if age > 18:
    print("More")
elif age == 18:
    print("Exactly")
else:
    print("Less")

message = "More" if age > 18 else ("Exactly" if age == 18 else "Less")

print("message", message)
