user_number = input("Podaj liczbę: ")

for i in range(7):
    print(''.join([user_number] * 5))


# zadanie 21

file = open('./wynikzadanie.txt', 'w')

for i in range(7):
    for j in range(5):
        file.write(user_number)
    file.write('\n')
