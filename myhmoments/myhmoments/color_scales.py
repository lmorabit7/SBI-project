"""
This module creates two dictionaries containing color scales.

The function rgb_colors modifies 10 rgb color codes in order to be interpreted by UCSF Chimera.
The resulting dictionary contains a range of 10 colors between red (+ hydrophobic) and blue (+ hydrophilic).
"""

# Generate colors for chimera (rgb/255)
def rgb_colors():
    """
    Divides by 255 each rgb code of a dictionary with a range of 10 rgb colors from red to blue
    (or blue to red in reverse dictionary). Returns modified dictionary values, i.e. rgb codes
    that can be interpreted by USCF Chimera.
    """

    colors = {
    1:(0,0,255),
    2:(0,64,255),
    3:(51,153,255),
    4:(102,178,255),
    5:(204,229,255),
    6:(255,204,204),
    7:(255,153,153),
    8:(255,102,102),
    9:(255,51,51),
    10:(255,0,0)
    }

    colors_dict = {}
    for key, value in colors.items():
        new_value = tuple(list(map(lambda x: x/255, value)))
        colors_dict[key] = new_value

    colors_reverse_dict = {}
    i = 10
    for key in sorted(colors_dict.keys()):
        colors_reverse_dict[i]=colors_dict[key]
        i-=1


# Dictionaries

colors_dict = {1: (0.0, 0.0, 1.0), 2: (0.0, 0.25098039215686274, 1.0), 3: (0.2, 0.6, 1.0), 4: (0.4, 0.6980392156862745, 1.0), 5: (0.8, 0.8980392156862745, 1.0), 6: (1.0, 0.8, 0.8), 7: (1.0, 0.6, 0.6), 8: (1.0, 0.4, 0.4), 9: (1.0, 0.2, 0.2), 10: (1.0, 0.0, 0.0)}
colors_reverse_dict = {1: (1.0, 0.0, 0.0), 2: (1.0, 0.2, 0.2), 3: (1.0, 0.4, 0.4), 4: (1.0, 0.6, 0.6), 5: (1.0, 0.8, 0.8), 6: (0.8, 0.8980392156862745, 1.0), 7: (0.4, 0.6980392156862745, 1.0), 8: (0.2, 0.6, 1.0), 9: (0.0, 0.25098039215686274, 1.0), 10: (0.0, 0.0, 1.0)}
