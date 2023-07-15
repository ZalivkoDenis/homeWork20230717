""""
    3) 8.54 (можно random'ом). Дано натуральное число n. Получить все простые делители этого числа.
"""
import random

import std_func


def task_8_84(n: int) -> tuple:
    res = set()
    check_divider = 2
    while check_divider ** 2 <= n:
        if n % check_divider == 0:
            res.add(check_divider)
            n //= check_divider
        check_divider += 1
    if n > 1:
        res.add(n)
    return tuple(res)


def main():
    n = random.randint(0, 100)
    print(f'Число, для которого будем искать простые делители: {n}')
    print("Результат:")
    std_func.output_out_params(task_8_84(n))


if __name__ == '__main__':
    main()
