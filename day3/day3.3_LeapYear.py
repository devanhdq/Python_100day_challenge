# year = int(input("Enter year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         print(f"{year} is leap year")
#     else:
#         print(f"{year} is not leap year")
# else:
#     print(f"{year} is not leap year")


def check_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0):
        print(f"{year} is leap year")
    elif (year % 400 == 0) and (year % 100 == 0):
        print(f"{year} is leap year")
    else:
        print(f"{year} is NOT leap year")


for i in range(2020, 2999):
    print(check_leap_year(i))
