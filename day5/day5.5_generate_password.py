import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_of_letter = int(input("How many letters would you like in your password?\n"))
number_of_symbol = int(input("How many symbols would you like?\n"))
number_of_number = int(input("How many numbers would you like?\n"))

passwords = []

for s in range(1, number_of_symbol + 1):
    passwords.append(random.choice(number))

for n in range(1, number_of_number + 1):
    passwords.append(random.choice(symbols))

for n in range(1, number_of_letter + 1):
    passwords.append(random.choice(letters))

random.shuffle(passwords)

passwords_str = ""

for c in passwords:
    passwords_str += c

print(f"Your password is: {passwords_str}")
