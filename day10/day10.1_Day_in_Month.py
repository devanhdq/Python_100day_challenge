def check_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 400 == 0) and (year % 100 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    is_leap = check_leap_year(year)
    if month > 12 or month < 1:
        return "Invalid month entered."
    elif month == 1 or month == 3 or month == 5 or month == 7 \
            or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        if is_leap:
            return 29
        else:
            return 28
    else:
        return 30


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

