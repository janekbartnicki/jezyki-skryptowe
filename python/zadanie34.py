iterator = 1

for gender in ('Kobieta', 'Mężczyzna'):
    for color in ('biały', 'czarny', 'zielony', 'czerwony', 'niebieski', 'żółty', 'szary'):
        for size in ('XXL', 'XL', 'L', 'M', 'S', 'XS'):
            filename = f'./metki/metka_{iterator}.txt'
            iterator += 1
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f'płeć: {gender}\nkolor: {color}\nrozmiar: {size}')
