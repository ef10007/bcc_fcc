from ase.build import surface
from ase.visualize import view
from ase.build import bulk
from ase import Atoms
from ase.io import write
import db_conn
from pprint import pprint

# lattice constant (BCC)
bcc = {'Li' : 3.428, 'Na' : 4.164, 'K' : 5.207, 'Rb' : 5.561, 
       'Cs' : 6.004, 'Ba' : 4.898, 'V' : 2.959, 'Nb' : 3.269,
       'Ta' : 3.283, 'Cr' : 2.805, 'Mo' : 3.132, 'W' : 3.161, 
       'Fe' : 2.775 }

# lattice constant (FCC)
fcc = {'Ca' : 5.457, 'Sr' : 5.916, 'Rh' : 3.779, 'Ir' : 3.834, 
       'Ni' : 3.452, 'Pd' : 3.878, 'Pt' : 3.917, 'Cu' : 3.551,
       'Ag' : 4.047, 'Au' : 4.081, 'Al' : 4.018}

def make_surface(limit_num=10):
    data = db_conn.get_data(limit_num)
    print('outside')
    atom = ''
    lattice_constant = 0
    miller_indices = 0

    for d in data:
    
        atom = str(d[0])
        lattice_constant = fcc[atom]
        b = lattice_constant / 2
        miller_indices = d[1]

        if miller_indices == (0, 0, 0):
            continue

        fcc_atom = Atoms(atom,
                    cell=[(0, b, b),
                          (b, 0, b), 
                          (b, b, 0)],
                    pbc=True)
        # yield fcc_atom, miller_indices

        s = surface(fcc_atom, miller_indices, 9)
        pprint(s)
        s.center(vacuum=10, axis=2)

        write('{}_{}.vasp'.format(atom, miller_indices), s, format='vasp', vasp5=True)
        print('Writing VASP files has been done!', '{}_{}.vasp'.format(atom, miller_indices))

        s = None

# def to_surface(atomobj, miller_indices):
#     s =surface(fcc_atom, (miller_indices, 9)
#     s.center(vacuum=10, axis=2)

#     write('{}_{}.vasp'.format(atom, miller_indices), s, format='vasp', vasp5=True)
#     print('Writing VASP files has been done!')


make_surface()