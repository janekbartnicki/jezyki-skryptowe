import cmath


def add_complex_numbers(z1, z2):

    return z1 + z2


def multiply_complex_numbers(z1, z2):
    return z1 * z2


def divide_complex_numbers(z1, z2):
    return z1 / z2


def complex_modulus(z):
    return abs(z)


def complex_arc_length(z):
    return cmath.phase(z)


z1 = 1 + 4j
z2 = 6 - 2j

print("Dodawanie:", add_complex_numbers(z1, z2))
print("Mnożenie:", multiply_complex_numbers(z1, z2))
print("Dzielenie:", divide_complex_numbers(z1, z2))
print("Moduł:", complex_modulus(z1))
print("Długość łuku:", complex_arc_length(z1))