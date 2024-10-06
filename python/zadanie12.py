get_elements = True
elements = []

print('Wpisuj elementy (wciśnij klawisz Enter aby zakończyć wpisywanie)...')
while get_elements:
    user_element = input('Podaj kolejny element: ')
    if user_element == '':
        get_elements = False
    else:
        elements.append(user_element)

for item in elements:
    print(item)