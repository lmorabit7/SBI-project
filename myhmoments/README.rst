MYHMOMENTS: CALCULATION OF HYDROPHOBICITY MOMENTS IN LOCAL REGIONS
==================================================================

The Myhmoments project provides a tool to calculate hydropathy moments in surface
regions of proteins given a pdb file.

Installation
=================
Before starting the installation:
- **make sure that Python is installed correctly**.
- installing NumPy and Biopython beforehand is recommended.

To start using the package you need to build and install Myhmoments. Download and unzip the source code
from https://github.com/lmorabit7/SBI-project, go to this directory at the command line, and type::

    python3 setup.py build
    python3 setup.py test
    sudo python3 setup.py install

Alternatively, if you prefer to install the package locally (with a symlink) simply type::

    pip3 install -e .

To use (with caution), simply do in python interactive mode::

>>> from myhmoments import *

All the functions of the myhmoments modules should be available now.

Myhmoments can also be executed as a standlone program from the commandline. The program will generate
output files and the possibility to start a subprocess to open the results in Chimera (if installed). Type:

    python3 myhmoments -i file.pdb



Python requirements
=================
Myhmoments is supported and tested on python3. Thus, we strongly recommend using
Python 3.5 from http://www.python.org.



Dependencies
=================
You must install the following dependencies in order to be able to fully use myhmoments:

- NumPy, see http://www.numpy.org

- Biopython, see http://www.biopython.org/



Distribution Structure
======================

- ``README.rst``  -- This file.
- ``MANIFEST.in`` -- Tells distutils what files to distribute.
- ``setup.py``    -- Installation file.
- ``myhmoments/`` -- The main code base code.
- ``.gitignore``  -- Tells python which files should ignore to not commit to source control.
