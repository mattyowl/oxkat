"""

CASA scripts expect pickle protocol 2 - but even if written that way in python3, we need to
handle the bytes / unicode strings issue. The routine in here should be a drop in replacement
for everywhere project_info is loaded from the pickle file in oxkat.

"""

import pickle

def convert_list(list_to_convert):
    new_list=[]
    for item in list_to_convert:
        if type(item) == unicode:
            new_list.append(str(item))
        elif type(item) == tuple:
            new_list.append(convert_tuple(item))
        elif type(item) == list:
            new_list.append(convert_list(item))
        else:
            new_list.append(item)
    return new_list

def convert_tuple(tuple_to_convert):
    new_list=convert_list(tuple_to_convert)
    return tuple(new_list)

def get_project_info():
    project_info = load_pickle('project_info.p')
    return project_info
    
def load_pickle(pickle_file_name):
    pickle_file=open(pickle_file_name, 'rb')
    project_info = pickle.load(pickle_file)
    try:
        new_dict={}
        for key in project_info.keys():
            item=project_info[key]
            if type(item) == list:
                new_dict[str(key)]=convert_list(item)
            elif type(item) == tuple:
                new_dict[str(key)]=convert_tuple(item)
            elif type(project_info[key]) == unicode:
                new_dict[str(key)]=str(item)
        project_info=new_dict
    except:
        pass # If we get here, hopefully we're on python3 ...
    pickle_file.close()
    return project_info

# Testing
#get_project_info()
