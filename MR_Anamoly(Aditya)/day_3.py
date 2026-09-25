#lets  caluclate the brute force password using python

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()-+"
print(f"Welcome! to the Brute Force Password Cracker\n")
print(f"You can use letters, numbers, and symbols(!@#$%^&*()-+)\n")
password =input("Enter the four-character password to brute force: ")
print("Brute forcing the password...")


def brute_force(password):
    all = lower + upper + digits + symbols
    attempts = 0

    for char1 in all:
        for char2 in all:
            for char3 in all:
                for char4 in all:
                    attempts += 1
                    guess = char1 + char2 + char3 + char4
                    if guess == password:
                        return guess, attempts

if len(password) != 4:
    print("Password must be four characters long.")
else:
    guess, attempts = brute_force(password)
    print(f"Password found: {guess} after {attempts} attempts.")
