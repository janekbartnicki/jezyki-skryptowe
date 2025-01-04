def count_vowels(text):
    vowels = 'aeiouąęóyAEIOUĄĘÓY'
    vowel_count = sum(1 for char in text if char in vowels)

    return vowel_count


print(f"Vowels in 'Języki Skryptowe': {count_vowels('Języki Skryptowe')}")