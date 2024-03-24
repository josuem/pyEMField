# %% 
import matplotlib.pyplot as plt
import scienceplots

from pyEMField import QE, QP
from pyEMField import Particle, E_field,Field2D

fig, ax = plt.subplots(1, 2)

qe = Particle(charge=QE, position=[0.0, 0.0])
qp = Particle(charge=QP, position=[0.0, 0.0])

vector_charges = [qe]

field = E_field(vector_charges, nx=64, ny=64)
field.calculate_E()
field.plot(ax=ax[0])
ax[0].set(title="Vector field electron")


vector_charges = [qp]

field2 = E_field(vector_charges, nx=64, ny=64)
field2.calculate_E()
field2.plot(ax=ax[1])
ax[1].set(title="Vector field proton", ylabel="")

plt.show()

# %% 