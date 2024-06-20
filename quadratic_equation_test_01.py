import pytest


@pytest.mark.parametrize("a, b, c, expected", [
    (1, 8, 15, (-3.0, -5.0)),  # Дискриминант > 0, два корня
    (1, -13, 12, (12.0, 1.0)),  # Дискриминант > 0, два корня
    (-4, 28, -49, (3.5,)),  # Дискриминант == 0, один корень
    (1, 1, 1, ('корней нет',))  # Дискриминант < 0, корней нет
])
def test_solution(a, b, c, expected):
    from quadratic_equation01 import solution
    assert solution(a, b, c) == expected


@pytest.mark.parametrize("a, b, c, expected", [
    (1, 8, 15, 4),  # Дискриминант = 64 - 60 = 4
    (1, -13, 12, 121),  # Дискриминант = 169 - 48 = 121
    (-4, 28, -49, 0),  # Дискриминант = 784 - 784 = 0
    (1, 1, 1, -3)  # Дискриминант = 1 - 4 = -3
])
def test_discriminant(a, b, c, expected):
    from quadratic_equation01 import discriminant
    assert discriminant(a, b, c) == expected
