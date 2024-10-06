def get_user_number():
    try:
        user_number = input('Podaj liczbę: ')
        user_number = int(user_number)
        return user_number

    except ValueError:
        print('Wpisana wartość nie jest liczbą!')


print(get_user_number())
