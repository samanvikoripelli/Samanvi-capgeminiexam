def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False
while True:
    year = int(input("enter year(or 0 to exit):"))
    if year == 0:
        break
    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")