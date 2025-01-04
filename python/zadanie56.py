import random

def shuffle_list(input_list):
    shuffled = input_list.copy()

    for i in range(len(shuffled) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]

    return shuffled


array = [1, 2, 3, 4, 5]
print("Oryginał:", array)
print("Pomieszana:", shuffle_list(array))
