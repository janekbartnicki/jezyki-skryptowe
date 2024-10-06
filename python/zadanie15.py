def get_numbers():
    is_get_numbers = True
    nums = []

    print('Wpisuj liczby (wciśnij klawisz Enter aby zakończyć wpisywanie)...')
    while is_get_numbers:
        user_element = input('Podaj kolejny element: ')
        if user_element == '':
            is_get_numbers = False
        else:
            nums.append(int(user_element))

    return nums


def avg(nums):
    return sum(nums) / len(nums)


def med(nums):
    if len(nums) % 2 == 0:
        return (nums[len(nums) / 2 + 1] + nums[len(nums) / 2 - 1]) / 2
    else:
        return nums[len(nums) / 2]


numbers = get_numbers()

print(f'Suma: {sum(numbers)}')
print(f'Średnia: {avg(numbers)}')
print(f'Mediana: {med(numbers)}')

