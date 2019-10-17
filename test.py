from ase.build import surface
from ase.visualize import view
from ase.build import bulk
from ase import Atoms
from ase.io import write


'''
FCC unit cell:
atoms.set_cell([(0, b, b), (b, 0, b), (b, b, 0)])
'''

# a = 4.05  # Gold lattice constant
a = 4.081
b = a / 2

fcc_atom = Atoms('Au',
                 cell=[(0, b, b),
                       (b, 0, b), 
                       (b, b, 0)],
                 pbc=True)

# s2 = surface('Au', (2, 1, 1), 9)
# s2.center(vacuum=10, axis=2)
# write('string_Au2.vasp', s2, format='vasp', vasp5=True)

s1 = surface(fcc_atom, (2, 1, 1), 9)
s1.center(vacuum=10, axis=2)
print(s1)
write('atom_________.vasp', s1, format='vasp', vasp5=True)

# Mobulk = bulk('Mo', 'bcc', a=3.16, cubic=True)
# s2 = surface(Mobulk, (3, 2, 1), 9)
# s2.center(vacuum=10, axis=2)
# view(s2)


# a = 4.0
# Pt3Rh = Atoms('Pt3Rh',
#               scaled_positions=[(0, 0, 0),
#                                 (0.5, 0.5, 0),
#                                 (0.5, 0, 0.5),
#                                 (0, 0.5, 0.5)],
#               cell=[a, a, a],
#               pbc=True)
# s3 = surface(Pt3Rh, (2, 1, 1), 9)
# s3.center(vacuum=10, axis=2)
# view(s3)

# Pt3Rh.set_chemical_symbols('PtRhPt2')
# s4 = surface(Pt3Rh, (2, 1, 1), 9)
# s4.center(vacuum=10, axis=2)
# view(s4)