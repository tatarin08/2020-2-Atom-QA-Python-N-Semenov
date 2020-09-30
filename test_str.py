import pytest
import random


@pytest.fixture
def random_str():
    random_string = ''.join([chr(random.randint(1, 100000)) for j in range(10)])
    return random_string


class TestStrExcept:
    def test_str_assign(self, random_str):
        try:
            random_str[1] = 'a'
        except Exception as exception:
            assert type(exception).__name__ == 'TypeError'

    def test_str_multiple(self, random_str):
        with pytest.raises(TypeError):
            assert random_str * 'bkhb'


@pytest.mark.parametrize('example, result', [(1, True),
                                              (0, False),
                                              (-1, False)
                                              ])
def test_str_multiple(random_str, example, result):
    assert (len(random_str * example) != 0) == result


def test_str_concatenation(random_str):
    assert 'abc' + 'def' + '' == 'abcdef'


@pytest.mark.parametrize('i', list(range(4)))
def test_str_index(i):
    str_example = '0123'
    assert str_example[i] == str(i)
