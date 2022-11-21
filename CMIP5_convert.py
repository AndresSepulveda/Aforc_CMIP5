#!/usr/bin/env python
#
# CMIP5_convert.py
#
# Script to convert CMIP5 original files obtained from the Climate Data
# Store (CDS) of Copernicus https://cds.climate.copernicus.eu into
# a format and using units which can be used by the online interpolation of CROCO
#
#  2022, S.G. Loyola (s.garcia.loyola@usp.br), Convert&Update from Aforc_ERA5 to Aforc_CMIP
#
# -------------------------------------------------
# Getting libraries and utilities
# -------------------------------------------------
#
from datetime import date
import json
from netCDF4 import Dataset as netcdf
import numpy as np
import os
import pandas as pd
#
# -------------------------------------------------
# Import my crocotools_param_python file
from cmip5_crocotools_param import *
#
# -------------------------------------------------
# Setting processed output directory
# -------------------------------------------------
# Get the current directory
os.makedirs(cmip5_dir_processed,exist_ok=True)
#
# -------------------------------------------------
# Loading CMIP5 variables's information as 
# python Dictionary from JSON file
# -------------------------------------------------
with open('CMIP5_variables.json', 'r') as jf:
    cmip5 = json.load(jf)
#
# -------------------------------------------------
# Loop on Years and Months
# -------------------------------------------------
timesteps=range(1140)
d=pd.date_range('2006-1-1','2100-12-31',freq='MS')
iyear=d.year
imonth=d.month
#
for k in range(len(variables)):
  for isteps in timesteps:
#
# -------------------------------------------------
# Loop on variables names
# -------------------------------------------------
#
#     for k in range(len(variables)):
#
# Variable's name, long-name and level-type
#
        vname = variables[k]
        vlong = cmip5[vname][0]
        vnc   = cmip5[vname][2]
        print('  Processing variable: ' + vname + ' -> Y' + str(iyear[isteps]) + 'M' + str(imonth[isteps]))
#
# Read input filedate.toordinal(date(Yorig,1,1))
#
        fname_in = cmip5_dir_raw + '/CMIP5_' + experiment + '_' + model + '_' + period + '_' + vname.upper() + '.nc'
        nc = netcdf(fname_in,'r+',format='NETCDF4')
       	time = nc.variables['time'][isteps]
       	lat = nc.variables['lat'][:]
       	lon = nc.variables['lon'][:]
       	data = nc.variables[vnc][isteps,:,:]
       	nc.close()
#
# Flip latitudes (to have increasing latitudes...)
#
        lat = np.flip(lat, axis=0)
        data = np.flip(data, axis=1)
#
# Missing values and multiply by cff to change unit
#
        try:
            mvalue=data.fill_value
        except AttributeError:
            print ('No fill value.. use nan')
            mvalue=np.nan

        data=np.array(data)
        #data=conv_cff[k]*data
        data[np.where(data==mvalue)]=9999.
#
# Convert time from days since 1850-1-1 0:0:0 into days since Yorig-1-1 0:0:0
#
        #time = time / 24.
        time = time - date.toordinal(date(Yorig,1,1)) \
	            + date.toordinal(date(1850,1,1))
#
# Changes names
#
        if vname=='u10':
            vname='u10m'
#
        if vname=='v10':
            vname='v10m'
#
# Create and write output netcdf file
#
#
        fname_out = cmip5_dir_processed + '/' + vname.upper() + '_Y' + str(iyear[isteps]) + 'M' + str(imonth[isteps]) + '.nc'
        nw = netcdf(fname_out,mode='w',format='NETCDF4')
        dimlon  = nw.createDimension('lon',  len(lon))
        dimlat  = nw.createDimension('lat',  len(lat))
        dimtime = nw.createDimension('time', None)
        varlon = nw.createVariable('lon', 'f4',('lon',))
        varlat = nw.createVariable('lat', 'f4',('lat',))
        vartime = nw.createVariable('time', 'f4',('time',))
        vardata = nw.createVariable(vname.upper(), 'f4',('time','lat','lon'))
        varlon.long_name = 'longitude of RHO-points'
        varlat.long_name = 'latitude of RHO-points'
        vartime.long_name = 'Time'
        varlon.units = 'degree_east'
        varlat.units = 'degree_north'
        vartime.units = 'days since '+str(Yorig)+'-1-1'
        vardata.missing_value = 9999.
        vardata.units = units[k]
        vardata.long_name = vlong
        varlon[:]=lon
        varlat[:]=lat
        vartime[0]=time
        vardata[0,:,:]=data
        nw.close()
        del data
        del time
#
# Print last message on screen
print(' ')
print(' CMIP5 files conversion done ')
print(' ')
