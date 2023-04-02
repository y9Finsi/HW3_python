# Функция для проверки симметричности массива
def isSymmetric(matrix):
 # Создаем нов массив, жругую относительно исходной
 transposed_matrix = [list(row) for row in zip(*matrix)]
 # Сравниваем исходн массив
 # Если они равны, то массив симметрич
 # Если нет, то массив несимметрич
 return 'YES' if matrix == transposed_matrix else 'NO'
# Получаем количество 
num = int(input())
# Получаем 
matrix = [list(map(int, input().split())) for _ in range(num)]
# Проверяем симметричность массива и выводим результат
print(isSymmetric(matrix))
