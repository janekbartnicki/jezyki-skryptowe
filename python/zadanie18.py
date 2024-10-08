def get_number():
    num = input('Podaj liczbę: ')

    try:
        num = int(num)
        print('Liczba jest liczbą całkowitą')
    except ValueError:
        try:
            num = float(num)
            print('Liczba jest liczbą rzeczywistą')
        except ValueError:
            print('Wprowadzona wartość nie jest liczbą')


get_number()
