def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    discr = b ** 2 - 4 * a * c
    return discr


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    discr = discriminant(a, b, c)
    if discr > 0:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        return x,
    else:
        return 'корней нет',


if __name__ == '__main__':
    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1))
