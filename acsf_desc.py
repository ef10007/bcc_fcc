from dscribe.descriptors import ACSF
from ase.build import molecule
import numpy as np
from ase import Atoms

# Setting up the ACSF descriptor
acsf = ACSF(
    species=["H", "O"],
    rcut=6.0,
    g2_params=[[1, 1], [1, 2], [1, 3]],
    g4_params=[[1, 1, 1], [1, 2, 1], [1, 1, -1], [1, 2, -1]],
)

# a = 4.081
# b = a / 2
# fcc_atom = Atoms('Au',
#                  cell=[(0, b, b),
#                        (b, 0, b), 
#                        (b, b, 0)],
#                  pbc=True)

# acsf = ACSF(fcc_atom) -> "Please provide the species as an iterable, e.g. a list."

water = molecule("H2O")
print(water)

# Create MBTR output for the hydrogen atom at index 1
acsf_water = acsf.create(water, positions=[1])

print(acsf_water)
print(acsf_water.shape)

acsf_water2 = acsf_water.reshape(-1, 1)
print(acsf_water2.shape)