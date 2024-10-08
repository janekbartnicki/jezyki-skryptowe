import random


def get_element_from_file(element_line):
    file = open('./dane_zadanie19.txt', 'r')
    lines = file.readlines()
    return lines[element_line]


from_range = int(input("Podaj początek przedziału: "))
to_range = int(input("Podaj koniec przedziału: "))

if from_range > to_range:
    from_range, to_range = to_range, from_range

print(f'Oto losowa liczba z podanego przedziału: {random.randrange(from_range, to_range)}')
print('Losowy element z pliku: ', get_element_from_file(random.randrange(0, 19)))
