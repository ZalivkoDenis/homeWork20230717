import pytest
import module_9_183
import module_9_182
import module_8_54
import module_11_245
import module_options_task_1


def test_9_183():
    assert sorted(module_9_183.task_9_183('Мир, труд, май!', 'Миру - мир!!!', case_sensitive=False)) == ['май', 'миру',
                                                                                                         'труд']


def test_9_182():
    assert sorted(module_9_182.task_9_182('Мир, труд, май!', 'Миру - мир!!!', case_sensitive=False)) == ['май', 'миру',
                                                                                                         'труд']


def test_8_54():
    assert module_8_54.task_8_84(11) == (11,)
    assert module_8_54.task_8_84(14) == (2,7)


def test_11_245():
    assert sorted(module_11_245.task_11_245([1,2,3,-3,-2,-1])) == [-3,-2,-1,1,2,3]


def test_opt_1():
    assert module_options_task_1.task_options_1([[1,2],[3,4]],[[5,6],[7,8]]) == [[6,8],[10,12]]