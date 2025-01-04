import math


def polygon_area(sides, length):
    if sides < 3:
        raise ValueError("Niewystarczająca ilość boków (conajmniej 3).")
    return (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))


print(polygon_area(4, 25))
