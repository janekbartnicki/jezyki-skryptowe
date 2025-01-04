import string

def wersaliki(filename):
    input_file = open(filename, 'r', encoding='utf-8')
    text = input_file.read().translate(str.maketrans('', '', string.punctuation)).lower()

    output_file = open('./wersaliki.txt', 'w', encoding='utf-8')
    output_file.write(text.upper())


wersaliki('./tekstdostatystyki.txt')