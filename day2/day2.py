print("Wellcome to tip calculator")

total = float(input("What was the total bill?\n"))
split = int(input("How many people to split the bill?\n"))
tip = int(input("What percent tip would you like to give? 10, 12 or 15\n"))

result = ((total / 100 * tip) + total) / split
round_result = round(result, 2)
round_result = "{:.2f}".format(round_result)

print(f"Each person should pay ${round_result}")
