import re
import numpy as np
from osgeo import gdal

######################################################################################################################
# DESCRIPTION: raster_trim takes a list of rasters as trims them to the greatest common dimensions
# and writes out a list of numpy arrays. The last two elements in the list are the greatest common coords
# for the upper left and lower right corners and the GDAL geotransform output
#
# AUTHOR: P. Alexander Burnham
# 9 August 2021
#
# INPUTS:
# rastList (required): a list of raster objects typically already rescaled by the raster_align function.
#
# OUTPUT:
# A list of trimmed raster matrices with the last two elements as a vector of the greatest common coords
# for the upper left and lower right corners and the GDAL geotransform output vector
######################################################################################################################

def raster_trim(rastList=None):

    if rastList is None:
            print("Error: No raster list provided! Please pass raster_trim a list of rasters processed by raster_align.")
            quit() # exit program and display message when no file names provided


    outList = [] # initialize a list

    # here is where the loop needs to be:
    for i in range(len(rastList)):

        # these need to be indexed the same way
        gt = rastList[i].GetGeoTransform()
        band = rastList[i].GetRasterBand(1)

        # create matrix for storing corner data
        cornerArray = np.empty(shape=(len(rastList),4))

        # loop through and extract corner data
        for i in range(len(rastList)):

            # get meta data for each raster
            meta = gdal.Info(rastList[i])

            # use regex to extract upper and lower left corners
            Uleft = re.search(r'Upper Left  \(([^)]+)', meta).group(1)
            Lright = re.search(r'Lower Right \(([^)]+)', meta).group(1)

            # create full string
            corners = Uleft + ',' + Lright

            # numeric list of corners (upper left [0-1] and lower right [2-3])
            cornersList = corners.split(',')
            cornersList = [ float(x) for x in cornersList ]

            # add corners to an array
            cornerArray[i,:] = cornersList

        # find greatest common dimensions to crop rasters to:
        # highest x, lowest y (upper left corner): lowest x, highest y (lower right corner)
        cornersCommon = [np.max(cornerArray[:,0]), np.min(cornerArray[:,1]), np.min(cornerArray[:,2]), np.max(cornerArray[:,3])]


        #p1 = point upper left of bounding box
        #p2 = point bottom right of bounding box
        p1 = (cornersCommon[0], cornersCommon[1])
        p2 = (cornersCommon[2], cornersCommon[3])


        # get pixel sizes and the lower left of the raster
        xinit = gt[0]
        yinit = gt[3]
        xsize = gt[1]
        ysize = gt[5]

        # get row and columns
        row1 = int((p1[1] - yinit)/ysize)
        col1 = int((p1[0] - xinit)/xsize)
        row2 = int((p2[1] - yinit)/ysize)
        col2 = int((p2[0] - xinit)/xsize)

        # trim the matrix
        dataLayer = band.ReadAsArray(col1, row1, col2 - col1, row2 - row1)

        # append the data layers to the list
        outList.append(dataLayer)

        ###################################################################################################

    # add the common coords and geotransform data
    outList.append(cornersCommon)
    outList.append(gt)

    return outList
