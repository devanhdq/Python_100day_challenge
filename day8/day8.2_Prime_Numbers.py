import math


def prime_numbers(number):
    if number <= 1:
        return f"{number}: is NOT a prime number"
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return f"{number}: is NOT a prime number"
    return f"{number}: is a prime number"


def prime_number_for(number):
    is_prime = True
    if number <2:
        is_prime = False
    for n in range(2, number):
        if number % n == 0:
            is_prime = False

    if is_prime:
        return f"{number}: is a prime number"

    else:
        return f"{number}: is NOT a prime number"


for i in range(1, 101):
    print(prime_number_for(i))

# print(prime_numbers(2))
