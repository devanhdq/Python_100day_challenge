def orderPizza(size, add_pepperoni, extra_cheese):
    result_price = 0
    if size == "S":
        result_price += 15
        if add_pepperoni == "Y":
            result_price += 2
        if extra_cheese == "Y":
            result_price += 1
    elif size == "M":
        result_price += 20
        if add_pepperoni == "Y":
            result_price += 2
        if extra_cheese == "Y":
            result_price += 1
    else:
        if add_pepperoni == "Y":
            result_price += 2
        if extra_cheese == "Y":
            result_price += 1
        result_price += 25
    return result_price


size = input("What size pizza do you want? S, M, L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

print(f"Your final bill is: {orderPizza(size, add_pepperoni, extra_cheese)}")
