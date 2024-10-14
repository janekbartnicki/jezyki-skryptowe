import math


def eq_1():
    alpha = int(input('Podaj α: '))
    beta = int(input('Podaj β: '))

    result_plus = 2 * math.sin(.5 * (alpha + beta)) * math.cos(.5 * (alpha - beta))
    result_minus = 2 * math.sin(.5 * (alpha - beta)) * math.cos(.5 * (alpha + beta))

    print(f'sin α + sin = {result_plus}')
    print(f'sin α - sin = {result_minus}')


def eq_2(amount):
    x = int(input('Podaj x: '))
    n = int(input('Podaj n: '))
    sum = 0

    for k in range(1, amount + 1):
        sum += (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) * math.pow(x, k)

    print(sum)

# eq_1()
eq_2(5)
