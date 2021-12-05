import random

print("Welcome To Your Password Generator")

# Characters used in password generation
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

# Stores the number of passowrds to be generated
numberOfPasswords = input("Amount of passwords to generate: ")

numberOfPasswords = int(numberOfPasswords)

# Stores the length of the passwords
lengthOfPasswords = input("Input your password length: ")

lengthOfPasswords = int(lengthOfPasswords)

if (numberOfPasswords == 1):
    print("\nHere is your password:")
else:
    print("\nHere are your passwords:")

# Generates the passwords
for pwd in range(numberOfPasswords):
    passwords = ""
    for c in range(lengthOfPasswords):
        passwords += random.choice(chars)
    print(passwords)