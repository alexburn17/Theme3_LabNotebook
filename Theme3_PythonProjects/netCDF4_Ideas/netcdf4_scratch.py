import netCDF4 as nc
import numpy as np

# locate local path to .nc4 test file
fn = "/Users/pburnham/Documents/GitHub/Theme3_LabNotebook/Theme3_PythonProjects/netCDF4_Ideas/data/prcp_1980.nc4"

# create netcdf data set
ds = nc.Dataset(fn)

# Pull precipitation data out of the netcd4 object
prcp=ds['prcp'][:]

# print a subset of the masked array
print(prcp[0, 500:505, 200:205])

# basic summary stats
print(np.max(prcp))
print(np.min(prcp))
print(np.mean(prcp))

