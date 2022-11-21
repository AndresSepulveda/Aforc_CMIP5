# Aforc_CMIP5

Scrips for ECMWF CDSAPI app data download, processing, renaming, and interpolation for use with CMIP5 data.

* 2022 - S.G. Loyola (s.garcia.loyola@usp.br) - Update from Aforc_ERA5 to Aforc_CMIP5

Here is a set of matlab and python routines allowing to :

1- Download native CMIP5 monthly atmospheric data into netcdf format (Run/DATA/CMIP5_native_configname/ directory)

2- Convert the raw data into a format useable by the ONLINE_BULK capability of croco ocean model. Run/DATA/CMIP_configname/ directory)

        - apply correct unit transformation
        - rename the variable with "CROCO" compatible names

- Pre-requisite : First the user need to install the ERA5 python API : https://cds.climate.copernicus.eu/api-how-to

- Edit the cmip5_crocotools_param.py parameter file

- Then to download the CMIP5 data (step 1 above)

        >> python3 CMIP5_request.py

- Then to unzip the raw download data and change name of the netcdf files

        >> ./CMIP5_unzip.sh

- Then to convert the CMIP5 data with unit and name into a "CROCO online bulk" compatible format (unit and names) (step 2 above):

        >> python3 CMIP5_convert.py

- If the user want to interpolate the data onto the croco model grid in order to crerate frc/blk netcdf file (Optional step 3 above)

- Adapt the crocotools_param.m section :

        %  Options for make_CMIP5

- Finally, executing make_ERA5 under matlab should work fine.
