import matplotlib.pyplot as plt
import numpy as np

Ay = 23.544
Fw1 = 23.544
Fw2 = Fw1

x_axis_points_short_beam = [0, 4.27, 4.275, 4.725, 4.73, 9]
y_axis_points_long_beam = [0, 6.79, 6.8, 8.19, 8.2, 15]


# z_axis_points_magn_bending_moment = [0, -100.53, -100.65, -100.65, -100.53, 0]

X, Y = np.meshgrid(x_axis_points_short_beam, y_axis_points_long_beam)


if (X.any() < 4.276):
    Z_short = -Ay * X
elif (X.any() > 4.276) and (X.any() < 4.725):
    Z_short = -Ay * X + Fw1*(X-4.275)
else:
    Z_short = -Ay * X + Fw1*(X-4.275) + Fw2*(X-4.725)


ax = plt.axes(projection="3d")
ax.plot_surface(X, Y, Z_short)
plt.show()
