def int_to_roman(number):
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result = ''
    for value, symbol in roman_map:
        while number >= value:
            result += symbol
            number -= value

    return result


def roman_to_int(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman):
        current_value = roman_values[char]
        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value
        prev_value = current_value

    return total


print(f'521 = {int_to_roman(521)}')
print(f'2824 = {int_to_roman(2824)}')

print(f'DXII = {roman_to_int("DXII")}')
print(f'MMDCCCXXIV = {roman_to_int("MMDCCCXXIV")}')