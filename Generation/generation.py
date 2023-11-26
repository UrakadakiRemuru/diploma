from typing import List, Dict
import random

import numpy as np


class ellipse:
    '''Представление эллипса.'''
    def __init__(self, coord: tuple, a: float, b: float, angle: float):
        '''
        :param coord: Координаты центра эллипса.
        :param a: Главная ось, умноженная на 2.
        :param b: Минорная ось, умноженная на 2.
        :param angle: Угол поворота эллипса против часовой стрелки относительно горизонтальной оси в градусах.
        '''
        self.coord = coord
        self.a = a
        self.b = b
        self.angle = angle


    def coord_to_array(self):
        '''Возвращает координаты центра в виде строки.'''
        return np.array(self.coord)


    def angle_to_rad(self):
        '''Возвращает угол поворота эллипса против часовой стрелки относительно горизонтальной оси в радианах.'''
        return self.angle * np.pi / 180


    def square(self):
        '''Возвращает площадь эллипса.'''
        return np.pi * self.a / 2 * self.b / 2


def generate_ellipse(n: int, w: float, h: float) -> List[ellipse]:
    '''Возвращает массив эллипсов.
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
        elps.append(ellipse((0 + random.choice(rand_sign) * w / 2 / random.choice(rand_coords_x),
                      0 + random.choice(rand_sign) * h / 2 / random.choice(rand_coords_y)),
                      a, b, random.choice(rand_sign) * random.choice(rand_angels)))
        marker = True
    return elps
