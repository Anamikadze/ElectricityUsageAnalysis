#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:53:20 2023

@author: anano
"""

import pandas as pd
def print_groups(hh, group_vars): #the function takes two arguements: 
#  hh = dataframe of household info and group_vars used to group data
    grouped = hh.groupby(group_vars) # groups data by group_vars
    med = grouped["etr"].median().round(2) #calculates median on grouped etr and rounds it
    print(med)
    return med

hh = pd.read_csv("households.csv", index_col='id') #reads household file, 
#sets index to id and stores it in hhq
q = pd.read_csv("quantities.csv", index_col='id')
hh["quint"] = pd.qcut(hh["inc"], 5, labels=[1,2,3,4,5]) #determines income quintile
#for everyhousehold in households.csv

pd1 = 53.35
pd2 = 55.27
dp = pd2 -pd1
hh["etr"] = dp * 100 * q["qd2"] / hh["inc"] #calculates ETR for everyhousehold Check:print(hh["etr"])

#how can we save that dataframe?

#%%
med_q = print_groups(hh, ["quint"]) 
med_t = print_groups(hh, ["type"])
med_b = print_groups(hh, ["type", "quint"])

#%%
print(med_b.index)

#%%
print("Detailed Medians for Type 3 Households")
print(med_b.xs(3, level="type")) #the arguements show that level, in this case type is 3

print("Medians for the 5th quintile:")
print(med_b.xs(5, level="quint"))

#%%
etr_lowest = med_b.xs(1, level = "quint")
print(etr_lowest)
#%%

etr_change = med_b - etr_lowest
print(etr_change) #difference in ETR for each type and 
#quintile from ETR from quintile 1 of the same type 
#That is why every first quintile parameter in each type is 0.00
