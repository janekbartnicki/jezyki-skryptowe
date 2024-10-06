def square_root(num):
    if num >= 0:
        return num ** (1/2)
    else:
        return f'{(-num) ** (1/2)}i lub -{(-num) ** (1/2)}i'


print(square_root(-23))
