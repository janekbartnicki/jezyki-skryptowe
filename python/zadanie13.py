def check_for_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    for vowel in vowels:
        print(f'{vowel}: {word.count(vowel)}')


user_word = input('Podaj słowo: ')
check_for_vowels(user_word)

