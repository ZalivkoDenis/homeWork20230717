"""
    5) Задача (1): Даны две матрицы. Написать функцию для нахождения суммы этих матриц.
"""
import random
import std_func


def task_options_1(m1: list[[int]], m2: list[[int]]) -> list[[int]] | None:
    if (len(m1) != len(m2)) or (len(m1[0]) != len(m2[0])):
        return None
    res = [[0] * len(m1) for _ in range(len(m1[0]))]
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            res[i][j] = m1[i][j] + m2[i][j]
    return res


def main():
    # Задаём размерность массива
    n = random.randint(2, 5)

    m1 = std_func.initial_int_matrix(n,n)
    std_func.fill_int_matrix_random(m1)
    print('Матрица 1: ')
    std_func.print_matrix(m1)

    m2 = std_func.initial_int_matrix(n,n)
    std_func.fill_int_matrix_random(m2)
    print('Матрица 2: ')
    std_func.print_matrix(m2)

    res = task_options_1(m1, m2)
    print('Сумма матриц m1+m2: ')
    std_func.print_matrix(res)
    pass


if __name__ == "__main__":
    main()
