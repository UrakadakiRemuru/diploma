import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

from Non_overlapping_model.non_overlapping_model import transform, transform_ellipse

# w = 10
# h = 10
# elps = generate_ellipse(2, w, h)
# draw_scene(elps, w, h)

elp1 = [(1, 1), 4, 1, -45]
elp2 = [(2, 1), 4, 1, 45]

c_r = transform(elp1)
trans_elp = transform_ellipse(elp1, elp2)

f, (ax1, ax2) = plt.subplots(1, 2,)
ax1.set(xlim=(-10, 10), ylim=(-10, 10), aspect="equal")
ax2.set(xlim=(-10, 10), ylim=(-10, 10), aspect="equal")
elp_i = Ellipse(elp1[0], elp1[1], elp1[2], angle=elp1[3])
elp_j = Ellipse(elp2[0], elp2[1], elp2[2], angle=elp2[3])

ax1.add_artist(elp_i)
ax1.add_artist(elp_j)

eps_ii = Circle(c_r, 1)
eps_ij = Ellipse(trans_elp[0], trans_elp[1], trans_elp[2], angle=trans_elp[3])

ax2.add_artist(eps_ii)
ax2.add_artist(eps_ij)
ax1.grid(color='gray', linestyle='--', linewidth=1)
ax2.grid(color='gray', linestyle='--', linewidth=1)
plt.show()
