#
# For CMIP python crocotools parameters list
#
# CAUTION IT MUST BE CONSISTENT with your MATLAB CROCOTOOLS_PARAM.m file in Run directory
#
#  2022 - S.G. Loyola (s.garcia.loyola@usp.br) - Update from Aforc_ERA5 to Aforc_CMIP5
#
# *******************************************************************************
#                         U S E R  *  O P T I O N S
# *******************************************************************************
#
# General path
#
config_dir = '/home/sgl/CROCO/SWA/CMIP/Run/'  # must be the same than crocotools_param
config_name = 'Benguela_LR'
#
# Dates limits
#
year_start = 2006
month_start = 1
year_end = 2100
month_end = 12
#
# Year origin of time
#
Yorig=1990
#
# Overlapping days (at the beginning/end of each month)
#
n_overlap = 2
#
# Original CMIP directory
#
cmip5_dir_raw = config_dir + 'DATA/CMIP5_native_' + config_name
#
# Output CMIP directory
#
cmip5_dir_processed = config_dir + 'DATA/CMIP5_' + config_name
#
# SCENARIOS RCP
# experiments = 'rcp_2_6'
#               'rcp_4_5'
#		'rcp_6_0'
#		'rcp_8_5'
experiment= 'rcp_2_6'
#
period= '200601-210012'
#
# MODELS
#
# models = 'ipsl_cm5a_mr' (IPSL, France)
#	   'fio_esm' (FIO, China)
# 	   'giss_e2_r' (NASA, USA)
#          'bcc_csm1_1_m' (BCC, China)
#          'cesm1_cam5' (NCAR, USA)
#          'csiro_mk3_6_0' (CSIRO, Australia)
#
model='csiro_mk3_6_0'
#
ensemble_member='r1i1p1'
#
# Request variables (see available at CMIP5_variables.json)
#
# variables = ['stt','msl','tcc','u10','v10','t2m','strd','ssrd','ewss','nsss','e','mpf','sshf','slhf','ssh','q','r']
#
variables = ['sst', 'tp',        'strd' ,  'ssrd',  't2m' , 'q',        'u10'   ,'v10'  , 'ssh','ewss','nsss']
units =     ['K'  , 'kg m-2 s-1', 'W m-2' , 'W m-2' ,'K'   , 'kg kg-1' , 'm s-1' ,'m s-1', 'cm','N m-2','N m-2']
#
# Request area ([north, west, south, east])
#
ownArea = 0 	# 0 if area from a crocotools_param.m file
                # 1 if own area
#
if ownArea == 0:
    # To complete if ownArea==0
    paramFile = config_dir + 'crocotools_param.m' # path the crocotools_param file of the simulation
else:
    # To complete if ownArea==1
    lonmin=7
    lonmax=23
    latmin=-45
    latmax=-20
#
# *******************************************************************************
#                         E N D     U S E R  *  O P T I O N S
# *******************************************************************************
