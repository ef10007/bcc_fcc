from ase.build import fcc111, add_adsorbate
from ase.build import surface
from ase.visualize import view
from ase.build import bulk
from ase import Atoms


# slab = fcc111('Al', size=(2,2,3), vacuum=10.0)
# add_adsorbate(slab, 'H', 1.5, 'ontop')
# slab.center(vacuum=10.0, axis=2)
# print(slab.get_tags())


# s1 = surface('Au', (2, 1, 1), 9)
# s1.center(vacuum=10, axis=2)
# view(s1)

# Mobulk = bulk('Mo', 'bcc', a=3.16, cubic=True)
# s2 = surface(Mobulk, (3, 2, 1), 9)
# s2.center(vacuum=10, axis=2)
# view(s2)


a = 4.0
Pt3Rh = Atoms('Pt3Rh',
              scaled_positions=[(0, 0, 0),
                                (0.5, 0.5, 0),
                                (0.5, 0, 0.5),
                                (0, 0.5, 0.5)],
              cell=[a, a, a],
              pbc=True)
s3 = surface(Pt3Rh, (2, 1, 1), 9)
s3.center(vacuum=10, axis=2)
view(s3)

Pt3Rh.set_chemical_symbols('PtRhPt2')
s4 = surface(Pt3Rh, (2, 1, 1), 9)
s4.center(vacuum=10, axis=2)
view(s4)