#!/usr/bin/python
%matplotlib inline

from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

STELLAR_LIB_FILENAME = r'../Hipparcos/I_239_selection.tsv'

def load_stellar_lib(filename): #this function largely contains some commands from "http://balbuceosastropy.blogspot.com/2014/03/construction-of-hertzsprung-russell.html"
    df = pd.read_table(filename, skiprows=44, sep=';', header=None, index_col=0,
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