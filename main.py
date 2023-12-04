import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle

from Generation.generation import ellipse
from Non_overlapping_model.non_overlapping_model import transform, transform_ellipse, not_overlapping_border

w = 10
h = 10
# elps = generate_ellipse(2, w, h)
# draw_scene(elps, w, h)

elp1 = ellipse((1, -5), 4, 2, 30)
elp2 = ellipse((2, 1), 4, 2, 120)

c_r = transform(elp1)
trans_elp = transform_ellipse(elp1, elp2)
print(trans_elp)
f, (ax1, ax2) = plt.subplots(1, 2,)
ax1.set(xlim=(-10, 10), ylim=(-10, 10), aspect="equal")
ax2.set(xlim=(-10, 10), ylim=(-10, 10), aspect="equal")
elp_i = Ellipse(elp1.coord, elp1.a, elp1.b, angle=elp1.angle)
elp_j = Ellipse(elp2.coord, elp2.a, elp2.b, angle=elp2.angle)
rect = Rectangle((-5, -5), w, h, fill=False)

for elp in [elp1, elp2]:
    print(not_overlapping_border(elp, w, h))

ax1.add_artist(elp_i)
ax1.add_artist(elp_j)
ax1.add_artist(rect)

eps_ii = Circle(c_r, 1)
eps_ij = Ellipse(trans_elp.coord, trans_elp.a, trans_elp.b, angle=trans_elp.angle)

ax2.add_artist(eps_ii)
ax2.add_artist(eps_ij)
ax1.grid(color='gray', linestyle='--', linewidth=1)
ax2.grid(color='gray', linestyle='--', linewidth=1)
plt.show()
