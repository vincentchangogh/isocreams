#!/usr/bin/python

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
    r"""Summarize the function in one line.

    imports data from a single padova isochrone file into one dictionary

    Parameters
    ----------
    filepath : string
        the directory + filename that your padova isochrone file is stored under (eg:"myfiles/isochrones/isochrone_file.dat")

    Returns
    -------
    pandas dataframe
        this contains the data loaded from your padova isochrone file.

    See Also
    --------
        the files loaded by this code are downloaded from <http://pleiadi.pd.astro.it/> (from the"solar_scaled" option). "iso_jc_z008s.dat" were used for testing. 
        This file must be separated out into numerous smaller files to be managed by this command: each file may only contain one header: the hashtag from this header must
        be removed, and only one line of said header (the line specifying the name of each column) may be kept

    References
    ----------
        padova isochrones from <http://pleiadi.pd.astro.it/>
    """
    # file used pn local device test <r"C:\Users\kdror\Documents\PhD year 1\python learning of PhD year 1\python September workshop\group_proj_repository\isocreams\iso_jc_z008s.csv">
    isochrone_table=pd.read_csv(filename,sep="\s+|s+",index_col=False)
    return isochrone_table

def load_multiple_isochrones(filepath,filenames):
    r"""Summarize the function in one line.

    imports data from a number of padova isochrone files into one dictionary

    Parameters
    ----------
    filepath : string
        the directory that your padova isochrones are stored in. Ensure that this string ends in a slash character, such that filepath+filename[0] points to a specific file.
    filenames : list
        a list of strings, where each string is the name of one of your padova isochrone files

    Returns
    -------
    dictionary
        this dictionary contains pandas dataframes loaded for each file specified in "filenames": each dataframe is stored under a key equal to the dataframe's corresponding filename

    Raises
    ------
    FileNotFoundError
        This can be raised mostl easliy if your input "filepath" doesn't end in a slash character

    See Also
    --------
        the files loaded by this code are downloaded from <http://pleiadi.pd.astro.it/> (from the"solar_scaled" option). "iso_jc_z008s.dat" were used for testing. 
        This file must be separated out into numerous smaller files to be managed by this command: each file may only contain one header: the hashtag from this header must
        be removed, and only one line of said header (the line specifying the name of each column) may be kept

    References
    ----------
        padova isochrones from <http://pleiadi.pd.astro.it/>
    """
    isochrones_dictionary={}
    for filename in filenames:
        isochrones_dictionary[filename]=load_isochrones(filepath+filename)
    return isochrones_dictionary
