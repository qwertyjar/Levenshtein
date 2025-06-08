def levenshtein_distance(s1, s2, insert_cost=1, delete_cost=1, replace_cost=1):
    M = len(s1)
    N = len(s2)

    # Создаем матрицу D размером (M+1) x (N+1)
    D = [[0] * (N + 1) for _ in range(M + 1)]

    # Инициализация первой строки и первого столбца
    for i in range(1, M + 1):
        D[i][0] = D[i - 1][0] + delete_cost
    for j in range(1, N + 1):
        D[0][j] = D[0][j - 1] + insert_cost

    # Заполнение матрицы
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if s1[i - 1] != s2[j - 1]:
                cost_replace = D[i - 1][j - 1] + replace_cost
            else:
                cost_replace = D[i - 1][j - 1]
            cost_delete = D[i - 1][j] + delete_cost
            cost_insert = D[i][j - 1] + insert_cost

            D[i][j] = min(cost_delete, cost_insert, cost_replace)

    return D[M][N]

def main():
    while True:
        print("\nМеню:")
        print("1. Вычислить расстояние Левенштейна")
        print("2. Выйти")
        choice = input("Выберите действие (1/2): ")

        if choice == '1':
            str1 = input("Введите первое слово: ")
            str2 = input("Введите второе слово: ")
            distance = levenshtein_distance(str1, str2)
            print(f"Расстояние Левенштейна между '{str1}' и '{str2}': {distance}")
        elif choice == '2':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()