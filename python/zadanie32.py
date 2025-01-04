import cmath

file = open('wspolczynniki.txt', "r")
a = float(file.readline().strip())
b = float(file.readline().strip())
c = float(file.readline().strip())

delta = cmath.sqrt(b ** 2 - 4 * a * c)
x1 = (-b + delta) / (2 * a)
x2 = (-b - delta) / (2 * a)

print(f"x1 = {x1}")
print(f"x2 = {x2}")
