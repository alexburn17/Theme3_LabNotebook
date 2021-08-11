import numpy as np
from osgeo import gdal

######################################################################################################################
# DESCRIPTION: get_coords takes in a list of trimmed raster layers from raster_trim
# and returns a list of lat and long coords
#
# AUTHOR: P. Alexander Burnham
# 10 August 2021
#
# INPUTS:
# trimmedRasts (required): a list of trimmed raster arrays from raster_trim
#
# OUTPUT:
# A list with the first element as a vector of lats and the second a vector of lons
######################################################################################################################

def get_coords(trimmedRasts=None):

    if trimmedRasts is None:
            print("Error: No raster list provided! Please pass get_coords a list of rasters processed by taster_trim.")
            quit() # exit program and display message when no file names provided

    ###################################################################################################

    outList = []

    # get the necessary structures from the object
    data = trimmedRasts[0]
    gt = trimmedRasts[-1]
    cornersCommon = trimmedRasts[-2]

    # pull out pixel size
    xsize = gt[1]
    ysize = gt[5]

    # get data mat dimensions
    width = len(data[0,:])
    height = len(data[:,0])

    # get lower left corner of clipped matrix
    ylow = cornersCommon[0]
    xlow = cornersCommon[3]

    # dimensions from 0 to max dims of dataset
    mx=np.arange(start=0, stop=width)
    my=np.arange(start=0, stop=height)

    # get lats and longs
    longVec = np.multiply(mx, xsize) + xlow # longitude vector
    latVec = np.multiply(my, ysize) + ylow # latitude vector

    outList.append(latVec)
    outList.append(longVec)

    return outList

    ###################################################################################################
