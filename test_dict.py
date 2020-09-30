import pytest
import random


@pytest.fixture(scope='class')
def random_dict():
    dict = {}
    for i in range(random.randint(1, 4)):
        key = ''.join([chr(random.randint(1, 10000)) for j in range(i)])
        dict[key] = random.randint(-1000, 1000)
    return dict


class TestDictMethods:
    def test_dict_clear(self, random_dict):
        clear_dict = random_dict.clear()
        assert clear_dict is None

    def test_dict_copy(self, random_dict):
        copy_of_dict = random_dict.copy()
        assert copy_of_dict == random_dict

    def test_dict_get(self):
        dict_example = {'n': 8}
        assert dict_example.get('n') == 8


@pytest.mark.parametrize('num', ['1', '2', '4', '6'])
def test_dict_key_to_value(num):
    dict_example = {'1': 1, '6': 6, '2': 2, '4': 4}
    assert dict_example[num] == int(num)


def test_dict_update():
    dict_example = {'arsenal': 'top', 'mu': 'good', 'liverpool': 100}
    len_before = len(dict_example)
    dict_example.update({'RUBIN KAZAN': 1000})
    assert len(dict_example)-1 == len_before
