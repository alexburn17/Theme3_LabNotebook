import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc

######################################################################################################################
# DESCRIPTION: summarize is a function that takes a netcdf4 dataset, removes no data values, trims the data set by a
# bounding box or a point in space (defaults to entire data set) and computes a summary statistic for each time point
#
# AUTHOR: P. Alexander Burnham
# 7 September 2021
#
# INPUTS:
# data: A netCDF4 dataset
# noData: a numeric value for the noData value used in the dataset (defaults to -9999)
# value: a character string denoting the name of the variable to be extracted
# operator: a character string for the summery stat to be computed (options are: mean, min, max, sum, median)
# UL: lat and lon coords in the the dataset's scale for the upper left corner of the bounding box
# LR: lat and lon coords in the the dataset's scale for the lower right corner of the bounding box
# latPoint: a lat point in the the dataset's scale
# lonPoint: a lon point in the the dataset's scale
#
# OUTPUT:
# A list containing the processed time and y value variables as numpy arrays
######################################################################################################################

def summarize(data=None, noData = -9999, value="value", operator = "mean", UL = None, LR = None, latPoint = None, lonPoint = None, plot = "no"):

    # extract vars
    lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]
    time = data.variables['time'][:]
    val = data.variables[value][:]

    # cropping coords are given, crop the dataset
    if UL != None:

        # trim 3D array to bounds
        upper = [np.abs(lat - UL[0]).argmin()]
        lower = [np.abs(lat - LR[0]).argmin()]
        left = [np.abs(lon - UL[1]).argmin()]
        right = [np.abs(lon - LR[1]).argmin()]

        # slice up the array
        val = val[:, upper[0]:lower[0], left[0]:right[0]]

        # get rid of no data values for summery
        val[val == noData] = np.nan

        # do the summery operation based on the operator of choice
        if operator == "mean":
            yVal = np.nanmean(val, axis = (1,2))
        if operator == "min":
            yVal = np.nanmin(val, axis = (1,2))
        if operator == "max":
            yVal = np.nanmax(val, axis = (1,2))
        if operator == "median":
            yVal = np.nanmedian(val, axis = (1,2))
        if operator == "sum":
            yVal = np.nansum(val, axis = (1,2))

    # point given pull it out
    if latPoint != None:

        # calculate index for point
        y = [np.abs(lat - latPoint).argmin()]
        x = [np.abs(lon - lonPoint).argmin()]

        # slice up the array
        yVal = val[:, y[0], x[0]]

        # get rid of no data values for summery
        yVal[yVal == noData] = np.nan

        operator = ''


    if LR  == None and latPoint == None:

        # get rid of no data values for summery
        val[val == noData] = np.nan

        # do the summery operation based on the operator of choice
        if operator == "mean":
            yVal = np.nanmean(val, axis = (1,2))
        if operator == "min":
            yVal = np.nanmin(val, axis = (1,2))
        if operator == "max":
            yVal = np.nanmax(val, axis = (1,2))
        if operator == "median":
            yVal = np.nanmedian(val, axis = (1,2))
        if operator == "sum":
            yVal = np.nansum(val, axis = (1,2))


    if plot == "yes":

        plt.plot(time, yVal, color='lightcoral', linewidth=4)

        plt.ylabel(operator + ' ' + value, fontsize=18)
        plt.xlabel("time", fontsize=18)
        plt.grid(True)

        plt.show()

    return [time, yVal]