import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import numpy as np

def draw_scene(elps: list, width: float, height: float):
    color = [i for i in range(0, 256)]
    fig, ax = plt.subplots()
    ax.set(xlim=(-width / 2 - 1, width / 2 + 1), ylim=(-height / 2 - 1, height / 2 + 1), aspect="equal")
    for elp in elps:
        c, w, h, alpha = elp
        ellipse = Ellipse(c, w, h, angle=-alpha, color=(np.random.random(), np.random.random(), np.random.random()))
        ax.add_artist(ellipse)
    rect = Rectangle((-width / 2, -height / 2), width, height, fill=False)
    ax.add_artist(rect)
    plt.show()
