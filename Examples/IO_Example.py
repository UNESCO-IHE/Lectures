# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:36:37 2015

@author: juan

Reading csv files in 3 ways
"""
csvfile = 'xy_catchment.csv'
csv_write_file = 'dummy.csv'
## Standard way
a = []
with open(csvfile, 'r') as f:
    f.next()
    for lines in f:
        a.append((float(lines.split(',')[1]), float(lines.split(',')[2][:-2])))

#%%
## using csv libraries
import csv
b = []
with open(csvfile, 'r') as f:
    gg = csv.reader(f)
    gg.next()
    for elem in gg:
        b.append((float(elem[1]), float(elem[2])))

#%% using numpy
import numpy as np
c = np.loadtxt(csvfile, delimiter=',', usecols=[1,2], skiprows=1)



# Writing files

#%% Standard way
with open(csv_write_file, 'wb') as f:
    for lines in a:
        f.write((str(lines[0])+', '+str(lines[1])+'\n'))

#%% using CSV libraries

with open(csv_write_file, 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(b)


#%% Using numpy
np.savetxt(csv_write_file, c, fmt='%.4f')