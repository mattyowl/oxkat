# ian.heywood@physics.ox.ac.uk


import pickle
import sys
import time
sys.path.append('oxkat')
from pickle_handler import get_project_info

execfile('oxkat/config.py')


def stamp():
    return str(time.time()).replace('.','')

myuvrange = ''

args = sys.argv
for item in sys.argv:
    parts = item.split('=')
    if parts[0] == 'mslist':
        mslist = parts[1].split(',')
    if parts[0] == 'uvmin':
        myuvrange = '>'+parts[1]


if myuvrange == '':
    myuvrange = '>150m'


project_info = get_project_info()
ref_ant = project_info['ref_ant']


for myms in mslist:


    clearstat()
    clearstat()


    gtab = GAINTABLES+'/cal_'+myms+'_'+stamp()+'.GP0'


    gaincal(vis=myms,
        field='0',
        uvrange=myuvrange,
        caltable=gtab,
        refant = str(ref_ant),
        solint='64s',
        solnorm=False,
        combine='',
        minsnr=3,
        calmode='p',
        parang=False,
        gaintable=[],
        gainfield=[],
        interp=[],
        append=False)


    applycal(vis=myms,
        gaintable=[gtab],
        field='0',
        calwt=False,
        parang=False,
        applymode='calonly',
        gainfield='0',
        interp = ['nearest'])


    # statwt(vis=myms,
    #     field='0')


    clearstat()
    clearstat()


