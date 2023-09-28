#!/usr/bin/python

#have this module exisiting in the same directory this __init__ file before using this script

#from __future__ import division
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
    return df_clean

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
    isochrone_table=pd.read_csv(filename,sep="\s+|s+",index_col=False,engine="python")
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

def isochrone_fitting(isochrone_dict,data):
    for model in list(isochrone_dict.keys()):
        for star in 

def star_and_isochrone_plotter(stellar_lib,isochrones_dictionary)
    df_clean=stellar_lib

    # Rows that do not meet the condition alpha + num are eliminated
    f = lambda s: (len(s) >= 2)  and (s[0].isalpha()) and (s[1].isdigit())
    i  = df_clean['SpType'].apply(f)
    df_clean = df_clean[i]

    # A new column is created with the first two characters from 'SpType'
    f = lambda s: s[0:2]
    df_clean['SpType2'] = df_clean['SpType'].apply(f)

    # Remove the lines containing special classes C, N, R, S
    f = lambda s: s[0] in 'OBAFGKM'
    df_clean = df_clean[df_clean['SpType'].map(f)]

    f = lambda s: s[0]
    clases = df_clean['SpType'].map(f)

    # Replace the letters with digits because we want them to appear in
    # a certain order
    orden = {'O':'0', 'B':'1', 'A':'2', 'F':'3', 'G':'4', 'K':'5', 'M':'6'}
    f = lambda s: orden[s[0]]+s[1]
    df_clean['SpType2'] = df_clean['SpType2'].apply(f)

    # Plot the stars, with different star classes in different colours
    def plot_lum_class(b,c, label):
        ''' b: boolean Series to make the selection
            c: Color
            label: for the legend
        '''
        x = df_clean['B-V'][b]
        y = df_clean['M_V'][b]
        ax.scatter(x, y, c = c, s=6, edgecolors='none', label = label)

    fig = plt.figure(figsize=(8,10))
    ax = fig.add_subplot(111)

    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(15, -15)
    ax.grid()
    ax.set_title('H-R Diagram \n (Hipparcos catalog)')

    ax.title.set_fontsize(20)
    ax.set_xlabel('Color index B-V')
    ax.xaxis.label.set_fontsize(20)
    ax.set_ylabel('Absolute magnitude')
    ax.yaxis.label.set_fontsize(20)

    f = lambda s: 'VII' in s
    b = df_clean['SpType'].map(f)
    plot_lum_class(b,'green', 'VII: white dwarfs')

    f = lambda s: ('VI' in s) and ('VII' not in s)
    b = df_clean['SpType'].map(f)
    plot_lum_class(b,'blue', 'VI: subdwarfs')

    f = lambda s: ('V' in s) and ('VI' not in s) and ('IV' not in s)
    b = df_clean['SpType'].map(f)
    plot_lum_class(b,'black', 'V: main-sequence')

    f = lambda s: 'IV' in s
    b = df_clean['SpType'].map(f)
    plot_lum_class(b,'grey', 'IV: subgiants')

    f = lambda s: 'III' in s
    b = df_clean['SpType'].map(f)
    plot_lum_class(b,'orange', 'III: giants')

    f = lambda s: ('II' in s) and ('III' not in s) and ('VII' not in s)
    b = df_clean['SpType'].map(f)
    plot_lum_class(b,'yellow', 'II: bright giants')

    f = lambda s: ('I' in s) and ('II' not in s) and ('V' not in s)
    b = df_clean['SpType'].map(f)
    plot_lum_class(b,'red', 'I: supergiants')

    ax.tick_params(axis='both', labelsize=14)
    legend = ax.legend(scatterpoints=1,markerscale = 6, shadow=True)
    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    for isochrone in list(isochrones_dictionary.keys()):
        plt.plot(isochrones_dictionary[isochrone]["M_b"]-isochrones_dictionary[isochrone]["M_v"],isochrones_dictionary[isochrone]["M_y"],label=isochrone)
    plt.show()