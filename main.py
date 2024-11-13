def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix


n = int(input('Введите количество строк матрицы :'))
m = int(input('Введите количество столбцов матрицы :'))
value = input('Введите значения матрицы : ')
print()
matrix = get_matrix(n, m, value)
if m <= 0:
    print([])
elif n <=0:
    print([])


