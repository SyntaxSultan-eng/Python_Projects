matrix_1 = []
matrix_2 = []
MainMatrix = []

# Главное правило - можно одну матрицу умножить на другую, если количество столбцов в первой матрице совпадает с количеством строк во второй матрице!

x = input().split() # кол-во строк и столбцов
for _ in range(int(x[0])): # Первая матрица
    matrix_1.append(input().split())
  
input()  #Просто пробел   

y = input().split() # кол-во строк и столбцов
for _ in range(int(y[0])): # Вторая матрица
    matrix_2.append(input().split())

######################### Алгоритм умножения матриц ################

counter = 0
for _ in range(int(x[0])):
    temp = []
    for i in range(int(x[0])):
        sum = 0
        for j in range(int(x[1])):
            sum += int(matrix_1[counter][j])*int(matrix_2[j][i])
        temp.append(sum)
    MainMatrix.append(temp)
    counter += 1

###################################################################

for item in MainMatrix:
    print(*item)
