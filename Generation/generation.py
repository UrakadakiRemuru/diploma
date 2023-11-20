from typing import List
import random


def generate_ellipse(n: int, w: float, h: float) -> List[List]:
    '''Возвращает массив эллипсов. Каждый эллипс представлен массивом его параметров: tuple(c_x, c_y) - координаты центра,
    a, b - главные оси эллипса, angle - угол поворота эллипса против часовой стрелки.
    :param n: Количество эллипсов.
    :param w: Ширина области.
    :param h: Высота области.'''
    rand_coords_x = [i for i in range(int(w / 2), int(w / 2) * 2)]
    rand_coords_y = [i for i in range(int(h / 2), int(h / 2) * 2)]
    rand_angels = [i for i in range(0, 181)]
    rand_sign = [-1, 1]
    elps = []
    marker = True
    for _ in range(n):
        while marker:
            a = w / 1.5 / random.choice(rand_coords_x)
            b = h / 1.5 / random.choice(rand_coords_y)
            if a != b:
                marker = False
        elps.append([(0 + random.choice(rand_sign) * w / 2 / random.choice(rand_coords_x),
                      0 + random.choice(rand_sign) * h / 2 / random.choice(rand_coords_y)),
                     a, b, random.choice(rand_sign) * random.choice(rand_angels)])
        marker = True
    return elps
