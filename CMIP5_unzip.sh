#!/bin/bash
#
#  This code decompresses the original .zip CMIP5 files downloaded from ECMWF
#  changes the name to link with python codes' names and then remove the initial .zip
#
#  2022 - S.G. Loyola (s.garcia.loyola@usp.br)
#
# Directroy of raw CMIP5 downloaded data
cd '/home/sgl/CROCO/SWA/CMIP/Run/DATA/CMIP5_native_Benguela_LR'
#
for z in *.zip; do
    unzip -o "$z";
    mv "$(unzip -Z1 $z)" "${z%%.*}.nc";
    rm -rf "${z%%.*}.zip";
done
