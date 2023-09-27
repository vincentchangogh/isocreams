#!/usr/bin/python
"""
This module aims to plot various isochrones using data from the Padova database.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = '../data/iso_jc_z008s_age_7.txt'

df = pd.read_csv(filename, sep='\t') # Reads file into Panda dataframe
df = df.dropna(axis=1, how='all') # Removes NaN column
print(df.head())

df["Mb_Mv"] = df["Mb"] - df["Mv"]

df.plot.scatter(x="Mb_Mv", y="Mv", alpha=0.5)
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])
plt.show()