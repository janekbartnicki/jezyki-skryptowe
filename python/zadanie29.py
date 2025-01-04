import string


def count_words(words):
    counter = {}

    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    return counter


def make_stats(filename):
    file = open(filename, 'r', encoding='utf-8')
    text = file.read().translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    count = count_words(words)

    print(f'Statystyka słów: {dict(sorted(count.items(), key=lambda x: x[1], reverse=True))}')
    print(f'Najczęściej występujące ({count[max(count, key=count.get)]} razy): "{max(count, key=count.get)}"')


make_stats('./tekstdostatystyki.txt')
