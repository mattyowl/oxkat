# ian.heywood@physics.ox.ac.uk


import pickle
import sys
sys.path.append('oxkat')
from pickle_handler import get_project_info

project_info = get_project_info()

myms = project_info['master_ms']
primary_field = project_info['primary'][1]
primary_tag = project_info['primary_tag']


if primary_tag == '0408':
    newphasecentre = 'J2000 04h08m20.3782s -65d45m09.080s'
elif primary_tag == '1934':
    newphasecentre = 'J2000 19h39m25.0264s -63d42m45.624s'


fixvis(vis = myms,
    field = bpcal,
    phasecenter = newphasecentre,
    refcode = 'J2000',
    datacolumn = 'DATA')

