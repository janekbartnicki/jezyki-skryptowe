def get_numbers():
    nums = []
    file = open('./dane_zadanie16.txt', 'r')

    for line in file:
        nums.append(int(line))

    return nums


def avg(nums):
    return sum(nums) / len(nums)


def med(nums):
    if len(nums) < 1:
        return
    nums.sort()
    if len(nums) % 2 == 0:
        return (nums[int(len(nums) / 2 + 1)] + nums[int(len(nums) / 2 - 1)]) / 2
    else:
        return nums[int(len(nums) / 2)]


numbers = get_numbers()

print(f'Suma: {sum(numbers)}')
print(f'Średnia: {avg(numbers)}')
print(f'Mediana: {med(numbers)}')

