"""
This module contains a dictionary with 17 dictionaries corresponding to the different
hydrophobicity scales according to http://web.expasy.org/protscale/.

Some scales do not assign to the most hydrophobic aminoacids the most positive value. These
scales will be assigned a reverse color scale in the color_scales module.

"""
# Amino acid scale: Optimized matching hydrophobicity (OMH).
# # Author(s): Sweet R.M., Eisenberg D.
# # Reference: J. Mol. Biol. 171:479-488(1983).

hphob_scales_dict = {
"OMH_Sweet": {
"ALA": -0.400, "ARG": -0.590, "ASN": -0.920, "ASP": -1.310, "CYS":  0.170,
"GLN": -0.910, "GLU": -1.220, "GLY": -0.670, "HIS": -0.640, "ILE":  1.250,
"LEU":  1.220, "LYS": -0.670, "MET":  1.020, "PHE":  1.920, "PRO": -0.490,
"SER": -0.550, "THR": -0.280, "TRP":  0.500, "TYR":  1.670, "VAL":  0.910
},

# Amino acid scale: Hydropathicity.
# # Author(s): Kyte J., Doolittle R.F.
# # Reference: J. Mol. Biol. 157:105-132(1982).

"Kyte_Doolitle" : {
"ALA":  1.800, "ARG": -4.500, "ASN": -3.500, "ASP": -3.500, "CYS":  2.500,
"GLN": -3.500, "GLU": -3.500, "GLY": -0.400, "HIS": -3.200, "ILE":  4.500,
"LEU":  3.800, "LYS": -3.900, "MET":  1.900, "PHE":  2.800, "PRO": -1.600,
"SER": -0.800, "THR": -0.700, "TRP": -0.900, "TYR": -1.300, "VAL":  4.200
},

# Amino acid scale: Hydrophobicity (delta G1/2 cal)
# # Author(s): Abraham D.J., Leo A.J.
# # Reference: Proteins: Structure, Function and Genetics 2:130-152(1987).

"Abraham_Leo" : {
"ALA":  0.440, "ARG": -2.420, "ASN": -1.320, "ASP": -0.310, "CYS":  0.580,
"GLN": -0.710, "GLU": -0.340, "GLY":  0.000, "HIS": -0.010, "ILE":  2.460,
"LEU":  2.460, "LYS": -2.450, "MET":  1.100, "PHE":  2.540, "PRO":  1.290,
"SER": -0.840, "THR": -0.410, "TRP":  2.560, "TYR":  1.630, "VAL":  1.730
},

# Amino acid scale: Hydrophobicity (free energy of transfer to surface in kcal/mole).
# # Author(s): Bull H.B., Breese K.
# # Reference: Arch. Biochem. Biophys. 161:665-670(1974).

"Bull_Breese" : {
"ALA":  0.610, "ARG":  0.690, "ASN":  0.890, "ASP":  0.610, "CYS":  0.360,
"GLN":  0.970, "GLU":  0.510, "GLY":  0.810, "HIS":  0.690, "ILE": -1.450,
"LEU": -1.650, "LYS":  0.460, "MET": -0.660, "PHE": -1.520, "PRO": -0.170,
"SER":  0.420, "THR":  0.290, "TRP": -1.200, "TYR": -1.430, "VAL": -0.750
},


# Amino acid scale: Hydrophobicity scale based on free energy of transfer (kcal/mole).
# # Author(s): Guy H.R.
# # Reference: Biophys J. 47:61-70(1985).
"Guy" : {
"ALA":  0.100, "ARG":  1.910, "ASN":  0.480, "ASP":  0.780, "CYS": -1.420,
"GLN":  0.950, "GLU":  0.830, "GLY":  0.330, "HIS": -0.500, "ILE": -1.130,
"LEU": -1.180, "LYS":  1.400, "MET": -1.590, "PHE": -2.120, "PRO":  0.730,
"SER":  0.520, "THR":  0.070, "TRP": -0.510, "TYR": -0.210, "VAL": -1.270
},

# Amino acid scale: Hydrophobicity scale (contact energy derived from 3D data).
# # Author(s): Miyazawa S., Jernigen R.L.
# # Reference: Macromolecules 18:534-552(1985).
"Miyazawa" : {
"ALA":  5.330, "ARG":  4.180, "ASN":  3.710, "ASP":  3.590, "CYS":  7.930,
"GLN":  3.870, "GLU":  3.650, "GLY":  4.480, "HIS":  5.100, "ILE":  8.830,
"LEU":  8.470, "LYS":  2.950, "MET":  8.950, "PHE":  9.030, "PRO":  3.870,
"SER":  4.090, "THR":  4.490, "TRP":  7.660, "TYR":  5.890, "VAL":  7.630
},

# Amino acid scale: Hydrophobicity scale (pi-r).
# # Author(s): Roseman M.A.
# # Reference: J. Mol. Biol. 200:513-522(1988).
"Roseman" : {
"ALA":  0.390, "ARG": -3.950, "ASN": -1.910, "ASP": -3.810, "CYS":  0.250,
"GLN": -1.300, "GLU": -2.910, "GLY":  0.000, "HIS": -0.640, "ILE":  1.820,
"LEU":  1.820, "LYS": -2.770, "MET":  0.960, "PHE":  2.270, "PRO":  0.990,
"SER": -1.240, "THR": -1.000, "TRP":  2.130, "TYR":  1.470, "VAL":  1.300
},

# Amino acid scale: Hydration potential (kcal/mole) at 25øC.
# # Author(s): Wolfenden R.V., Andersson L., Cullis P.M., Southgate C.C.F.
# # Reference: Biochemistry 20:849-855(1981).
"Wolfenden" : {
"ALA":  1.940, "ARG": -19.920, "ASN": -9.680, "ASP": -10.950, "CYS": -1.240,
"GLN": -9.380, "GLU": -10.200, "GLY":  2.390, "HIS": -10.270, "ILE":  2.150,
"LEU":  2.280, "LYS": -9.520, "MET": -1.480, "PHE": -0.760, "PRO":  0.000,
"SER": -5.060, "THR": -4.880, "TRP": -5.880, "TYR": -6.110, "VAL":  1.990
},

# Amino acid scale: Normalized consensus hydrophobicity scale.
# # Author(s): Eisenberg D., Schwarz E., Komarony M., Wall R.
# # Reference: J. Mol. Biol. 179:125-142(1984).
"Eisenberg" : {
"ALA":  0.620, "ARG": -2.530, "ASN": -0.780, "ASP": -0.900, "CYS":  0.290,
"GLN": -0.850, "GLU": -0.740, "GLY":  0.480, "HIS": -0.400, "ILE":  1.380,
"LEU":  1.060, "LYS": -1.500, "MET":  0.640, "PHE":  1.190, "PRO":  0.120,
"SER": -0.180, "THR": -0.050, "TRP":  0.810, "TYR":  0.260, "VAL":  1.080
 },

# Amino acid scale: Hydrophilicity.
# # Author(s): Hopp T.P., Woods K.R.
# # Reference: Proc. Natl. Acad. Sci. U.S.A. 78:3824-3828(1981).

"Hopp_Woods" : {
"ALA": -0.500, "ARG":  3.000, "ASN":  0.200, "ASP":  3.000, "CYS": -1.000,
"GLN":  0.200, "GLU":  3.000, "GLY":  0.000, "HIS": -0.500, "ILE": -1.800,
"LEU": -1.800, "LYS":  3.000, "MET": -1.300, "PHE": -2.500, "PRO":  0.000,
"SER":  0.300, "THR": -0.400, "TRP": -3.400, "TYR": -2.300, "VAL": -1.500
},

# Amino acid scale: Average surrounding hydrophobicity.
# Author(s): Manavalan P., Ponnuswamy P.K.
# Reference: Nature 275:673-674(1978).
"Manavalan" : {
"ALA": 12.970, "ARG": 11.720, "ASN": 11.420, "ASP": 10.850, "CYS": 14.630,
"GLN": 11.760, "GLU": 11.890, "GLY": 12.430, "HIS": 12.160, "ILE": 15.670,
"LEU": 14.900, "LYS": 11.360, "MET": 14.390, "PHE": 14.000, "PRO": 11.370,
"SER": 11.230, "THR": 11.690, "TRP": 13.930, "TYR": 13.420, "VAL": 15.710
},

# Amino acid scale: Hydrophobicity of physiological L-alpha amino acids
# # Author(s): Black S.D., Mould D.R.
# Reference: Anal. Biochem. 193:72-82(1991).
"Black": {
"ALA":  0.616, "ARG":  0.000, "ASN":  0.236, "ASP":  0.028, "CYS":  0.680,
"GLN":  0.251, "GLU":  0.043, "GLY":  0.501, "HIS":  0.165, "ILE":  0.943,
"LEU":  0.943, "LYS":  0.283, "MET":  0.738, "PHE":  1.000, "PRO":  0.711,
"SER":  0.359, "THR":  0.450, "TRP":  0.878, "TYR":  0.880, "VAL":  0.825
},

# Amino acid scale: Hydrophobicity scale (pi-r).
# Author(s): Fauchere J.-L., Pliska V.E.
# Reference: Eur. J. Med. Chem. 18:369-375(1983).
"Fauchere" : {
"ALA":  0.310, "ARG": -1.010, "ASN": -0.600, "ASP": -0.770, "CYS":  1.540,
"GLN": -0.220, "GLU": -0.640, "GLY":  0.000, "HIS":  0.130, "ILE":  1.800,
"LEU":  1.700, "LYS": -0.990, "MET":  1.230, "PHE":  1.790, "PRO":  0.720,
"SER": -0.040, "THR":  0.260, "TRP":  2.250, "TYR":  0.960, "VAL":  1.220
},

# Amino acid scale: Free energy of transfer from inside to outside of a globular PROtein.
# Author(s): Janin J.
# # Reference: Nature 277:491-492(1979).
"Janin" : {
"ALA":  0.300, "ARG": -1.400, "ASN": -0.500, "ASP": -0.600, "CYS":  0.900,
"GLN": -0.700, "GLU": -0.700, "GLY":  0.300, "HIS": -0.100, "ILE":  0.700,
"LEU":  0.500, "LYS": -1.800, "MET":  0.400, "PHE":  0.500, "PRO": -0.300,
"SER": -0.100, "THR": -0.200, "TRP":  0.300, "TYR": -0.400, "VAL":  0.600
},

# Amino acid scale: Membrane buried helix paraMETer.
# Author(s): Rao M.J.K., Argos P.
# Reference: Biochim. Biophys. Acta 869:197-214(1986).
"Rao_Argos" : {
"ALA":  1.360, "ARG":  0.150, "ASN":  0.330, "ASP":  0.110, "CYS":  1.270,
"GLN":  0.330, "GLU":  0.250, "GLY":  1.090, "HIS":  0.680, "ILE":  1.440,
"LEU":  1.470, "LYS":  0.090, "MET":  1.420, "PHE":  1.570, "PRO":  0.540,
"SER":  0.970, "THR":  1.080, "TRP":  1.000, "TYR":  0.830, "VAL":  1.370
},

# Amino acid scale: Hydrophobicity scale (Contribution of hydrophobic interactions to the stability of the globular conformation of PROteins).
# Author(s): Tanford C.
# Reference: J. Am. Chem. Soc. 84:4240-4274(1962).
"Tanford" : {
"ALA":  0.620, "ARG": -2.530, "ASN": -0.780, "ASP": -0.090, "CYS":  0.290,
"GLN": -0.850, "GLU": -0.740, "GLY":  0.480, "HIS": -0.400, "ILE":  1.380,
"LEU":  1.530, "LYS": -1.500, "MET":  0.640, "PHE":  1.190, "PRO":  0.120,
"SER": -0.180, "THR": -0.050, "TRP":  0.810, "TYR":  0.260, "VAL":  1.800
},

# Amino acid scale: Antigenicity value X 10.
# Author(s): Welling G.W., Weijer W.J., Van der Zee R., Welling-Wester S.
# Reference: FEBS Lett. 188:215-218(1985).
"Welling" : {
"ALA":  1.150, "ARG":  0.580, "ASN": -0.770, "ASP":  0.650, "CYS": -1.200,
"GLN": -0.110, "GLU": -0.710, "GLY": -1.840, "HIS":  3.120, "ILE": -2.920,
"LEU":  0.750, "LYS":  2.060, "MET": -3.850, "PHE": -1.410, "PRO": -0.530,
"SER": -0.260, "THR": -0.450, "TRP": -1.140, "TYR":  0.130, "VAL": -0.130
}}
