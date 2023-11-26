from typing import List, Dict

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import numpy as np
from Generation.generation import ellipse
def draw_scene(elps: List[ellipse], width: float, height: float):
    '''Рисует все сгенерированные эллипсы в заданной области.
    :param elps: Массив эллипсов.
    :param width: Ширина области.
    :param height: Высота области.'''
    color = [i for i in range(0, 256)]
    fig, ax = plt.subplots()
    ax.set(xlim=(-width / 2 - 1, width / 2 + 1), ylim=(-height / 2 - 1, height / 2 + 1), aspect="equal")
    for elp in elps:
        ellipse = Ellipse(elp.coord, elp.a, elp.b, angle=elp.angle, color=(np.random.random(), np.random.random(), np.random.random()))
        ax.add_artist(ellipse)
    rect = Rectangle((-width / 2, -height / 2), width, height, fill=False)
    ax.add_artist(rect)
    plt.show()
