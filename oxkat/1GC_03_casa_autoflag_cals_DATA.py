# ian.heywood@physics.ox.ac.uk


import pickle
sys.path.append('oxkat')
from pickle_handler import get_project_info

# with open('project_info.p','rb') as f:
#     project_info = pickle.load(f,encoding='latin1')


#project_info = pickle.load(open('project_info.p','rb'))
project_info = get_project_info()

myms = project_info['master_ms']
bpcal = project_info['primary']
pcals = project_info['secondary']


clearstat()
clearstat()


flagdata(vis=myms,mode='rflag',datacolumn='data',field=bpcal[1])
flagdata(vis=myms,mode='tfcrop',datacolumn='data',field=bpcal[1])
flagdata(vis=myms,mode='extend',growtime=90.0,growfreq=90.0,growaround=True,flagneartime=True,flagnearfreq=True,field=bpcal[1])

for i in range(0,len(pcals)):
    pcal = pcals[i][1]
    if bpcal[1] != pcal: # avoid double flagging of primary
        flagdata(vis=myms,mode='rflag',datacolumn='data',field=pcal)
        flagdata(vis=myms,mode='tfcrop',datacolumn='data',field=pcal)
        flagdata(vis=myms,mode='extend',growtime=90.0,growfreq=90.0,growaround=True,flagneartime=True,flagnearfreq=True,field=pcal)


flagmanager(vis=myms,mode='save',versionname='autoflag_cals_data')


clearstat()
clearstat()
