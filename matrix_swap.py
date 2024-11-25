import random

def print_menu():
    print("\nМеню:")
    print("1. Ввод исходных данных вручную")
    print("2. Генерация случайной матрицы")
    print("3. Выполнение алгоритма")
    print("4. Вывод результата")
    print("5. Завершение работы программы")

def input_matrix():
    n = int(input("Введите размер матрицы (n x n): "))
    matrix = []
    print("Введите элементы матрицы (через пробел):")
    for i in range(n):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)
    return matrix

def generate_random_matrix(size):
    return [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]

def swap_rows_and_columns(matrix):
    min_row_index = None
    max_col_index = None
    min_value = float('inf')
    max_value = float('-inf')

    # Поиск минимального элемента и максимального элемента
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_row_index = i
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_col_index = j
                
    # Замена местами строки и столбца
    if min_row_index is not None and max_col_index is not None:
        for i in range(len(matrix)):
            # Смена строки с минимальным элементом на соответствующий столбец
            matrix[min_row_index][i], matrix[i][max_col_index] = matrix[i][max_col_index], matrix[min_row_index][i]

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    pass
    matrix = None
    result_displayed = False

    while True:
        print_menu()
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            matrix = input_matrix()
            result_displayed = False  # Сбрасываем флаг, так как введены новые данные
            
        elif choice == '2':
            size = int(input("Введите размер матрицы (n x n): "))
            matrix = generate_random_matrix(size)
            result_displayed = False  # Сбрасываем флаг, так как введены новые данные
            
        elif choice == '3':
            if matrix is not None:
                swap_rows_and_columns(matrix)
                result_displayed = False  # Сбрасываем флаг, так как выполнен алгоритм
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите данные.")
                
        elif choice == '4':
            if matrix is not None:
                display_matrix(matrix)
                result_displayed = True  # Успешно выведен результат
            else:
                print("Сначала введите данные.")
                
        elif choice == '5':
            print("Завершение работы программы.")
            break
            
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт из меню.")

if __name__ == "__main__":
    main()
