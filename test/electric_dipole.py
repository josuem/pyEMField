# %% 
import matplotlib.pyplot as plt
import scienceplots

from pyEMField import E_field, Particle
from pyEMField import QE, QP

plt.style.use(["science", "notebook"])

# %% Electric dipole
distance_1 = 0.5  # m
distance_2 = 0.01  # m

fig, ax = plt.subplots(1, 2)

qe = Particle(charge=QE, position=[-distance_1, 0.0])
qp = Particle(charge=QP, position=[distance_1, 0.0])

vector_charges = [qe, qp]

field = E_field(vector_charges, nx=64, ny=64)
field.calculate_E()
field.plot(ax=ax[0])
ax[0].set(title="Distance 0.5m")

qe = Particle(charge=QE, position=[-distance_2, 0.0])
qp = Particle(charge=QP, position=[distance_2, 0.0])

vector_charges = [qe, qp]

field2 = E_field(vector_charges, nx=64, ny=64)
field2.calculate_E()
field2.plot(ax=ax[1])
ax[1].set(title="Distance 0.01m", ylabel="")

plt.show()

fig.savefig("electric_dipole.png", dpi=300)
# %% 