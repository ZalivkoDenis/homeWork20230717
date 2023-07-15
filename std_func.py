import random


def input_int_number():
    while True:
        some_number = input("Enter number: ")
        if some_number.isdigit():
            result = int(some_number)
            break
    return result


def answer_rnd_int_number(min: int = 0, max: int = 100):
    return random.randint(min, max)


def clear_word_only_alfa(wrd: str) -> str:
    """
    Производит "очистку" строки от небукв
    :param wrd: строка (слово)
    :return: очищенная строка (слово)
    """
    res = list()
    for ch in wrd:
        if ch.isalpha():
            res.append(ch)

    return ''.join(res)


def output_out_params(*args):
    """
    Вывод на печать (в терминал) переданных аргументов
    :param args: Переданные аргументы для печати
    :return: Функция не возвращает значений
    """
    for item in args:
        print(item)

    return None


def clear_word_list_only_alfa(wrd_lst: list[str]) -> list[str]:
    return list(clear_word_only_alfa(item) for item in wrd_lst)


def initial_int_matrix(n: int, m: int = None) -> list[[int]]:
    """
    Инициализация матрицы n*m
    :param n: n
    :param m: m
    :return: list[n][m]
    """
    if m is None: m = n
    some_list = [[]] * n
    for index in range(n):
        some_list[index] = [0] * m
    return some_list


def fill_int_matrix_random(matrix: list[[int]], min_value: int = None, max_value: int = None):
    """
    Заполнение матрицы m*n рандомными INT-значениями
    :param matrix: Изменяемая матрица. Должна быть уже проинициализирована, т.к. доступ к элементам будет уже по
    индексам.
    :param min_value: Минимальное значение из диапазона случайных чисел
    :param max_value: Максимальное значение для диапазона случайных чисел
    :return:
    """
    if min_value is None: min_value = 0
    if max_value is None: max_value = 100
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(min_value, max_value)
    return None


def get_matrix_axis_y(matrix: list[[]], axis_y: int) -> tuple:
    result = tuple()
    for i in range(0, len(matrix)):
        result += matrix[i][axis_y],
    return result


def get_matrix_axis_x(matrix: list[[]], axis_x: int) -> tuple:
    return tuple(item for item in matrix[axis_x])


def get_vector_reverse(vector: list) -> tuple:
    return tuple(vector[::-1])


def print_matrix(matrix: list[[]]):
    """
    Вывод в терминал квадратной матрицы
    :param matrix: Матрица m*n
    :return:
    """
    for item in matrix:
        print(item)
    return None


def print_vector(vector: tuple):
    print('Элементы вектора: ', end='')
    for item in vector:
        print(item, end=' ')


def func_a_b(a, b):
    return a + b
