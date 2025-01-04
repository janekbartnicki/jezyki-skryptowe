def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


start_year = int(input('Podaj początek zakresu: '))
end_year = int(input('Podaj koniec zakresu: '))

for year in range(start_year, end_year + 1):
    if is_leap_year(year):
        print(year)
