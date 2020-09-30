import pytest


class Test_add_and_multi:
    def test_int_addition(self):
        assert 2 + 1 == 3 and -2 + 4 == 2

    def test_int_multiplication(self):
        assert 5 * 10 == 50 and 0 * 1 == 0 and 12 * 3 == 36


@pytest.mark.parametrize('example, result', [('4/1', 4),
                                              ('4/2', 2),
                                              ('-8/-2', 4)
                                              ])
def test_int_res(example, result):
    assert eval(example) == result


def test_int_sign():
    assert (-1)*(-1) == 1


def test_int_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        assert 1/0
