#!/usr/bin/env python
#
#  Script to download CMIP5 datasets from the Climate Data
#  Store (CDS) of Copernicus https://cds.climate.copernicus.eu
#
#  This script use the CDS Phyton API[*] to connect and download specific CMIP5
#  variables, for a chosen area and monthly date interval, required by CROCO to
#  perform simulations with atmospheric forcing. Furthermore, this script use
#  CMIP5 parameter names and not parameter IDs as these did not result in stable
#  downloads.
#
#  Tested using Python 3.8.6 and Python 3.9.1. This script need the following
#  python libraries pre-installed: "calendar", "datetime", "json" and "os".
#
#  [*] https://cds.climate.copernicus.eu/api-how-to
#
#  2022, S.G. Loyola (s.garcia.loyola@usp.br), Convert&Update from Aforc_ERA5 to Aforc_CMIP5
#
#  You may see all available CMIP5 variables at the following website
#  https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip5-monthly-single-levels?tab=overview
# -------------------------------------------------
# Getting libraries and utilities
# -------------------------------------------------
import cdsapi
from CMIP5_utilities import *
import calendar
import datetime
import json
import os
from zipfile import ZipFile
# -------------------------------------------------
# Import my crocotools_param_python file
from cmip5_crocotools_param import *
print('Model is '+str(model))
#
# -------------------------------------------------
#
if ownArea == 0:
    dl = 2
    lines = [line.rstrip('\n') for line in open(paramFile)]
    for line in lines:
        if "lonmin" in line:
            for i in range(len(line)):
                if line[i] == "=":
                    iStart = i+1
                elif line[i] == ";":
                    iEnd = i
            lonmin = line[iStart:iEnd]
        elif "lonmax" in line:
            for i in range(len(line)):
                if line[i] == "=":
                    iStart = i+1
                elif line[i] == ";":
                    iEnd = i
            lonmax = line[iStart:iEnd]
        elif "latmin" in line:
            for i in range(len(line)):
                if line[i] == "=":
                    iStart = i+1
                elif line[i] == ";":
                    iEnd = i
            latmin = line[iStart:iEnd]
        elif "latmax" in line:
            for i in range(len(line)):
                if line[i] == "=":
                    iStart = i+1
                elif line[i] == ";":
                    iEnd = i
            latmax = line[iStart:iEnd]
#
lonmin = str(float(lonmin)-dl)
lonmax = str(float(lonmax)+dl)
latmin = str(float(latmin)-dl)
latmax = str(float(latmax)+dl)
print ('lonmin-dl = ', lonmin)
print ('lonmax+dl =', lonmax)
print ('latmin-dl =', latmin)
print ('latmax+dl =', latmax)
#
# -------------------------------------------------
area = [latmax, lonmin, latmin, lonmax]
#
# -------------------------------------------------
# Setting raw output directory
# -------------------------------------------------
# Get the current directory
os.makedirs(cmip5_dir_raw,exist_ok=True)
#
# -------------------------------------------------
# Loading CMIP5 variables's information as 
# python Dictionary from JSON file
# -------------------------------------------------
with open('CMIP5_variables.json', 'r') as jf:
    cmip5 = json.load(jf)
#
# -------------------------------------------------
# Downloading CMIP5 datasets
# -------------------------------------------------
# Variables/Parameters loop
    for k in range(len(variables)):
#
        # Variable's name, long-name and level-type
        vname = variables[k]
        vlong = cmip5[vname][0]
#
        # Request options
        options = {
             'variable': vlong,
             'area': area,
             'format': 'zip',
             'experiment': experiment,
	     'model': model,
             'ensemble_member': ensemble_member,
             'period': period
                }
        # Product "single-levels"
        product = 'projections-cmip5-monthly-single-levels'
        # Output filename
        fname = 'CMIP5_' + experiment + '_' + model + '_' + period + '_' + vname.upper() + '.zip'   
        output = cmip5_dir_raw + '/' + fname
#
	# Printing message on screen
        print('                                                           ')
        print('-----------------------------------------------------------')
        print(' Performing CMIP5 data request, please wait...             ')
        print(' Model = ',model,'                                         ')
        print(' Experiment = ',experiment,'                               ')
        print(' Period = ',period,'                                       ')
        print(' Variable = ',vlong,'                                      ')
        print('-----------------------------------------------------------')
        print('Request options: ')
        print(options)
#
        # Server ECMWF-API
        c = cdsapi.Client()
#
        # Do the request
        c.retrieve(product,options,output)
#
# UnZip files from CMIP5 raw file
with ZipFile(output, 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
#
# Print output message on screen
print('                                               ')
print(' CMIP5 data request has been done successfully! ')
print('                                               ')




