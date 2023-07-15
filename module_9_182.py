"""
2) 9.182 (которые есть только в первом предложении). Даны два предложения. Напечатать слова, которые есть только в
одном из них (в том числе повторяющиеся).
"""

import std_func
from std_func import output_out_params as oop
from std_func import clear_word_list_only_alfa as cwl


def task_9_182(snt1: str, snt2: str, case_sensitive: bool = False) -> tuple[str]:

    def clear_one_for_two(l1: list[str], l2: list[str]):
        res = set()
        l1 = cwl(l1)
        l2 = cwl(l2)
        for item in l1:
            if not item in l2:
                res.add(item)
        return tuple(res)

    res = set()
    snt1 = snt1
    snt2 = snt2
    if not case_sensitive:
        snt1 = snt1.lower()
        snt2 = snt2.lower()

    res.update(clear_one_for_two(snt1.split(), snt2.split()))
    res.update(clear_one_for_two(snt2.split(), snt1.split()))

    res.discard('')

    return tuple(res)


def output_in_params(*args):
    print(f'Предложение 1:\n\t{args[0]}\n'
          f'Предложение 2:\n\t{args[1]}\n')
    return


def main():
    sentence1 = 'Добро пожаловать в мир!'
    sentence2 = 'Добро должно быть с кулаками... Мир суров )'
    output_in_params(sentence1, sentence2)

    print('Результат (case_sensitive = False):')
    oop(task_9_182(sentence1, sentence2, case_sensitive=False))

    print('\nРезультат (case_sensitive = True):')
    oop(task_9_182(sentence1, sentence2, case_sensitive=True))

    return


if __name__ == '__main__':
    main()
