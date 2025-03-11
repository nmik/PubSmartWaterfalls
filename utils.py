#!/usr/bin/env python                                                          #
#                                                                              #
# Autor: Michela Negro, GSFC/CRESST/UMBC                                       #
#        Nicolo' Cibrario, Torino University                                  #
# This program is free software; you can redistribute it and/or modify         #
# it under the terms of the GNU General Public License as published by         #
# the Free Software Foundation; either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
#------------------------------------------------------------------------------#


"""general parsing functions.
"""

import os
import numpy as np
from matplotlib import pyplot as plt
import astropy.io.fits as pf

WATERFALL_DICT = {'Long_hard': {'cmap': 'Reds', 'title': 'Long (hard)'},
                  'Long_norm': {'cmap': 'Greens', 'title': 'Long (norm)'},
                  'Long_soft': {'cmap': 'Blues', 'title': 'Long (soft)'},
                  'Long_blackbody': {'cmap': 'Greys', 'title': 'Long (BB)'},
                  'Med_hard':  {'cmap': 'Reds', 'title': 'Med (hard)'}, 
                  'Med_norm':  {'cmap': 'Greens', 'title': 'Med (norm)'},
                  'Med_soft':  {'cmap': 'Blues', 'title': 'Med (soft)'},
                  'Med_blackbody':  {'cmap': 'Greys', 'title': 'Med (BB)'},
                  'Short_hard': {'cmap': 'Reds', 'title': 'Short (hard)'}, 
                  'Short_norm': {'cmap': 'Greens', 'title': 'Short (norm)'},
                  'Short_soft': {'cmap': 'Blues', 'title': 'Short (soft)'},
                  'Short_blackbody': {'cmap': 'Greys', 'title': 'Short (BB)'}}

def parse_grb_files(file_folder_path, grb_file):
    """
    Parsing of the GRB*.npy files.
    
    Parameters
    ----------
    file : str
        npy file for a GRB.
    
    Returns
    -------
    array 
       set of 12 waterfall images: (12, N, M)
    """
    
    name = grb_file.replace('.npy', '')
    f = np.load(file_folder_path+grb_file)
    
    return name, f

def load_grb_images_from_list(file_folder_path, grb_name_list):
    """
    Parsing of the GRB*.npy files.
    
    
    Parameters
    ----------
    file_folder_path : str
        file path to GRB*.npy files.
    grb_name_list : str
        List of names of the GRB*.npy files.
        
    Returns
    -------
    array
        set of images.
    """
    
    names_ = []
    grb_images_ = []
    for grbname in grb_name_list:
        filename = grbname+'.npy'
        try:
            name, f = parse_grb_files(file_folder_path, filename)
            grb_images_.append(f)
            names_.append(name)
        except:
            print('Error in loading file:', filename)
            pass
    return np.array(names_), grb_images_

def load_grb_images(file_folder_path):
    """
    Parsing of the GRB*.npy files.
    
    
    Parameters
    ----------
    file_folder_path : str
        file path to GRB*.npy files.
        
    Returns
    -------
    array
        set of images.
    """
    
    names_ = []
    grb_images_ = []
    for filename in os.listdir(file_folder_path):
        try:
            name, f = parse_grb_files(file_folder_path, filename)
            grb_images_.append(f)
            names_.append(name)
        except:
            pass
    return np.array(names_), grb_images_