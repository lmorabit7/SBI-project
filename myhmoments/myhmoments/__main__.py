"""
This module is the main module of myhmoments package. It computes the hydropathy
moments of a given pdb file.

Given a pdb file (required to run the program), the program computes the hydropathy moments
of x regions in the protein surface. The results can be visualized in USCF-Chimera.
First, it parses the input arguments given by the user:

- a pdb file (required),
- a outputfile name,
- a threshold to trim surface residues,
- a solvent accesibility array,
- a radius of the sphere that will define the region,
- and a hydrophobicity scale.

The program wirtes 3 different files: the tab file containing the hydropathy moments,
a bild fild with vector objects corresponding to the hydropathy moments of the x
regions and file containing a macro for USCF-Chimera in order to better visualize
the pdb file with the vector objects on it.

The program executes 3 main functions imported from other modules in the package.
First, the surface residues are fetched using the function get_surface_residues with a
given input threshold. Then the carbon-alpha coordinates are stored with the function
get_CA_coordinates and finally, the hydropathy moments are calculated with get_H_moments.

The program can start a subprocess that will execute the macro file in order to visualize
the results in USCF-Chimera. Once the path to the USCF-Chimera is provided in the commandline,
the macro file opens the results.cmd file in USCF-Chimera together with the .bild file that
wiill display the hydropathy moments vectors colored according to a 10-color scale for hydropathy.
"""

if __name__=="__main__":
    try:
        import sys
        import os
        import argparse
        import re
        import subprocess
        import myhmoments.exceptions as e
        import myhmoments.surface as s
        import myhmoments.moments as mo

    except ImportError as e:
        raise Exception("Failed to import %s\n" %e)

##########################################################################
###################### S B I ## P R O J E C T ############################
##########################################################################
################ H Y D R O P A T H Y ## M O M E N T ####################
##########################################################################
############### O F ## S U R F A C E ## R E G I O N S ####################
##########################################################################

##########################################################################
################# P A R S E ## I N P U T ##  A R G S #####################
##########################################################################
    parser = argparse.ArgumentParser(description="""Given a pdb file(s), calculate
    the hydropathy moments of surface regions""")

    parser.add_argument('-i', '--input',
                        dest = "infile",
                        action = "store",
                        default = None,
                        required = True,  # Input is mandatory
                        help = "Input pdb file")

    parser.add_argument('-o', '--output',
                        dest = "outfile",
                        action = "store",
                        default = "results",
                        help = "Output files prefix. Extensions are given by the script")

    parser.add_argument('-acc', '--acc_array',
                        dest = "acc_array",
                        action = "store",
                        default ="Sander",
                        choices = ["Sander", "Miller", "Wilke"],
                        help ="""Specify solvent accessibility (ACC) values for DSSP relative
                        accessible surface area (RSA) calculations.\n
                        Default: Sander.\n
                        Usage example: -acc Miller""")

    parser.add_argument('-t', '--threshold',
                        dest = "threshold",
                        action = "store",
                        default = 0.2,
                        type = float,
                        help = """Threshold value (float) for relative accessible surface area (RSA) to
                        set surface residues. Takes values between 0.0 and 1.0. \n
                        Default: 0.2 (Residues with RSA >= 0.2 are considered surface residues)""")


    parser.add_argument('-r', '--radius',
                        dest = "radius",
                        action = "store",
                        default = 6.0,
                        type = float,
                        help = """Radius of the sphere (float) from the center CA where it set. CA of
                        other residues placed inside the sphere will be used to calculate the
                        hydropathy moment of the sphere.\n
                        Default: 6.0""")

    parser.add_argument('-hy', '--hyphob_scale',
                        dest = "hphob_scale",
                        action = "store",
                        default = "Kyte_Doolitle",
                        choices = ["OMH_Sweet", "Kyte_Doolitle", "Abraham_Leo", "Bull_Breese", "Guy", "Miyazawa", "Roseman", "Wolfenden", "Eisenberg", "Hopp_Woods", "Manavalan", "Black", "Fauchere", "Janin", "Rao_Argos", "Tanford", "Welling"],
                        help = """Hydrophobicity scale used for hydropathy moments calculations.\n
                        Default: Eisenberg scale. """)

    sys.stderr.write("""CALCULATION OF HYDROPATHY MOMENTS IN LOCAL REGIONS
    ------------------------------------------------------\n""")
    args = parser.parse_args()
    if args.infile.endswith(".pdb"):                       # If file is not .pdb, raise exception
        sys.stderr.write("Input file:\t\t%s\n" %args.infile)
    else:
        raise e.FileExtensionError(args.infile)

    outfile_prefix = re.sub('\.', '_', str(args.outfile))  # Replace any extension added by the user with _
    outfile_file = outfile_prefix+".tab"                   # Output file .tab
    outfile_moments_file = outfile_prefix+".bild"          # Output file .bild with hydropathy moments (Chimera)
    outfile_macro_file = outfile_prefix+".cmd"             # Output file .cmd with file.pdb and hydropathy moments (Chimera)

    sys.stderr.write("Output files prefix:\t%s\n" %args.outfile)
    sys.stderr.write("ACC array:\t\t%s\n" %args.acc_array)
    if args.threshold<0.2 or args.threshold>0.8:           # If threshold not correct, raise exception
        raise e.ThresholdError(args.threshold)
    else:
        sys.stderr.write("RSA threshold:\t\t%s\n" %args.threshold)
    if args.radius<4.0 or args.radius>10.0:                # If radius not correct, raise exception
        raise e.RadiusError(args.radius)
    else:
        sys.stderr.write("Sphere radius:\t\t%s\n" %args.radius)
    sys.stderr.write("Hydrophobicity scale:\t%s\n" %args.hphob_scale)

    #####################################################################
    ####                       RUN FUNCTIONS                        #####
    #####################################################################

    surface_residues_number = s.get_surface_residues(filename=args.infile,
                                                     my_acc_array=args.acc_array,
                                                     my_threshold=args.threshold)
    CA_dictionary = s.get_CA_coordinates(filename=args.infile,
                                         my_set=surface_residues_number)
    moments = mo.get_H_moments(my_dictionary=CA_dictionary,
                               my_radius=args.radius,
                               my_h_scale=args.hphob_scale)

    #####################################################################
    ####                       PRINT RESULTS                        #####
    #####################################################################

    sys.stderr.write("Printing results...\n")

    sys.stdout.write("H moment\t%s\t%s\t%s\t%s\t%s\t%s\n" %("Origin(x)","Origin(y)","Origin(z)", "Vector(x)", "Vector(y)","Vector(z)"))
    count = 1
    for key, value in moments.items():
        sys.stdout.write("%8s\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\n" %(count,key[0],key[1],key[2],value[0],value[1],value[2]))
        count+=1

    with open(outfile_file, "w") as outfd:
        outfd.write("Input file:\t%s\n" %args.infile)
        outfd.write("Output file:\t%s\n" %args.outfile)
        outfd.write("ACC array:\t%s\n" %args.acc_array)
        outfd.write("RSA threshold:\t%s\n" %args.threshold)
        outfd.write("Sphere radius:\t%s\n" %args.radius)
        outfd.write("Hydrophobicity scale:\t%s\n\n" %args.hphob_scale)
        outfd.write("H moment\t%s\t%s\t%s\t%s\t%s\t%s\n" %("Origin(x)","Origin(y)","Origin(z)", "Vector(x)", "Vector(y)","Vector(z)"))
        count = 1
        for key, value in moments.items():
            outfd.write("%8s\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\n" %(count,key[0],key[1],key[2],value[0],value[1],value[2]))
            count+=1

    with open(outfile_moments_file, "w") as outfd_moments:
        for key, value in moments.items():
            if value[0]!= 0 and value[1]!= 0 and value[2]!= 0:
                new_value_x = key[0] + value[0]
                new_value_y = key[1] + value[1]
                new_value_z = key[2] + value[2]
                outfd_moments.write(".color %f %f %f\n" %(value[3][0], value[3][1], value[3][2]))
                outfd_moments.write(".arrow %f %f %f %f %f %f\n" %(key[0],key[1],key[2],new_value_x,new_value_y,new_value_z))

    with open(outfile_macro_file, "w") as outfd_macro:
        outfd_macro.write("open %s\n" %(args.infile))
        outfd_macro.write("""background solid white\ndel solvent\n~ribbon\nshow @ca\nsurface\ntransp 60,s\ncolor grey,s\n""")
        outfd_macro.write("open %s" %(outfile_moments_file))

    sys.stderr.write("Program finished!\n")


    #####################################################################
    ####            VISUALIZE RESULTS IN USCF-Chimera               #####
    #####################################################################


    question = input("Would you like to open %s in UCSF-Chimera? y/n\n"%(outfile_macro_file))
    if question == "y":
        for i in range(0,3):
            try:
                path = input("Please enter the full path to USCF-Chimera application:\n")
                subprocess.Popen([path, outfile_macro_file])
                sys.stderr.write("Opening %s in USCF-Chimera interface... \n" %(outfile_macro_file))
                sys.stderr.write("Closing program.\nBye!\n")
                break
            except (FileNotFoundError, PermissionError) as e:
                sys.stderr.write("Path not correct! %s\n" %e)
                if i == 2:
                    sys.stderr.write("You can check results by opening %s file on UCSF Chimera.\nClosing program.\nBye!\n" %(outfile_macro_file))
    else:
        sys.stderr.write("You can check results by opening %s file on UCSF Chimera.\nClosing program.\nBye!\n" %(outfile_macro_file))
