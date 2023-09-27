#!/usr/bin/python
"""
This module aims to plot various isochrones using data from the Padova database.
Input:
    File containing absolute magnitude in B and V (Mb and Mv, respectively)
Output:
    Graphs showing isochrones of stars at various ages, with x-axis Mb-Mv and y-axis Mv
Data set used:
    http://pleiadi.pd.astro.it/#data5
We used the solar enhanced, Z = 0.008 Y = 0.250 isochrones file.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = '../data/iso_jc_z008s_age_7.txt'

df = pd.read_csv(filename, sep='\t') # Reads file into Panda dataframe
df = df.dropna(axis=1, how='all') # Removes NaN column
print(df.head())

df["Mb_Mv"] = df["Mb"] - df["Mv"] # Defining Mb-Mv

df.plot.scatter(x="Mb_Mv", y="Mv", alpha=0.5) # Plotting the isochrone
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.show()