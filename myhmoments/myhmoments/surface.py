"""
This module uses Biopython modules PDB.Parser and PDB.DSSP to process a given PDB file.

The get_surface_residues function returns a set containing the number of those residues in the surface
and the get_CA_coordinates function returns a dictonary with their alpha-carbon coordinates. This
dictionary will be used to center the region when calculating hydropathy moment.
"""

#if __name__=="__main__":

import sys

try:
    from Bio.PDB.PDBParser import PDBParser
    from Bio.PDB.DSSP import DSSP
except ImportError as e:
    raise Exception("Failed to import %s\n" %e)


def get_surface_residues(filename, my_acc_array, my_threshold):
    """
    Given a pdb file, finds the residues exposed to the solvent (not buried)
    according to the ASA (accessible surface area) value given by DSSP module.
    The user can select a threshold of ASA. Default is 0.2.
    """
    p = PDBParser(PERMISSIVE=1)
    s = p.get_structure("code.pdb", filename)
    model = s[0]
    d = DSSP(model, filename, dssp='mkdssp', acc_array=my_acc_array)

    sys.stderr.write("\nHandled %i residues\n" % len(d))

    residue_number = set()

    for element in sorted(d):
        if type(element[3]) is not str: #Sometimes the element[3] is NA
            if element[3] >= my_threshold:
                # foreach aa in the surface (according to threshold) store residue_number
                try:
                    residue_number.add(str(list(d.keys())[element[0]-1][1][1]) + list(d.keys())[element[0]-1][0])
                except IndexError:
                    sys.stderr.write("Element " +str(d.keys()[0]) +" index out of range\n")
    return residue_number


def get_CA_coordinates(filename, my_set):
    """
    Given a pdb file, it creates a dictionary with the CA (alpha-carbon) coordinates
    of those residues that are in the surface (set).
    """
    p = PDBParser(PERMISSIVE=1)
    s = p.get_structure("code.pdb", filename)
    model = s[0]

    CA_coordinates = {}

    sys.stderr.write("Calculating CA coordinates of residues...\n")
    for chain in model:
        for residue in chain:
            residue_name =str(residue.get_full_id()[3][1]) + residue.get_full_id()[2]
            if residue.get_id()[0] == " " and residue_name in my_set:
                residue_number = str(residue.get_resname())+str(residue.get_id()[1])
                for atom in residue:
                    if atom.get_name() == "CA":
                        # get CA coordinates, will be the values
                        CA = atom.get_coord()
                CA_coordinates[residue_number] = tuple(CA)
    return CA_coordinates
