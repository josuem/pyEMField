import numpy as np
import matplotlib.pyplot as plt

class Field2D:
    def __init__(self, nx=64, ny=64, xlim=[-2, 2], ylim=[-2, 2]):
        self.xlim, self.ylim = xlim, ylim
        self.nx, self.ny = nx, ny
        
    def create_mesh(self):
        # Grid of x, y points
        self.x = np.linspace(self.xlim[0], self.xlim[1], self.nx)
        self.y = np.linspace(self.ylim[0], self.ylim[1], self.ny)
        
        self.X, self.Y = np.meshgrid(self.x, self.y)

        # Electric field vector, E=(Ex, Ey), as separate components
        self.Fx, self.Fy = np.zeros((self.ny, self.nx)), np.zeros((self.ny, self.nx))

    def calculate_field(self, vector_field):
        self.create_mesh()

        for i in range(self.nx):
            for j in range(self.ny):
                field_xtmp, field_ytmp = vector_field(x=self.X[j, i], y=self.Y[j, i])
                self.Fx[j, i] += field_xtmp
                self.Fy[j, i] += field_ytmp


    def plot(self, **kwargs):
        ax = kwargs.get('ax', plt.plot())
        arrowsize = kwargs.get('arrowsize', 1.0)
        density = kwargs.get('density', 1.5)

        # Plot the streamlines with an appropriate colormap and arrow style
        color = 2 * np.log(np.hypot(self.Fx, self.Fy))
        ax.streamplot(self.x, self.y, self.Fx, self.Fy, color=color, linewidth=1, cmap=plt.cm.inferno,
                    density=density, arrowstyle='->', arrowsize=arrowsize)

        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.set_aspect('equal')
