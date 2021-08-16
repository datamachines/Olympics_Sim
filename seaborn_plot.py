#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 17:00:22 2021

@author: ethan
"""
# import functions from related scripts
from fixed_vars import *
from get_plot_data import get_plot_data

# import proper packages
import matplotlib.pyplot as plt
import seaborn as sns

# plot density plots
fig = plt.figure()

sns.distplot(get_plot_data()[0], color='red', hist=False, rug=True)
sns.distplot(get_plot_data()[1], color='green', hist=False, rug=True)
sns.distplot(get_plot_data()[2], color='blue', hist=False, rug=True)

# plt.title("Tournament Structure Distributions ")
plt.xlabel("Percent of Competitions where Best Athlete Wins a Medal")
plt.ylabel("Density") 

fig.legend(labels=['Heats','Single Elimination Bracket', 'Round Robin'], loc=1,
           fancybox=True, framealpha=1, shadow=True, borderpad=1)
plt.show()