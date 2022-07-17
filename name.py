name = input("Enter your name: ")
if len(name) < 3 :
    print("Too short.Name must be at least 3 characters.")
elif len(name) > 40 :
    print("Name is too long")
else:
    print("Name looks good")