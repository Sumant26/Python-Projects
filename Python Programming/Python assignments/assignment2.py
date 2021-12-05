name =  input("Enter your name: ")

def nameLength(name):
    if len(name) > 10:
        print("Name is very big")
    elif len(name) > 5:
        print("Name is Ok")
    else:
        print("Name is too short")
    return name
print(nameLength(name))

# nameLength(name)