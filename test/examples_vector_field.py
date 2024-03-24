# %% 
import matplotlib.pyplot as plt
import scienceplots

from pyEMField import Field2D

# %% Uniform vector field
def field_test(**kwargs):
    return [1, 0]

field = Field2D(xlim=[-1, 1], ylim=[-1, 1])
field.calculate_field(field_test)

fig, ax =  plt.subplots(1)
field.plot(ax=ax, density=1, arrowsize=1)
ax.set(title="v(x, y) = (1, 0)")
plt.show()

# %% Example non-conservative vector field 
# v(x, y) = (-y, x)

def field_test(**kwargs):
    for key, value in kwargs.items():
        if key == 'x':
            x = value
        if key == 'y':
            y = value
    return [-y, x]


field = Field2D(xlim=[-1, 1], ylim=[-1, 1])
field.calculate_field(field_test)

fig, ax =  plt.subplots(1)
field.plot(ax=ax, density=1, arrowsize=1)
ax.set(title="v(x, y) = (-y, x)")
plt.show()

# %% source vector field
def field_test(x, y):
    return [x, y] / ((x)**2 + (y)**2)**(3/2)

field = Field2D(nx=100, ny=100, xlim=[-1, 1], ylim=[-1, 1])
field.calculate_field(field_test)

fig, ax =  plt.subplots(1)
field.plot(ax=ax, density=1, arrowsize=1)
ax.set(title="$v(x, y) = (x, y) / ((x)^2 + (y)^2)^{3/2}$")
plt.show()

# %% 