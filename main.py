""" Программа для решения уравнений с тремя неизвестными методом гаусса """
def get_matrix():
    "Обьявление и заполение матрицы"
    mat = [[0 for i in range(4)] for i in range(3)]
    for i in range(3):
        for j in range(4):
            mat[i][j] = float(input("Введите элемент A(" + str(i + 1) + "," + str(j + 1) + "): "))
    return mat
def one(matrix, n):
    "Приведение числа к еденице "
    if matrix[n][n] == 0:
        for i in range(1, len(matrix)):
            if matrix[i][n] != 0:
                matrix[n], matrix[i] = matrix[i], matrix[n]
                matrix[n][n] *= -1

    k = matrix[n][n]
    for i in range(4):
        matrix[n][i] = (matrix[n][i]/ k)

    return matrix
def gauss(matrix, n):
    "Функция вычисления новых значений матрицы методом гаусса"
    if n==0:
        for i in range(3):
            for j in range(4):
                matrix[i][j]= matrix[i][j] - (matrix[n][j] * matrix[i][n])

    elif n == 1:
        for i in [2,3]:
            matrix[n-1][i] = matrix[n-1][i] - matrix[n-1][n] * matrix[n][i]
            matrix[n+1][i] = matrix[n+1][i] - matrix[n+1][n] * matrix[n][i]

    elif n == 2:
        for i in [0,1]:
            matrix[i][n+1] = matrix[i][n+1] - matrix[i][n] * matrix[n][n+1]

    for i in [0, 1, 2]:
        matrix[i][n] = 0  # Обнуляем столбец

    matrix[n][n] = 1  # ставим единицу в нужное место для красоты
    return matrix
def iter(matrix, n):
    "Функция в который обьеденяет фунции приведения числа к еденице и пересчёт элементов методом гаусса"
    matrix = (one(matrix, n))
    show_mat(matrix,3) #Это вывод матрицы в процессе решения
    matrix = gauss(matrix, n)
    show_mat(matrix,3) #Это вывод матрицы в процессе решения
    return matrix
def show_mat(matrix, n):
    "Красивый вывод матрицы"
    for i in range(n):
        print(matrix[i][0]," ",matrix[i][1]," ",matrix[i][2]," ",matrix[i][3]," ",)
def main():
    matrix = get_matrix()
    print("Матрица: ")
    show_mat(matrix, 3)
    for i in range(3):
        matrix = iter(matrix, i)

    print("\nОтветы: ")
    for i in range(3):
        print("x" + str(i), " = ", round(matrix[i][3]))

main()
input()