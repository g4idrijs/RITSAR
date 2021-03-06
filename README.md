# SARIT
Synthetic Aperture Radar (SAR) Image Processing Toolbox for Python

This is an initial version of a SAR image processing toolbox for Python.  The SciPy core libraries are required.  If using the omega-k algorithm, OpenCV is also required.  To get started, update the Python Dictionaries located in the parameters folder or leave the default values in place.  In main.py in the top level directory, comment out those algorithms you do not wish to use.

Current capabilities include modeling the phase history for a collection of point targets as well as processing phase histories using the polar format, backprojection, and omega-k algorithms.

Over the coming months, I will update this readme with more detailed instructions as well as interfaces for AFRL Gotcha data and DIRSIG SAR simulated data.

If anyone is interested in collaborating, I can be reached at dm6718@g.rit.edu.  Ideas on how to incorporate a GUI or package the code for a distutils distribution would be greatly appreciated.
