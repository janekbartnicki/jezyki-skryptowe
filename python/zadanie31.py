import math

base = int(input('Podaj podstawę: '))
iterations = int(input('Podaj liczbę iteracji: '))
sum = base
print('licznik   suma')
print('**0**    **0**')
print('-----     -----')
stars_counter = 0
stars_sum = 0
for i in range(1, iterations + 1):
    built_string = ''

    if len(str(i)) <= 5:
        stars_counter = 5 - len(str(i))
        stars_sum = 5 - len(str(sum))

        if stars_counter % 2 == 0:
            built_string = (''.join(['*' for _ in range(int(stars_counter / 2))]) +
                            str(i) + ''.join(['*' for _ in range(int(stars_counter / 2))])) + '  |  '
        else:
            built_string = (''.join(['*' for _ in range(math.floor(stars_counter / 2))]) +
                            str(i) + ''.join(['*' for _ in range(math.ceil(stars_counter / 2))])) + '  |  '

        if stars_sum % 2 == 0:
            built_string += (''.join(['*' for _ in range(int(stars_sum / 2))]) +
                        str(sum) + ''.join(['*' for _ in range(int(stars_sum / 2))]))
        else:
            built_string += (''.join(['*' for _ in range(math.floor(stars_sum / 2))]) +
                             str(sum) + ''.join(['*' for _ in range(math.ceil(stars_sum / 2))]))

        print(built_string)
    else:
        print(f'{i}  |  {sum}')
    sum += base
