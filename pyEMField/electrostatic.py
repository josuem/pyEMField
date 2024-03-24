"""
Module for plotting electric field.

.. codeauthor:: Josué Meneses Díaz <josue.meneses@usach.cl>

sources: https://scipython.com/blog/visualizing-a-vector-field-with-matplotlib/
"""

# %%  Plot electric field
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from .constants import KE

class Particle:
    def __init__(self, charge, position):
        self.charge = charge
        self.position = np.array(position)

class Vector:
    def __init__(self, module_r, r, vector):
        self.module_r = module_r
        self.r = np.array(r)
        self.vector = np.array(vector)


class F_net:
    def __init__(self, vec_net, forces, r_ab, mag_r_ab):
        self.vec_net = np.array(vec_net)	
        self.forces = [np.array(force) for force in forces]
        self.r_ab = [np.array(r) for r in r_ab]
        self.mag_r_ab = np.array(mag_r_ab)


def force_ab(qa, qb):
    """Calculates the force between two particles due to the Coulomb's law.

    Args:
        qa (Particle): Particle with charge to apply force over qb.
        qb (Particle): Particle in analysis.

    Returns:
        Vector: Vector containing the module of the distance, the
            vector between the particles and the force applied.
    """
    # Calculates the vector between the particles
    r_ab = qb.position - qa.position

    # Calculates the module of the vector
    mag_r_ab = np.linalg.norm(r_ab)

    # Calculates the force between the particles
    F = Ke * qa.charge * qb.charge * r_ab / mag_r_ab**3

    # Returns a Vector object with the force information
    return Vector(mag_r_ab, r_ab, F)


def force_net(qa, vector_charges):
    r_ab = []
    mag_r_ab = []
    F = []

    for vector in vector_charges:
        tmp = force_ab(vector, qa)

        F.append(tmp.vector)
        r_ab.append(tmp.r)
        mag_r_ab.append(tmp.module_r)

    summary_force = F_net(np.sum(F, axis=0), F, r_ab, mag_r_ab)
    
    return summary_force


def report_forces(F, forces_string, num_decimals=8):  # Añadido num_decimals como argumento opcional
    for i, label in enumerate(forces_string, start=0):
        if i != 0:
            # Ajustar el número de decimales en los prints utilizando la sintaxis de formato de cadena
            print(f"r_{forces_string[i]}{forces_string[0]} = [{F.r_ab[i-1][0]:.{num_decimals}f}, {F.r_ab[i-1][1]:.{num_decimals}f}][m]")
            print(f"|r_{forces_string[i]}{forces_string[0]}| = {F.mag_r_ab[i-1]:.{num_decimals}f}[m]")
            print(f"f_{forces_string[i]}{forces_string[0]}   = [{F.forces[i-1][0]:.{num_decimals}e}, {F.forces[i-1][1]:.{num_decimals}e}][N]")

    
    # Print net force
    print(f"f{forces_string[0]}=[{F.vec_net[0]:.{num_decimals}e}, {F.vec_net[1]:.{num_decimals}e}][N]")


# %% 

def electric_field(qa, x, y):
    r = [x, y] - qa.position
    mag_r_ab = np.linalg.norm(r)
    F = KE * qa.charge * r / mag_r_ab**3

    return Vector(mag_r_ab, r, F)


class E_field:
    def __init__(self, vector_charges, xlim=[-2, 2], ylim=[-2, 2], nx=64, ny=64):
        self.vector_charges = vector_charges
        self.xlim, self.ylim = xlim, ylim
        self.nx, self.ny = nx, ny
        
    def create_mesh(self):
        # Grid of x, y points
        self.x = np.linspace(self.xlim[0], self.xlim[1], self.nx)
        self.y = np.linspace(self.ylim[0], self.ylim[1], self.ny)
        
        self.X, self.Y = np.meshgrid(self.x, self.y)

        # Electric field vector, E=(Ex, Ey), as separate components
        self.Ex, self.Ey = np.zeros((self.ny, self.nx)), np.zeros((self.ny, self.nx))


    def calculate_E(self):
        self.create_mesh()

        for charge in self.vector_charges:
            for i in range(self.nx):
                for j in range(self.ny):
                    Ex_tmp, Ey_tmp = electric_field(charge, x=self.X[j, i], y=self.Y[j, i]).vector
                    self.Ex[j, i] += Ex_tmp
                    self.Ey[j, i] += Ey_tmp

    def plot(self, ax=plt.plot):
        # Plot the streamlines with an appropriate colormap and arrow style
        color = 2 * np.log(np.hypot(self.Ex, self.Ey))
        ax.streamplot(self.x, self.y, self.Ex, self.Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
                    density=1.5, arrowstyle='->', arrowsize=1.0)

        # Add filled circles for the charges themselves
        charge_colors = {True: '#aa0000', False: '#0000aa'}

        for charge in self.vector_charges:
            ax.add_artist(Circle(charge.position, 0.05, color=charge_colors[charge.charge>0]))

        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        # ax.set_xlim(-2,2)
        # ax.set_ylim(-2,2)
        ax.set_aspect('equal')




# %% 

