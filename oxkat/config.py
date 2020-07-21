#!/usr/bin/env python
# ian.heywood@physics.ox.ac.uk


import os
import subprocess

CWD = os.getcwd()
HOME = os.path.expanduser('~')

# ------------------------------------------------------------------------
#
# Singularity containers
#


#IDIA_CONTAINER_PATH = HOME+'/containers/'
IDIA_CONTAINER_PATH = '/idia/software/containers/STIMELA_IMAGES/'
#CHPC_CONTAINER_PATH = HOME+'/lustre/containers'
CHPC_CONTAINER_PATH = '/apps/chpc/astro/stimela_images/'
NODE_CONTAINER_PATH = HOME+'/containers/'
HIPPO_CONTAINER_PATH = '/data/mjh/containers/'

CASA_PATTERN = 'casa_'
CLUSTERCAT_PATTERN = 'ddfacet'
CODEX_PATTERN = 'codex-africanus'
CUBICAL_PATTERN = 'cubical'
DDFACET_PATTERN = 'ddfacet'
KILLMS_PATTERN = 'killms'
MAKEMASK_PATTERN = 'meqtrees'
PYBDSF_PATTERN = 'pybdsf'
RAGAVI_PATTERN = 'ragavi'
SHADEMS_PATTERN = 'shadems'
TRICOLOUR_PATTERN = 'tricolour'
WSCLEAN_PATTERN = 'wsclean'
WSCLEANIDG_PATTERN = 'wsclean*idg'


# ------------------------------------------------------------------------
#
# Paths for components and OUTPUTS
#


OXKAT = CWD+'/oxkat'
PARSETS = CWD+'/parsets'
TOOLS = CWD+'/tools'

GAINPLOTS = CWD+'/GAINPLOTS'
GAINTABLES = CWD+'/GAINTABLES'
IMAGES = CWD+'/IMAGES'
LOGS = CWD+'/LOGS'
SCRIPTS = CWD+'/SCRIPTS'
VISPLOTS = CWD+'/VISPLOTS'


# ------------------------------------------------------------------------
#
# MeerKAT primary beam models
#


BEAM_L = HOME+'/Beams/meerkat_pb_jones_cube_95channels_$(xy)_$(reim).fits'


# ------------------------------------------------------------------------
#
# Slurm settings
#

SLURM_DEFAULTS = {
	'TIME': '12:00:00',
	'PARTITION': 'debug',
	'NTASKS': '1',
	'NODES': '1',
	'CPUS': '8',
	'MEM': '60000'
}

SLURM_TRICOLOUR = {
    'TIME': '06:00:00',
    'PARTITION': 'debug',
    'NTASKS': '1',
    'NODES': '1',
    'CPUS': '20',
    'MEM': '64000'
}

SLURM_WSCLEAN = {
    'TIME': '12:00:00',
    'PARTITION': 'debug',
    'NTASKS': '1',
    'NODES': '1',
    'CPUS': '20',
    'MEM': '64000'
}

SLURM_HIGHMEM = {
    'TIME': '36:00:00',
    'PARTITION': 'HighMem',
    'NTASKS': '1',
    'NODES': '1',
    'CPUS': '32',
    'MEM': '480GB'
}

# ------------------------------------------------------------------------
#
# PBS settings
#

CHPC_ALLOCATION = 'ASTR1301'

PBS_DEFAULTS = {
	'PROGRAM': CHPC_ALLOCATION,
	'WALLTIME': '12:00:00',
	'QUEUE': 'serial',
	'NODES': '1',
	'PPN': '8',
	'MEM': '64gb'
}

PBS_TRICOLOUR = {
	'PROGRAM': CHPC_ALLOCATION,
	'WALLTIME': '06:00:00',
	'QUEUE': 'serial',
	'NODES': '1',
	'PPN': '24',
	'MEM': '120gb'
}

PBS_WSCLEAN = {
	'PROGRAM': CHPC_ALLOCATION,
	'WALLTIME': '12:00:00',
	'QUEUE': 'serial',
	'NODES': '1',
	'PPN': '24',
	'MEM': '120gb'
}


# ------------------------------------------------------------------------
#
# 1GC defaults
#

# Pre-processing
PRE_FIELDS = ''                      # Comma-separated list of fields to select from raw MS
PRE_NCHANS = 1024                    # Integer number of channels in working MS
PRE_TIMEBIN = '8s'                   # Integration time in working MS

# Scan intents
CAL_1GC_TARGET_INTENT = 'TARGET'     # (partial) string to match for target intents
CAL_1GC_PRIMARY_INTENT = 'BANDPASS'  # (partial) string to match for primary intents
CAL_1GC_SECONDARY_INTENT = 'PHASE'   # (partial) string to match for secondary intents

# Reference antennas
CAL_1GC_REF_ANT = 'auto'             # Comma-separated list to manually specify refant(s)
CAL_1GC_REF_POOL = ['m000','m001','m002','m003','m004','m006'] 
                                     # Pool to re-order for reference antenna list for 'auto'

# Field selection, IDs only at present. (Use tools/ms_info.py.)
CAL_1GC_PRIMARY = 'auto'             # Primary calibrator field ID
CAL_1GC_TARGETS = 'auto'             # Comma-separated target field IDs
CAL_1GC_SECONDARIES = 'auto'         # Comma-separated secondary IDs
                                     # - Lists of equal length in targets and secondaries maps cals to targets
                                     # - A single ID in uses same secondary for all targets
                                     # - A length mismatch reverts to auto, so double check!

# GBK settings
CAL_1GC_UVRANGE = '>150m'            # Selection for baselines to include during 1GC B/G solving (K excluded)
CAL_1GC_DELAYCUT = 2.5               # Jy at central freq. Do not solve for K on secondaries weaker than this
CAL_1GC_FILLGAPS = 24                # Maximum channel gap over which to interpolate bandpass solutions



# ------------------------------------------------------------------------
#
# 2GC defaults
#


# G settings
CAL_2GC_UVRANGE = '>150m'            # Selection for baselines to include during G solving
CAL_2GC_PSOLINT = '64s'              # Solution interval for phase-only selfcal
CAL_2GC_APSOLINT = 'inf'             # Solution interval for amplitude and phase selfcal


# ------------------------------------------------------------------------
#
# wsclean defaults
#


WSC_CONTINUE = False
WSC_FIELD = 0
WSC_STARTCHAN = -1
WSC_ENDCHAN = -1
WSC_CHANNELSOUT = 8
WSC_IMSIZE = 10240
WSC_CELLSIZE = '1.1asec'
WSC_BRIGGS = -0.3
WSC_NITER = 120000
WSC_GAIN = 0.1
WSC_MGAIN = 0.85
WSC_MULTISCALE = False
WSC_SCALES = '0,3,9'
WSC_SOURCELIST = True
WSC_BDA = False
WSC_BDAFACTOR = 24
WSC_NWLAYERSFACTOR = 3
WSC_PADDING = 1.2
WSC_NOMODEL = False
WSC_MASK = 'auto'
WSC_THRESHOLD = 1e-6
WSC_AUTOTHRESHOLD = 0.3
WSC_AUTOMASK = 5.0
WSC_FITSPECTRALPOL = 4
WSC_PREDICTCHANNELS = 64
WSC_MEM = 95
WSC_USEIDG = False # use image-domain gridder (not useable yet)
WSC_IDGMODE = 'CPU'
WSC_PARALLELDECONVOLUTION = 0 # 0 or specify max facet size (not useable yet)


# ------------------------------------------------------------------------
#
# MakeMask defaults
#


MAKEMASK_THRESH = 6.0
MAKEMASK_DILATION = 2


# ------------------------------------------------------------------------
#
# DDFacet defaults
#


# [Data]
DDF_DDID = 'D*'
DDF_FIELD = 'F0'
DDF_COLNAME = 'CORRECTED_DATA'
DDF_CHUNKHOURS = 2
DDF_DATASORT = 1
# [Predict]
DDF_PREDICTCOLNAME = 'MODEL_DATA'
DDF_INITDICOMODEL = ''
# [Output]
DDF_OUTPUTALSO = 'oenNS'
DDF_OUTPUTIMAGES = 'DdPMmRrIikz' # add 'A' to re-include spectral index map
DDF_OUTPUTCUBES = 'MmRi' # output intrinsic and apparent resid and model cubes
# [Image]
DDF_NPIX = 10125
DDF_CELL = 1.1
# [Facets]
DDF_DIAMMAX = 1.5
DDF_DIAMMIN = 0.05
DDF_NFACETS = 8 # crank this up (32?) to get better beam resolution if FITS beam is used
DDF_PSFOVERSIZE = 1.5
DDF_PADDING = 1.7 # padding needs increasing from default if NFacets is raised to prevent aliasing
# [Weight]
DDF_ROBUST = -0.3
# [Comp]
DDF_SPARSIFICATION = '0' # [100,30,10] grids every 100th visibility on major cycle 1, every 30th on cycle 2, etc.
# [Parallel]
DDF_NCPU = 32
# [Cache]
DDF_CACHERESET = 0
DDF_CACHEDIR = '.'
DDF_CACHEHMP = 1
# [Beam]
DDF_BEAM = '' # specify beam cube of the form: meerkat_pb_jones_cube_95channels_$(xy)_$(reim).fits
DDF_BEAMNBAND= 10
DDF_DTBEAMMIN = 1
DDF_FITSPARANGLEINCDEG = 0.5
DDF_BEAMCENTRENORM = True
DDF_FEEDSWAP = 1
DDF_BEAMSMOOTH = False
# [Freq]
DDF_NBAND = 8
DDF_NDEGRIDBAND = 8
# [DDESolutions]
DDF_DDSOLS = ''
DDF_DDMODEGRID = 'AP'
DDF_DDMODEDEGRID = 'AP'
# [Deconv]
DDF_GAIN = 0.12
DDF_THRESHOLD = 0.0
DDF_CYCLEFACTOR = 0
DDF_RMSFACTOR = 3.0	
DDF_DECONVMODE = 'hogbom'
DDF_SSD_DECONVPEAKFACTOR = 0.001
DDF_SSD_MAXMAJORITER = 3
DDF_SSD_MAXMINORITER = 120000
DDF_SSD_ENLARGEDATA = 0
DDF_HOGBOM_DECONVPEAKFACTOR = 0.15
DDF_HOGBOM_MAXMAJORITER = 10
DDF_HOGBOM_MAXMINORITER = 100000
DDF_HOGBOM_POLYFITORDER = 4
# [Mask]
DDF_MASK = 'auto' # 'auto' enables automasking 
                  # 'fits' uses the first *.mask.fits in the current folder
                  # otherwise pass a filename to use a specific FITS image
# [Misc]
DDF_MASKSIGMA = 5.5
DDF_CONSERVEMEMORY = 1


# ------------------------------------------------------------------------
#
# killMS defaults
#


# [VisData]
KMS_TCHUNK = 0.2
KMS_INCOL = 'CORRECTED_DATA'
KMS_OUTCOL = 'MODEL_DATA'
# [Beam]
KMS_BEAM = ''
KMS_BEAMAT = 'Facet'
KMS_DTBEAMMIN = 1
KMS_CENTRENORM = 1
KMS_NCHANBEAMPERMS = 95
KMS_FITSPARANGLEINCDEG = 0.5
KMS_FITSFEEDSWAP = 1
# [ImageSkyModel]
KMS_MAXFACETSIZE = 0.25
# [DataSelection]
KMS_UVMINMAX = '0.15,8500.0'
KMS_FIELDID = 0
KMS_DDID = 0
# [Actions]
KMS_NCPU = 32
KMS_DOBAR = 0
# [Solvers]
KMS_SOLVERTYPE = 'CohJones'
KMS_DT = 12
KMS_NCHANSOLS = 8
# [KAFCA]
KMS_NITERKF = 9
KMS_COVQ = 0.05


# ------------------------------------------------------------------------
#
# PyBDSF defaults
#


PYBDSF_THRESH_PIX = 5.0
PYBDSF_THRESH_ISL = 3.0
PYBDSF_CATALOGTYPE = 'srl'
PYBDSF_CATALOGFORMAT = 'fits'


# ------------------------------------------------------------------------
#
# ClusterCat defaults
#


CLUSTERCAT_NDIR = 7
CLUSTERCAT_CENTRALRADIUS = 0.15
CLUSTERCAT_NGEN = 100
CLUSTERCAT_FLUXMIN = 0.000001
CLUSTERCAT_NCPU = 32
