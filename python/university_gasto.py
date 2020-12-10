#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:17:02 2020

@author: yalinghu
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/Users/yalinghu/Desktop/dataproject')
os.getcwd()

uni_gasto = pd.read_csv('university_gasto.csv',sep=',', decimal='.')

# Categoriza el gasto total a tres niveles (precio alquier + precio credito)
x=uni_gasto.gasto
res = x.describe()

m=res[1]
sd=res[2]
n=res[0]
plt.hist(x, bins=10, edgecolor='black', color='yellow')
plt.xticks(np.arange(15, 60, 5))
plt.title('Figure 1. Cost level defined by credit price of University' '\n' 'and renting price per m2')
plt.ylabel('Frecuency')
plt.xlabel('Cost level')
props = dict(boxstyle='round', facecolor = 'white', lw = 0.5)
textstr = '$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$'%(m, sd, n)
plt.text (47,570, textstr, bbox = props)
plt.axvline (x=m,
             linewidth=1,
             linestyle='solid',
             color='red', label='Mean')
plt.axvline (x=m-sd,
             linewidth=1,
             linestyle='dashed',
             color='green', label='-1 S.D.')
plt.axvline (x=m+sd,
             linewidth=1,
             linestyle='dashed',
             color='green', label='+1 S.D.')
plt.savefig('Figure_1.png')
plt. legend(loc='upper left', bbox_to_anchor=(0.72, 0.7))


uni_gasto_c = uni_gasto

uni_gasto.loc[ (uni_gasto['gasto']<=(m-sd)), "gasto_cat"] = "Low"   
uni_gasto.loc[((uni_gasto['gasto']<(m+sd)) & (uni_gasto['gasto']>(m-sd))), "gasto_cat"] = "Medium"
uni_gasto.loc[ (uni_gasto['gasto']>=(m+sd)), "gasto_cat"] = "High" 

uni_gasto.to_csv("uni_gasto_category.csv")





# Sacar media y sd de las dos variables (precio alquier, precio credito)
y=uni_gasto.precio_credito
res1 = y.describe()
m=res1[1]
sd=res1[2]
n=res1[0]
plt.hist(y, bins=10, edgecolor='black', color='yellow')
plt.xticks(np.arange(8, 40, 5))
plt.title('Figure 2. Cost level of per credit price' '\n' '')
plt.ylabel('Frecuency')
plt.xlabel('Cost level')
props = dict(boxstyle='round', facecolor = 'white', lw = 0.5)
textstr = '$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$'%(m, sd, n)
plt.text (30,570, textstr, bbox = props)
plt.axvline (x=m,
             linewidth=1,
             linestyle='solid',
             color='red', label='Mean')
plt.axvline (x=m-sd,
             linewidth=1,
             linestyle='dashed',
             color='green', label='-1 S.D.')
plt.axvline (x=m+sd,
             linewidth=1,
             linestyle='dashed',
             color='green', label='+1 S.D.')
plt.savefig('Figure_2.png')




z=uni_gasto.precio_alquiler
res2 = z.describe()

m=res2[1]
sd=res2[2]
n=res2[0]
plt.hist(z, bins=10, edgecolor='black', color='yellow')
plt.xticks(np.arange(6, 16, 2))
plt.title('Figure 3. Cost level of renting price' '\n' '')
plt.ylabel('Frecuency')
plt.xlabel('Cost level')
props = dict(boxstyle='round', facecolor = 'white', lw = 0.5)
textstr = '$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$'%(m, sd, n)
plt.text (12,420, textstr, bbox = props)
plt.axvline (x=m,
             linewidth=1,
             linestyle='solid',
             color='red', label='Mean')
plt.axvline (x=m-sd,
             linewidth=1,
             linestyle='dashed',
             color='green', label='-1 S.D.')
plt.axvline (x=m+sd,
             linewidth=1,
             linestyle='dashed',
             color='green', label='+1 S.D.')
plt.savefig('Figure_3.png')






























