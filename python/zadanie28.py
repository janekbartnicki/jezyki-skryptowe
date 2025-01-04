def get_variables():
    print('an + bn = cn')
    rows = int(input('Podaj ilosc wierszy: '))
    matrix = []

    for row in range(1, rows + 1):
        an = int(input(f'Podaj a{row}: '))
        bn = int(input(f'Podaj b{row}: '))
        cn = int(input(f'Podaj c{row}: '))
        matrix.append([an, bn, cn])

    return matrix


matrix = get_variables()
result = []

for i in range(len(matrix)):
    max_row = i
    for k in range(i + 1, len(matrix)):
        if abs(matrix[k][i]) > abs(matrix[max_row][i]):
            max_row = k
    matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

    for j in range(i + 1, len(matrix)):
        factor = matrix[j][i] / matrix[i][i]
        for k in range(i, len(matrix) + 1):
            matrix[j][k] -= factor * matrix[i][k]

    if matrix[-1][-2] == 0 and matrix[-1][-1] != 0:
        print('Układ sprzeczny')

    result = [0] * len(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        result[i] = matrix[i][-1]
        for j in range(i + 1, len(matrix)):
            result[i] -= matrix[i][j] * result[j]
        result[i] /= matrix[i][i]

print(f'a: {result[0]}, b: {result[1]}')