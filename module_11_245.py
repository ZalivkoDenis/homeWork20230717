"""
4) 11.245 (использовать только один проход по исходному массиву, только один цикл!). Дан массив. Переписать его
        элементы в другой массив такого же размера следующим образом: сначала должны идти все отрицательные элементы,
        а затем все остальные. Использовать только один проход по исходному массиву.
"""
import random

import std_func


def task_11_245(in_list: list[int]) -> list[int]:
    result = []
    for item in in_list:
        if item < 0:
            result.insert(0, item)
        else:
            result.append(item)
    return result


def main():
    mass = []
    items_count = 10
    for _ in range(items_count):
        mass.append(random.randint(-10, 10))
    print('Входной массив: ')
    std_func.output_out_params(mass)
    print('Выходной массив: ')
    res_mass = task_11_245(mass)
    print(res_mass)


if __name__ == "__main__":
    main()
