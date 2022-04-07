#!/usr/bin/env python
# ian.heywood@physics.ox.ac.uk


import json


def str_iterator(inlist):
	xx = []
	for yy in inlist:
		xx.append(str(yy))
	return xx


with open('project_info.json') as f:
	project_info = json.load(f)

myms = str(project_info['working_ms'])
band = str(project_info['band'])
nchan = int(project_info['nchan'])
ref_ant = str(project_info['ref_ant'])
bpcal = str(project_info['primary_id'])
bpcal_name = str(project_info['primary_name'])
primary_tag = str(project_info['primary_tag'])
pcal_names = str_iterator(project_info['secondary_names'])
pcals = str_iterator(project_info['secondary_ids'])
pcal_dirs = project_info['secondary_dirs']
target_names = str_iterator(project_info['target_names'])
targets = str_iterator(project_info['target_ids'])
target_dirs = project_info['target_dirs']
target_cal_map = str_iterator(project_info['target_cal_map'])
target_ms = str_iterator(project_info['target_ms'])

