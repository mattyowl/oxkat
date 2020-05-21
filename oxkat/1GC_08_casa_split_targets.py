# ian.heywood@physics.ox.ac.uk


import pickle
sys.path.append('oxkat')
from pickle_handler import get_project_info

#project_info = pickle.load(open('project_info.p','rb'))
project_info = get_project_info()

myms = project_info['master_ms']
targets = project_info['target_list'] 


for targ in targets:
    target = targ[1]
    opms = targ[2]


    mstransform(vis=myms,
        outputvis=opms,
        field=target,
        usewtspectrum=True,
        realmodelcol=True,
        datacolumn='corrected')


    flagmanager(vis=opms,
        mode='save',
        versionname='post-1GC')
