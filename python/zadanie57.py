import random


def random_element_from_file():
    with open('./dane_zadanie57.txt', 'r') as file:
        lines = list(file.readlines())
        random_index = random.randint(0, len(lines) - 1)
        return lines[random_index].strip()


print(random_element_from_file())
