#!/usr/bin/env python

# Defined utilities to script CMIP5_request.py
#
#  Updates
#  2022, S.G. Loyola (s.garcia.loyola@usp.br), Convert&Update from Aforc_ERA5 to Aforc_CMIP5
#
# -------------------------------------------------
# Getting libraries
# -------------------------------------------------
import datetime
import calendar

# -------------------------------------------------
# Increment date by custom months
# -------------------------------------------------
def addmonths4date(date,addmonths):
    month = date.month - 1 + addmonths
    year = date.year + month // 12
    month = month % 12 + 1
    day = min(date.day,calendar.monthrange(year,month)[1])
    return datetime.date(year,month,day)



