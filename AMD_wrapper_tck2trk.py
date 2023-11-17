#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:58:55 2023

@author: ali
"""


import os , glob, shutil
import sys, subprocess
#import nibabel as nib

try :
    BD = os.environ['BIGGUS_DISKUS']
#os.environ['GIT_PAGER']
except KeyError:  
    print('BD not found locally')
    BD = '/mnt/munin6/Badea/Lab/mouse'    
    #BD ='/Volumes/Data/Badea/Lab/mouse'
else:
    print("BD is found locally.")
#create sbatch folder

#perm_folder = BD+"/mrtrix_amd/perm_files"

#dwi_path = '/Volumes/Data/Badea/Lab/jacques/AMD_data/'
#dwis = os.listdir(dwi_path)
#dwis = [i for i in dwis if 'dwi' in i]
#dwis = sorted(dwis)

list_folders_path_orig = '+++++mouse/mrtrix_amd/perm_files/'
list_folders_path = os.listdir(list_folders_path_orig)
#list_of_masks= [i for i in list_folders_path if 'mask.nii.gz' in i]
#list_of_subjs = [i.partition('_mask.nii.gz')[0] for i in list_of_masks]
list_of_tracts= [i for i in list_folders_path if '2mill' in i]

#list_of_masks = sorted(list_of_masks)
list_of_tracts = sorted(list_of_tracts)
#list_of_subjs = sorted(list_of_subjs)

output_folder = ' ++++/mretrix_amd/AMD_trk'
tck_temp_folder = '++++/amd_trcks/'
dusom = '+++/Nariman_mrtrix_amd/amd_trcks/'

for i,_ in enumerate (list_of_tracts):
#     if dwis[i].partition('_mask.nii.gz')[0] in list_of_tracts[i] and list_of_subjs[i] in list_of_tracts[i]:  
    tck_temp_path = os.path.join(tck_temp_folder, list_of_tracts[i])
    output_path = os.path.join(tck_temp_folder, list_of_tracts[i].replace('.tck','.trk'))
    
    #if not os.path.exists(output_path):
        
    #if not os.path.exists(dusom + list_of_tracts[i]):
    #    shutil.copy(list_of_tracts[i], tck_temp_path)
    subj = list_of_tracts[i].partition('_smallerTracks')[0]
    mask_path = os.path.join(list_folders_path_orig,f'{subj}_mask.nii.gz')
    command_paths = (f"python ++++/mretrix_amd/tck2trk.py {mask_path} {tck_temp_path}")
    print(command_paths)
    #os.system("python /Users/ali/Desktop/Mar23/mretrix_amd/tck2trk.py "+ command_paths)
    os.system(command_paths)
    if os.path.exists(output_path) and os.path.exists(tck_temp_path):
        os.remove(tck_temp_path)
    #else:
    #    print(f'Already wrote {output_path}')
