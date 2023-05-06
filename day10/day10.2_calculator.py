def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

number1 = int(input("Enter your number1: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
number2 = int(input("Enter your number2: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(number1, number2)

print(f"{number1} {operation_symbol} {number2} = {answer}")
