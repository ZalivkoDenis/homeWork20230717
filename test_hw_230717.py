import pytest
import module_9_183

def test_9_183():
    assert  sorted(module_9_183.task_9_183('Мир, труд, май!','Миру - мир!!!', case_sensitive=False)) == ['май', 'миру', 'труд']

