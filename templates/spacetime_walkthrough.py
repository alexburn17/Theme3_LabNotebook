# Date created:  April 21, 2023
# Author: P. Alexander Burnham

# The main objective of the spacetime python library is to make tasks like loading, rescaling, merging, and conducting
# mathmatical operations on spatiotemporal (or other D-dimensional data sets) easier for the user by providing a set of
# concise yet powerful functions. spacetime opperations utilize a cube-like structure for all data sets that makes storing
# and manipulating large D-dimensional datasets more efficient. For scientists working with spatiotemporal data
# (such as climate or weather data sets) spacetime is an ideal platform that allows the user to focus on the science rather
# than the coding. Here we explore the process of loading raster files, rescaling and writing to disc for a number of
# different data cleaning scenarios.



# load in functions from spacetime code base
from spacetime.input.readData import read_data
from spacetime.scale.rasterAlign import raster_align
from spacetime.scale.rasterTrim import raster_trim
from spacetime.objects.fileObject import file_object
from spacetime.operations.cubeSmasher import cube_smasher
from spacetime.operations.makeCube import make_cube
from spacetime.operations.loadCube import load_cube
from spacetime.graphics.dataPlot import plot_cube
from spacetime.operations.time import cube_time, return_time, scale_time, select_time
from spacetime.operations.cubeToDataframe import cube_to_dataframe
import matplotlib.pyplot as plt
import glob
from osgeo import gdal
import numpy as np
import pandas as pd
import netCDF4 as nc
from datetime import datetime, timedelta

################################################################################################################
# Loading Data into Spacetime
################################################################################################################
# Spacetime takes file names/paths as lists. Here we set up a list of geotif files. The initial `read_data()` function
# in spacetime uses GDAL's python bindings at it's base. It can read any file type that GDAL can read. For the full list
# of supported types, see the [GDAL API](https://gdal.org/python/). When a great number of files need to be read in,
# automated python functions like `grep` can pull lists of file paths from a given directory into the system based on
# file extension or some other feature of the file names. Here we pull in a few different tifs manually.


# create our list of file paths realtive to our directory
data = ["demoData/N0_AKestrel_1976_1980.tif", "demoData/N0_AKestrel_1977_1981.tif", "demoData/N0_AKestrel_1978_1982.tif"]

# spacetime function "read_data()" to create a file object
ds = read_data(data)

# Querry the file object
ds.get_epsg_code() # examine the EPSG code for each file
ds.get_nodata_value() # no data value
ds.get_UL_corner() # upper left corners
ds.get_band_number() # band numbers

# Examine the actual data sets
plotData = ds.get_data_array() # extract the data sets from the file object

# plot the first file removing values below 0 (i.e. nodata vals)
plt.imshow(plotData[0], vmin=0)
#plt.show()

# Here we look at the dimensions of the first dataset in the list, what is the shape of the first file?
ds.get_data_array()[0].shape

# Lets turn these files into a cube object
yearObj = cube_time(start="1976", length=3, scale = "year") # make a time vec


# Now we will make a cube object from this file object. When cubes are created, a .nc4 file is written to disk. This allows
# for virtualization through a number of third-party python libraries like dask and netCDF4. The arguments `organizeFiles`
# and `organizeBands` set up the structure of the cube based on the data files. "filestotime" and "bandstotime" together
# will take every file and every band within every file and treat them as time slices when compiling the cube.
# If variables are stored in different files or bands, the "filestovar" or "bandstovar" arguments would be used instead.

cube3d = make_cube(data = ds, fileName = "test1.nc4", organizeFiles = "filestotime", organizeBands="bandstotime", timeObj = yearObj) # make a cube


# Setting up a cube with multiple variables. Here we have a set of files names 2001 and 2002. Each has three bands that are RGB color bands
data1 = ["demoData/2001.tif", "demoData/2002.tif"] # read files

# make file object
ds1 = read_data(data1)

# check bands
ds1.get_band_number()

#We have the correct number of bands, 3. Lets assemble our cube. We use the "filestotime" and "bandstovar" arguments and pass R G and B to varNames as a list.
# make time vector
yearObj1 = cube_time(start="2001", length=2, scale = "year")

# make cube
cube4d = make_cube(data = ds1, fileName = "test2.nc4", organizeFiles = "filestotime", organizeBands="bandstovar", varNames=["R","G","B"], timeObj=yearObj1)

# Querrying our cube object
cube3d.get_data_array()
cube4d.get_data_array()



################################################################################################################
# Spatial Scaling
################################################################################################################
# In the previous section, we set up several cubes from geotif files and explored some of the basic querrying and cube
# building functionality of spacetime. However, all of the files we were working with, had the same scales and grid sizes.
# Spacetime has the functionality to rescale rasters of different extents, grid sizes, epsg codes etc. and create a cleaned
#cube where all of those factors are consistent across the data layers.


# read files and load data
data = ["demoData/LULC_1995.tif", "demoData/India_cropped-area_1km_2016.tif"]
ds = read_data(data)

# check number of bands
ds.get_band_number()

# check the epsg codes
ds.get_epsg_code()

# check the raster dimensions
ds.get_dims()

# check pixel size
ds.get_pixel_size()

# check no data values
ds.get_nodata_value()

# Get the array data
arrays = ds.get_data_array()

# plot file 1
plt.imshow(arrays[0], vmin=0, vmax=17)
#plt.show()

# plot file 2
plt.imshow(arrays[1], vmin=0, vmax=100)
#plt.show()

# Let's rescale these files using some spacetime functions.
alignedDS = raster_align(data=ds, resolution=.08, SRS=4326, noneVal=127)

# check epsg codes
alignedDS.get_epsg_code()

# get raster dimensions
alignedDS.get_dims()

# pixel size
alignedDS.get_pixel_size()

# check no data values
alignedDS.get_nodata_value()

# Lets also look at the rescaled images.
scaledArray = alignedDS.get_data_array()

# plot file 1
plt.imshow(scaledArray[0], vmin=0, vmax=17)
# plt.show()

# plot file 2
plt.imshow(scaledArray[1], vmin=0, vmax=100)
# plt.show()

# Cropping file objects
trimmedDS = raster_trim(alignedDS)

# lets compare the dimensions of the new objects
trimmedDS.get_dims()



#Comparing the plotted images reveals that the files are now aligned and trimmed
trimmedArray = trimmedDS.get_data_array()

# plot file 1
plt.imshow(trimmedArray[0], vmin=0, vmax=17)
#plt.show()

# plot file 2
plt.imshow(trimmedArray[1], vmin=0, vmax=100)
#plt.show()

# Make a cube
yearObj = cube_time(start="1995", length=2, scale = "year", skips = 21) # create time vec

# We will now create a cube by assigning files and bands to time.
cube = make_cube(data = trimmedDS, fileName = "indiaCube.nc4", organizeFiles = "filestotime", organizeBands="bandstotime", timeObj = yearObj)

# Finally, lets look at the data
cube.get_data_array()

################################################################################################################
# Temporal Scaling
################################################################################################################
# Let's load two raster files that contain 101 bands each. Each band is a year. The datasets contain the same data, however,
# they are at different spatial scales. We will first create the file object

# read files and load data
data = ["demoData/Carya_ovata_sim_disc_10km.tif", "demoData/Carya_ovata_sim_disc_1km.tif"]
ds = read_data(data)

# scale data
scaledData = raster_align(ds)
trimmedData = raster_trim(scaledData)

# set up time vec for 101 months starting from 2000-10-12
monthObj = cube_time(start="2000-10-12", length=101, scale = "month")

# make cube
cube = make_cube(data = trimmedData, fileName = "cube1.nc4", organizeFiles = "filestovar", organizeBands="bandstotime", timeObj = monthObj, varNames = ["10km", "1km"])

# scale time by year
timeScaled = scale_time(cube=cube, scale="year", method="mean")

# extract data from cube
timeScaled.get_data_array()

# a new time vec
monthObjDay = cube_time(start="2000-10-12", length=101, scale = "day")

# make cube
cubeDay = make_cube(data = trimmedData, fileName = "cubeDay.nc4", organizeFiles = "filestovar", organizeBands="bandstotime", timeObj = monthObjDay, varNames = ["10km", "1km"])

# the first of the month
selectedDay = select_time(cube=cubeDay, range="entire", scale = "day", element=1)

# print the time vector
selectedDay.get_time()

# select aprils between 2001 and 2003
selectedApril = select_time(cube=cube, range=["2000", "2005"], scale = "month", element=4)

# print the time vector
selectedApril.get_time()



################################################################################################################
# Cube Operations
################################################################################################################


#Let's start by creating a cube as we have done previously for the yearly Carya ovata data. We will rescale and trim the data sets

# scale data
scaledData = raster_align(ds)
trimmedData = raster_trim(scaledData)


#Finally, we will make a cube Object. Each file will be assigned to a variable (10km and 1km).
yearObj = cube_time(start="2000", length=101, scale = "year") # set up time vec for 101 years

# make cube
cube = make_cube(data = trimmedData, fileName = "yearCube.nc4", organizeFiles = "filestovar", organizeBands="bandstotime", timeObj = yearObj, varNames = ["10km", "1km"])

# Mathmatical Operations
answer = cube_smasher(eq = "a + 1000 ** c", a=cube, b=1000, c = 2, parentCube = cube)

# pre operations value = 0
cube.get_data_array()[0,0,50,50]

# after the operation = 1000000
answer.get_data_array()[0,0,50,50]



