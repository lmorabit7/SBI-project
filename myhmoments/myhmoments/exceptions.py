
"""
This module contains the different exception classes created specifically for hpmcalculator.

"""

class FileExtensionError(Exception):
    """ An exception is raised when the input file does not contain .pdb extension"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Incorrect input file extension: %s. Please, input a .pdb file" %(self.value)

class InputValueError(Exception):
    """
    An exception is raised when the input value is smaller than a given minimum threshold
    and greater than a given maximum threshold.
    """
    def __init__(self, value):
        self.value = value

class ThresholdError(InputValueError):
    """
    An exception is raised when the threshold value is smaller than 0.2
    and greater than 0.8.
    """

    def __str__(self):
        return "Incorrect threshold value: %s. Threshold value x: 0.2<=x<=0.8" %(self.value)

class RadiusError(InputValueError):
    """
    An exception is raised when the radius value is smaller than 4.0
    and greater than 10.0.
    """

    def __str__(self):
        return "Incorrect radius value: %s. Radius value x: 4.0<=x<=10.0" %(self.value)
