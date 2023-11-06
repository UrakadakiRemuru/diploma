from typing import List, Any
from helpers import get_key_by_value

A = [[-2, 3, -3], [1, 1, -3], [2, -1, -4]]

def format_matrix(A: List[List]) -> List[List]:
    A = [[el * (-1) if ind != len(row) - 1 else el for ind, el in enumerate(row)] for row in A]
    return A

def search_negative_free_coefficient(A: List[List]) -> Any:
    '''Функция осуществляет поиск наибольшего отрицательного свободного коэффициента (a_i).
    A - матрица коэффициентов системы неравенств (ограничений) вида: -a_i1(-x_1) - ... -a_in(-x_n) + a_i <= 0 (i = 1, ..., m).
    Каждый массив - набор коэффициентов соответствующего неравенства.
    Функция возвращает порядковый номер массива, т.е порядковый номер неравенства,
    которому он принадлеждит,в случае отсутствия отрицательного коэффициента возвращает True.'''
    negative_coef_dict = {}
    for r, row in enumerate(A):
        val = row[-1]
        if val < 0:
            negative_coef_dict.update({r: val})
    if negative_coef_dict:
        return get_key_by_value(negative_coef_dict, min(list(negative_coef_dict.values())))



def search_negative_coefficient(A: List[List]) -> Any:
    '''Функция производит поиск первого отрицательного коэффициента неравенства.
    A - матрица коэффициентов системы неравенств (ограничений) вида: -a_i1(-x_1) - ... -a_in(-x_n) + a_i <= 0 (i = 1, ..., m).
    Каждый массив - набор коэффициентов соответствующего неравенства.
    Функция возвращает порядковый номер столбца, в котором находится первый отрицательный коэффициент или False в случае
    отсутствия отрицательных коэффициентов в неравенстве (несовместность системы), или True в случае отсутствия
    отрицательных свободного члена и коэффициетов.'''
    free_coefficient = search_negative_free_coefficient(A)
    print('свободный коэф: ', free_coefficient)
    if free_coefficient is not None:
        row = A[free_coefficient]
        for c, el in enumerate(row):
            if el < 0 and c != len(row) - 1:
                print('отрицательный коэф: ', c)
                return c
        return False
    return True




def choose_solving_element(A: List[List]) -> Any:
    '''Функция определяет разрешающий элемент для модифицированного метода Жордановых исключений.
    A - матрица коэффициентов системы неравенств (ограничений) вида: -a_i1(-x_1) - ... -a_in(-x_n) + a_i <= 0 (i = 1, ..., m).
    Каждый массив - набор коэффициентов соответствующего неравенства.
    Функция возвращает массив: первый элемент - порядковый номер строки, второй элемент - порядковый номер столбца.
    В случае отсутствия отрицательных коэффициентов возвращает None.'''
    c = search_negative_coefficient(A)
    print('negative_coef: ', c)
    if c is True:
        return c
    elif c is False:
        return c
    else:
        ratio_dict = {}
        for r, row in enumerate(A):
            ratio = row[-1] / row[c]
            if ratio == 0 and row[c] > 0:
                return [r, c]
            elif ratio > 0:
                ratio_dict.update({r: ratio})
        return [get_key_by_value(ratio_dict, min(list(ratio_dict.values()))), c]


def simplex_method(A: List[List], free_terms: List, x: List[str], y: List[str]) -> Any:
    '''Функция осуществляет симплекс метод. Т.е производится поиск опроного решения системы неравенств.
    A - матрица коэффициентов системы неравенств (ограничений) вида: -a_i1(-x_1) - ... -a_in(-x_n) + a_i <= 0 (i = 1, ..., m).
    Каждый массив - набор коэффициентов соответствующего неравенства.
    free_terms - массив порядковых номеров свободных переменных.
    Функция возвращает опроное решение в виде массива или None в случае его отсутствия, т.е несовместности системы.'''
    for i in A:
        print(i)
    A_r = [[0 for _ in row] for row in A]
    if free_terms:
        pass
    else:
        solving_element = choose_solving_element(A)
        print('solving_element: ', solving_element)
        if solving_element is False:
            print('Система несовместна.')
        elif solving_element is True:
            solution = []
            for row in A:
                if row != A[-1]:
                    solution.append(row[-1])
            print(x, y, sep='\n')
            return solution
        else:
            r, c = solving_element
            x[c], y[r] = "-" + y[r], x[c][1:]
            for i, row in enumerate(A):
                for j, el in enumerate(row):
                    if i == r and j == c:
                        A_r[i][j] = 1 / A[r][c]
                    elif i != r and j == c:
                        A_r[i][j] = - A[i][c] / A[r][c]
                    elif i == r and j != c:
                        A_r[i][j] = A[r][j] / A[r][c]
                    else:
                        A_r[i][j] = (A[i][j] * A[r][c] - A[i][c] * A[r][j]) / A[r][c]
            return simplex_method(A_r, [], x, y)

A = format_matrix(A)
print(simplex_method(A, [], ['-x1', '-x2'], ['y1', 'y2', 'y3']))