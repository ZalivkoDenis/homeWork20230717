"""
1) 9.183. Даны два предложения. Напечатать слова, которые встречаются в двух предложениях только один раз.

"""

from std_func import clear_word_list_only_alfa as cwl
from std_func import output_out_params


def task_9_183(snt1: str, snt2: str, case_sensitive: bool = False) -> tuple:
    """
    Даны два предложения.
    Напечатать слова, которые встречаются в двух предложениях только один раз.

    :param snt1: Предложение №1
    :param snt2: Предложение №2
    :param case_sensitive: регистронезависимый поиск
    :return: Слова, которые встречаются в двух предложениях только один раз.
    """
    result = set()

    if not case_sensitive:
        result.update(cwl(snt1.lower().split()) + cwl(snt2.lower().split()))
    else:
        result.update(cwl(snt1.split()) + cwl(snt2.split()))
    result.discard('')
    return tuple(result)


def output_in_params(*args):
    print(f'Предложение 1:\n\t{args[0]}\n'
          f'Предложение 2:\n\t{args[1]}\n')
    return




def main():
    sentence1 = 'Добро пожаловать в мир!'
    sentence2 = 'Добро должно быть с кулаками... Мир суров )'
    output_in_params(sentence1, sentence2)
    output_out_params(task_9_183(sentence1, sentence2))
    return


if __name__ == '__main__':
    main()
