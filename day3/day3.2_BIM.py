height = float(input("Enter your height (m): "))
weight = int(input("Enter your weight (kg):"))

bim = round(weight / height ** 2, 2)

if bim < 18.5:
    print(f"Your BIM is {bim},you are underweight")
elif 18.5 < bim < 25:
    print(f"Your BIM is {bim},you are normal weight")
elif 25 < bim < 30:
    print(f"Your BIM is {bim},you are slightly overweight")
elif 30 < bim < 35:
    print(f"Your BIM is {bim},you are obese")
else:
    print(f"Your BIM is {bim},you are clinically obese")
