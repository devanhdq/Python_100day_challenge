import random as rd

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

index = rd.randint(0, len(names) - 1)

print(f"{rd.choice(names)} is going to buy the meal today!")
