"""
This module calculates the hydropathy moments of different regions in the surface.

The regions are defined as spheres of a given radius. The spheres are centered to each
CA of the surface residues. Using the distance function, the residues that are at a distance
=< of the radius are used to calculate the hydropathy moment of the region residues. Each
hydrophobicity index of the residues is associated to a color using the colors module.
The color resulting of the mean of all residues will be assigned to the hydropathy moment.
"""


try:
    import sys
    import math
    from myhmoments.hphob_scales import hphob_scales_dict
    from myhmoments.colors import get_color

except ImportError as e:
    raise Exception("Failed to import %s\n" %e)


def distance(atom1, atom2):
    """
    Computes the difference between two atom coordinates and returns the norm of
    the vector between two atom coordinates i.e. the Euclidean distance.
    """
    x_dist = (atom1[0] - atom2[0])**2
    y_dist = (atom1[1] - atom2[1])**2
    z_dist = (atom1[2] - atom2[2])**2
    return int(math.sqrt(x_dist + y_dist + z_dist))

def unit_vector(x,y,z):
    """
    Calculates the module of a vector and returns the unit vector.
    """
    module =  math.sqrt(x**2 + y**2 + z**2)
    if module != 0:
      return (x/module, y/module, z/module)
    else:
      return (x, y, z)

def get_average(container):
    """
    Returns the average of a list of values.
    """
    average = sum(container)/len(container)
    return average

def get_H_moments(my_dictionary, my_radius, my_h_scale):
    """
    Calculates the hidrophocity moment of each region using a given hydrophobicity
    scale, a given radius, and the dictonary containing the surface residues.
    """
    sys.stderr.write("Calculating hydropathy moments... ")
    my_h_dict = hphob_scales_dict[my_h_scale]
    max_H_constant = max(my_h_dict.values())
    min_H_constant = min(my_h_dict.values())

    count = 0
    region_moments = {}


    for aa1, ca1 in my_dictionary.items(): # get the center of the sphere
      Hx = Hy = Hz = 0
      H_list = []
      count +=1

      for aa2, ca2 in my_dictionary.items():
        dis = distance(ca1, ca2)
        if dis < my_radius: # get the vectors from CA1(sphere center) to CA2(CA of residues inside the sphere)
          x = ca2[0] - ca1[0]
          y = ca2[1] - ca1[1]
          z = ca2[2] - ca1[2]
          r_unit_vector = unit_vector(x, y ,z) # unit vector

          for key, value in my_h_dict.items():
              if aa2.startswith(key):
                  H_constant = value  # get the H_constant of every aa in the sphere
                  x = r_unit_vector[0] * value
                  y = r_unit_vector[1] * value
                  z = r_unit_vector[2] * value
          Hx += x
          Hy += y
          Hz += z
          H_list.append(H_constant) # append H_constant of every aa in the sphere to a list

      mean_H_constant = get_average(H_list)  # calculate the average H_constant of the sphere

      # Get color
      color = get_color(value=mean_H_constant, minimum=min_H_constant, maximum=max_H_constant, scale=my_h_scale)
      region_moments[ca1] = (Hx, Hy, Hz, color)


    sys.stderr.write("%s hydropathy moments calculated.\n" %count)
    return region_moments
