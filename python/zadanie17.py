def get_number():
    try:
        user_input = input('Podaj liczbę całkowitą: ')
        return int(user_input)
    except ValueError:
        print('Podana wartość nie jest liczbą!')


print(get_number())