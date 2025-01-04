def get_letters_array():
    file = open('./tekstwejsciowy.txt')
    return list(file.readline())


letters_dict = {}
for letter in get_letters_array():
    if letter not in letters_dict:
        letters_dict[letter] = 1
    else:
        letters_dict[letter] += 1

for letter in letters_dict:
    print(f'{letter}: {letters_dict[letter]}')