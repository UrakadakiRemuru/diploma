import math
from typing import List, Sequence, Tuple, Optional, Dict

import numpy as np

from Generation.generation import ellipse
from Matrices.matrices import inverse, transpose, sqrt_diagonal, P, Q, S


def transform(elp: ellipse, c: Optional[Tuple] = None) -> tuple:
    '''Возвращает координаты центра преобразованного в окружность эллипса или эллипса.
    :param elp: Массив параметров эллипса.
    :param c: Опциональный параметр. Координаты центра j-ого эллипса.
    '''
    if c is None:
        return tuple(
            np.linalg.multi_dot(
                [inverse(sqrt_diagonal(P(elp.a, elp.b))), transpose(Q(elp.angle)), transpose(elp.coord_to_array())]))
    else:
        return tuple(
            np.linalg.multi_dot(
                [inverse(sqrt_diagonal(P(elp.a, elp.b))), transpose(Q(elp.angle)), transpose(np.array(list(c)))]))


def find_params_for_transformed_ellipse(S_ij: np.array, c: tuple) -> ellipse:
    '''Реализует приведение уравнения 2-ого порядка для эллипса к каноническому виду. Возвращает массив параметров эллипса.
    :param S_ij: Матрица эллипса полученная в результате линейного преобразования.
    :param c: Координаты центра эллипса.
    '''
    [[s_11, s_12], [s_21, s_22]] = S_ij
    c_x, c_y = c
    A = s_11
    B = (s_12 + s_21) / 2
    C = s_22
    D = -(2 * c_x * A + c_y * B) / 2
    E = -(2 * c_y * C + c_x * B) / 2
    F = c_x ** 2 * A + c_x * c_y * B + c_y ** 2 * C - 1
    s = A + C
    delta = np.linalg.det(np.array([[A, B],
                                    [B, C]]))
    Delta = np.linalg.det(np.array([[A, B, D],
                                    [B, C, E],
                                    [D, E, F]]))
    F_1 = Delta / delta
    A_1 = max([(s + math.sqrt(s ** 2 - 4 * delta)) / 2, (s - math.sqrt(s ** 2 - 4 * delta)) / 2])
    C_1 = s - A_1
    x, y = np.linalg.solve(np.array([[A, B], [B, C]]), np.array([-D, -E]))
    ang = math.atan((A_1 - A) / B) * 180 / math.pi
    return ellipse((x, y), 2 * math.sqrt(-F_1 / A_1), 2 * math.sqrt(-F_1 / C_1), ang)


def transform_ellipse(elp_i: ellipse, elp_j: ellipse) -> ellipse:
    '''Возвращает параметры преобразованного эллипса.
    :param elp_i: Массив параметров i-ого эллипса.
    :param elp_j: Массив параметров j-ого эллипса.'''
    c_j = transform(elp_i, elp_j.coord)
    S_ij = S(P(elp_i.a, elp_i.b), Q(elp_i.angle), P(elp_j.a, elp_j.b), Q(elp_j.angle))
    print(S_ij)
    return find_params_for_transformed_ellipse(S_ij, c_j)


def not_overlapping_border(elp: ellipse, width: float, height: float):
    w_list = [np.array([1, 0]), -np.array([1, 0]), np.array([0, 1]), -np.array([0, 1])]
    w_list = [transpose(w) for w in w_list]
    s_list = [width / 2, -width / 2, height / 2, -height / 2]
    for border in range(4):
        if (np.dot(transpose(w_list[border]), elp.coord) - s_list[border]) ** 2 >= \
                np.linalg.norm(np.linalg.multi_dot([sqrt_diagonal(P(elp.a, elp.b)),
                                                    transpose(Q(elp.angle)),
                                                    w_list[border]])) ** 2 and \
                np.dot(transpose(w_list[border]), elp.coord) <= s_list[border]:
            '''print((np.dot(transpose(w_list[border]), elp.coord) - s_list[border]) ** 2, \
                np.linalg.norm(np.linalg.multi_dot([sqrt_diagonal(P(elp.a, elp.b)),
                                                    transpose(Q(elp.angle)),
                                                    w_list[border]])) ** 2)
            print(np.dot(transpose(w_list[border]), elp.coord), s_list[border])'''
            marker = True
        else:
            marker = False
    return marker
