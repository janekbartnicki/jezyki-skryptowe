import random

cols = int(input('Podaj ilość kolumn: '))
rows = int(input('Podaj ilość wierszy: '))
start_range = int(input('Podaj zakres początkowy liczb losowych: '))
end_range = int(input('Podaj zakres końcowy liczb losowych: '))

if start_range > end_range:
    start_range, end_range = end_range, start_range

file = open('./danewygenerowane.txt', 'w')

for row in range(rows):
    for col in range(cols):
        file.write(str(random.randrange(start_range, end_range)) + ' ')
    file.write('\n')
