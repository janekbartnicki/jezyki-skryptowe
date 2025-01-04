def custom_power(x, n):
    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    while n > 0:
        if n & 1:
            result *= x

        x *= x
        n >>= 1

    return result


print(f"2^3 = {custom_power(2, 3)}")
print(f"5^2 = {custom_power(5, 2)}")
print(f"2^-2 = {custom_power(2, -2)}")
