def check_number(num):
    if type(num) is not int:
        print('To nie liczba')
    elif num == 0:
        print('To zero')
    elif num > 0:
        print('więcej niż zero')
    else:
        print('mniej niż zero')


check_number(1)
