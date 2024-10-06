import math


def print_value_n_times(value, n):
    print('@'.join([str(value)] * n))


print_value_n_times((-0.7 * math.e + 4.07), 10)
