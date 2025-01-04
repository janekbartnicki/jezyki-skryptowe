import math


def eq_1():
    alpha = int(input('Podaj α: '))
    beta = int(input('Podaj β: '))

    result_plus = 2 * math.sin(.5 * (alpha + beta)) * math.cos(.5 * (alpha - beta))
    result_minus = 2 * math.sin(.5 * (alpha - beta)) * math.cos(.5 * (alpha + beta))

    print(f'sin α + sin = {result_plus}')
    print(f'sin α - sin = {result_minus}')


def eq_2():
    x = int(input('Podaj x: '))
    n = int(input('Podaj n: '))
    amount_of_runs = 100

    result = 1

    for i in range(1, amount_of_runs):
        result += ((n - (n - (i - 1))) * (x ** i)) / math.factorial(i)

    print(f'(1 + {x})^{n} = {result}')


def eq_3():
    a = int(input('Podaj a: '))
    b = int(input('Podaj b: '))
    c = int(input('Podaj c: '))

    x1 = (-b + math.sqrt(4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(4 * a * c)) / (2 * a)

    print(f'x1 = {x1}, x2 = {x2}')


def eq_4():
    result = 1
    x = int(input('Podaj x: '))

    for i in range(1, 100):
        result += (x ** i) / math.factorial(i)

    print(f'e^x = {result}')


def eq_5():
    a0 = float(input('Podaj a0: '))
    amount_of_n = int(input('Podaj liczbę wyrazów n: '))
    an = [float(input(f'Podaj a{n}: ')) for n in range(1, amount_of_n + 1)]
    bn = [float(input(f'Podaj b{n}: ')) for n in range(1, amount_of_n + 1)]
    x = float(input('Podaj x: '))
    L = float(input('Podaj L: '))

    result = a0

    for i in range(1, amount_of_n + 1):
        cos_eq = an[i - 1] * math.cos(i * math.pi * x / L)
        sin_eq = bn[i - 1] * math.sin(i * math.pi * x / L)
        result += cos_eq + sin_eq

    print(f'Wartość f(x) = {result}')

# eq_1()
# eq_2()
# eq_3()
# eq_4()
eq_5()