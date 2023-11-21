import numpy as np
def Q(angle: float) -> np.array:
    '''Возвращает матрицу поворота на угол angle против часовой стрелки в двумерном пространстве.
    :param angle: Угол поворота.
    '''
    return np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])


def P(a: float, b: float) -> np.array:
    '''Возвращает матрицу коэффициетов канонического уравнения эллипса.
    :param a: Главная ось (x).
    :param b: Минорная ось (y).
    '''
    return np.array([[(a / 2) ** 2, 0], [0, (b / 2) ** 2]])

def inverse(M: np.array) -> np.array:
    '''Возвращает обратную матрицу.
    :param M: Произвольная матрица.'''
    if np.linalg.det(M) == 0:
        raise Exception('Матрица не имеет обратной.')
    else:
        return np.linalg.inv(M)


def transpose(M: np.array) -> np.array:
    '''Возвращает транспонированную матрицу.
    :param M: Произвольная матрица.'''
    return M.transpose()


def sqrt_diagonal(M: np.array) -> np.array:
    '''Возвращает корень из диагональной матрицы.
    :param M: Диагональная матрица.'''
    if np.count_nonzero(M - np.diag(np.diagonal(M))) == 0:
        return np.sqrt(M)
    else:
        raise Exception('Матрица не является диагональной.')


def S(P_i: np.array, Q_i: np.array, P_j: np.array, Q_j: np.array) -> np.array:
    '''Возвращает матрицу S_ij.
    :param P_i: Матрица значений главных осей в квадрате i-ого эллипса.
    :param Q_i: Матрица поворота i-ого эллипса.
    :param P_j: Матрица значений главных осей в квадрате j-ого эллипса.
    :param Q_j: Матрица поворота j-ого эллипса.'''
    return np.linalg.multi_dot([sqrt_diagonal(P_i), transpose(Q_i), Q_j, inverse(P_j), transpose(Q_j), Q_i, sqrt_diagonal(P_i)])
