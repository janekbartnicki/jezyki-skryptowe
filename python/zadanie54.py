from fractions import Fraction


def decimal_to_fraction(number):
    return str(Fraction(number).limit_denominator())


print(decimal_to_fraction(0.5))
