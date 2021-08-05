from osgeo import gdal
import glob
import numpy as np

######################################################################################################################
# DESCRIPTION: This function called raster_align takes a list of raster names, loads the rasters
# into memory and ensures they have the same aligned structure with the correct SRS codes and consitant resolutions
#
# AUTHOR: P. Alexander Burnham
# 5 August 2021
#
# INPUTS:
# rastNames (required): a list or array of file names including the required path if in another directory.
# resolution: the pixel dimensions to be used for all rasters. Defaults to the largest common pixel size
# SRS: this is the SRS code that sets the units and geospatial scale. Defaults to EPSG:3857 like google maps
# noneVal: the value to be used for pixels in the raster that contain no value. Defaults to -9999
#
# OUTPUT:
# It outputs a list of rescaled and gepspatialy aligned rasters
######################################################################################################################
def raster_align(rastNames=None, resolution=None, SRS=3857, noneVal=-9999):

    if rastNames is None:
        print("Error: No file list provided! Please pass raster_align a list of raster file names.")
        quit() # exit program and display message when no file names provided

    # define the espg code as a character for GDAL
    SRS_code = "EPSG:" + str(SRS)

    timeList = len(rastNames) # time dimension for list

    # initialize a mat to store files in during the loop and one to store the modification
    dataMat = [[0] * 3 for i in range(timeList)]

    # create a list of rasters in first column
    for t in range(0, timeList):
        dataMat[0][t] = gdal.Open(rastNames[t])

    # if resolution is not provided, default to the greatest common resolution
    if resolution is None:
        # get greatest common dimension
        for j in range(0, timeList):

            # put on same scale based on the SRS code to get consistant resolution values
            temp = gdal.Warp('', dataMat[0][j], dstSRS=SRS_code, format='VRT')
            dataMat[1][j] = temp.GetGeoTransform()[1]

        temp=None # flush from disk

        # get max resolution value
        resolution = np.max(dataMat[1][:])

    # do transformation and alingnment
    for i in range(0, timeList):
        dataMat[2][i] = gdal.Warp('', dataMat[0][i], targetAlignedPixels=True, dstSRS=SRS_code, format='VRT',
        outputType=gdal.GDT_Int16, xRes=resolution, yRes=-resolution, dstNodata=noneVal)

    return dataMat[2][:]
######################################################################################################################
# END FUNCTION
######################################################################################################################