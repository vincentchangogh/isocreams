#!/usr/bin/python
%matplotlib inline

#have this module exisiting in the same directory this __init__ file before using this script
import read_mist_models

from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#the two filename variables below require the directory path to be prefixed to the speicified file name.
STELLAR_LIB_FILENAME = r'../Hipparcos/I_239_selection.tsv'
ISOCRHRONE_FILENAME=r"...\isocreams\ISOCHRONE_DATA.cmd"

def load_stellar_lib(filename): #this function largely contains some commands from "http://balbuceosastropy.blogspot.com/2014/03/construction-of-hertzsprung-russell.html"
    df = pd.read_table(filename, skiprows=52, sep=';', header=None, index_col=0,
                       names = ['HIP', 'Vmag', 'Plx', 'B-V', 'SpType'],
                       skipfooter=1, engine='python')
    
    df_clean = df.applymap(lambda x: np.nan if isinstance(x, basestring)
                       and x.isspace() else x)
    df_clean= df_clean.dropna()
    df_clean['Vmag'] = df_clean['Vmag'].astype(np.float)
    df_clean['Plx'] = df_clean['Plx'].astype(np.float)
    df_clean['B-V'] = df_clean['B-V'].astype(np.float)
    # Add a new column with the absolute magnitude
    df_clean['M_V'] = df_clean['Vmag'] + 5 * np.log10(df_clean['Plx']/100.)

def load_isochrones(filename):
    # file used pn local device test <r"C:\Users\kdror\Documents\PhD year 1\python learning of PhD year 1\python September workshop\group_proj_repository\isocreams\iso_jc_z008s.csv">
    isochrone_table=pd.read_csv(filename,sep="\s+|s+",index_col=False)
    return isochrone_table

def plot_isochrones_vs_stars():
    for age in np.unique() #we need to separate isochrones