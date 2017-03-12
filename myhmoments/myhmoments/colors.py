"""
This module assigns a color to the different hydrophobicity index of each residue.

It uses the numpy and color_scales module to color each residue of a hydrophobicity
scale.
"""
try:
    from myhmoments.color_scales import *
    import numpy as n
except ImportError as e:
    raise Exception("Failed to import %s\n" %e)


def get_color(value,minimum,maximum,scale):
    """
    Given a hydrophobicity scale, it finds its maximum and minimum indexes and divides
    the scale in 10 groups of residues. Using the color_scale_dictionary, it assigns a
    color to each index (value) depending on which group has fallen in.

    """

    reverse_scales = set(["Guy", "Hopp_Woods", "Welling", "Bull_Breese"])

    list_of_ranges = n.linspace(minimum,maximum,num=10,endpoint=True)
    list_of_colors = []
    i=1
    if scale not in reverse_scales:
        for element in list_of_ranges:
            color = colors_dict[i]
            list_of_colors.append(color)
            i+=1
    else:
        for element in list_of_ranges:
            color = colors_reverse_dict[i]
            list_of_colors.append(color)
            i+=1

    j=-1
    for element in list_of_ranges:
        if value >= element:
            j+=1
    return list_of_colors[j]
