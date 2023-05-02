def love_calculator(name1, name2):
    both_name = f"{name1.lower()}{name2.lower()}"

    compatibility = int(
        f"{both_name.count('t') + both_name.count('r') + both_name.count('u') + both_name.count('e')}{both_name.count('l') + both_name.count('o') + both_name.count('v') + both_name.count('e')}")

    if compatibility < 10 or compatibility > 90:
        return f"Your score is {compatibility}, you go together like coke and mentos."
    elif 40 < compatibility < 50:
        return f"Your score is {compatibility}, you are alright together."
    else:
        return f"Your score is {compatibility}"


name1 = input("What is your name? ")
name2 = input("What is their name? ")

print(love_calculator(name1, name2))
