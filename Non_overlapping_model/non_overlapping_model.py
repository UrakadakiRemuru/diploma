import math
from typing import List, Sequence, Tuple, Optional

import numpy as np
from Matrices.matrices import inverse, transpose, sqrt_diagonal, P, Q, S


def transform(elp: List, c: Optional[Tuple] = None) -> tuple:
    '''Возвращает координаты центра преобразованного в окружность эллипса или эллипса.
    :param elp: Массив параметров эллипса.
    :param c: Опциональный параметр. Координаты центра j-ого эллипса.
    '''
    (c_x, c_y), a, b, ang = elp
    if c is None:
        return tuple(
            np.linalg.multi_dot([inverse(sqrt_diagonal(P(a, b))), transpose(Q(ang)), transpose(np.array([c_x, c_y]))]))
    else:
        return tuple(
            np.linalg.multi_dot([inverse(sqrt_diagonal(P(a, b))), transpose(Q(ang)), transpose(np.array(list(c)))]))


def find_params_for_transformed_ellipse(S_ij: np.array, c: tuple) -> list:
    '''Реализует приведение уравнения 2-ого порядка для эллипса к каноническому виду. Возвращает массив параметров эллипса.
    :param S_ij: Матрица эллипса полученная в результате линейного преобразования.
    :param c: Координаты центра эллипса.
    '''
    [[s_11, s_12], [s_21, s_22]] = S_ij
    print(S_ij)
    c_x, c_y = c
    print(c)
    A = s_11
    B = (s_12 + s_21) / 2
    C = s_22
    D = -(2 * c_x * A + c_y * B) / 2
    E = -(2 * c_y * C + c_x * B) / 2
    F = c_x ** 2 * A + c_x * c_y * B + c_y ** 2 * C
    s = A + C
    delta = np.linalg.det(np.array([[A, B], [B, C]]))
    Delta = np.linalg.det(np.array([[A, B, D], [B, C, E], [D, E, F]]))
    F_1 = Delta / delta
    A_1 = max([(s + math.sqrt(s ** 2 - 4 * delta)) / 2, (s - math.sqrt(s ** 2 - 4 * delta)) / 2])
    C_1 = s - A_1
    x, y = np.linalg.solve(np.array([[A, B], [B, C]]), np.array([-D, -E]))
    ang = math.atan((A_1 - A) / B) * 180 / math.pi
    return [(x, y), 2 * math.sqrt(-F_1 / A_1), 2 * math.sqrt(-F_1 / C_1), ang]


def transform_ellipse(elp_i: list, elp_j: list) -> list:
    '''Возвращает параметры преобразованного эллипса.
    :param elp_i: Массив параметров i-ого эллипса.
    :param elp_j: Массив параметров j-ого эллипса.'''
    c_i, a_i, b_i, ang_i = elp_i
    c_j, a_j, b_j, ang_j = elp_j
    c_j = transform(elp_i, c_j)
    S_ij = S(P(a_i, b_i), Q(ang_i), P(a_j, b_j), Q(ang_j))
    return find_params_for_transformed_ellipse(S_ij, c_j)
