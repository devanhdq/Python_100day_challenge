input_age = input("What is your current age?\n")

age = 90 - int(input_age)

days = age * 365
weeks = age * 52
months = age * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left")
