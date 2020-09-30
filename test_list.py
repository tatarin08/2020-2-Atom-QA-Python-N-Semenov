import pytest
import random


class TestMultiple:
    def test_multiple_int(self):
        list_example = ['a', 8, 'n']
        assert type(list_example*random.randint(-1, 1)).__name__ == 'list'

    def test_multiple_not_int(self):
        list_example = ['a', 8, 'n']
        with pytest.raises(TypeError):
            assert list_example*2.5


def test_list_concatenation():
    list_1 = [0, 2]
    list_2 = ['n', [4, 5]]
    assert list_1 + list_2 == [0, 2, 'n', [4, 5]]


@pytest.mark.parametrize('n', [0, 1, 2, 3, 4])
def test_list_index(n):
    list_example = [0, 1, 2, 3, 4]
    assert list_example[n] == n


def test_list_sort():
    list_example = [random.randint(1, 100) for i in range(3)]
    list_example.sort()
    assert all(list_example[i] <= list_example[i+1] for i in range(2))
