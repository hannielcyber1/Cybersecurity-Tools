import random
import string

# Ask user for settings
min_length = int(input("Enter minimum password length: "))
max_length = int(input("Enter maximum password length: "))
num_passwords = int(input("Enter number of passwords to generate: "))

# Character set (lowercase + uppercase + numbers + symbols)
charset = string.ascii_letters + string.digits + string.punctuation

with open("password.lst", "w") as f:
    for _ in range(num_passwords):
        length = random.randint(min_length, max_length)
        password = ''.join(random.choices(charset, k=length))
        f.write(password + "\n")

print(f"\nGenerated {num_passwords} passwords in 'password.lst'")