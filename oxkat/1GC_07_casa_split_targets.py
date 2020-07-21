# ian.heywood@physics.ox.ac.uk


<<<<<<< HEAD:oxkat/1GC_08_casa_split_targets.py
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
=======

execfile('oxkat/casa_read_project_info.py')


for i in range(0,len(targets)):
    target = targets[i]
    opms = target_ms[i]
>>>>>>> master:oxkat/1GC_07_casa_split_targets.py


    mstransform(vis=myms,
        outputvis=opms,
        field=target,
        usewtspectrum=True,
        realmodelcol=True,
        datacolumn='corrected')


    flagmanager(vis=opms,
        mode='save',
        versionname='post-1GC')
