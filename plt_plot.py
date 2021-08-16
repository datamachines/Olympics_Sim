#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 6 17:00:22 2021

@author: ethan
"""
# import functions from related scripts
from fixed_vars import *
from get_plot_data import get_plot_data

# import proper packages
import matplotlib.pyplot as plt
import numpy as np

# percentages plot with  means

labels = ['Heat', 'Single Elimination', 'Round Robin', 'Heat Mean %', 'Single Elim Mean %', 'Round Robin Mean %']
mean_heat = np.mean(get_plot_data()[0])
mean_single = np.mean(get_plot_data()[1])
mean_robin = np.mean(get_plot_data()[2])
x = range(1, 101) # range to track each iteration of 100 simulations
plt.plot(x, get_plot_data()[0], color = 'red')
plt.plot(x, get_plot_data()[1], color = 'green')
plt.plot(x, get_plot_data()[2], color = 'blue')
# plotting dotted mean lines 
plt.hlines(mean_heat, x[0], x[len(x)-1], label='Heat Mean', linestyles='dashed', colors = 'red')
plt.hlines(mean_single, x[0], x[len(x)-1], label='Single Elim Mean', linestyles='dashed', colors = 'green')
plt.hlines(mean_robin, x[0], x[len(x)-1], label='Round Robin Mean', linestyles='dashed', colors = 'blue')
plt.legend(labels, loc = 'center left', bbox_to_anchor=(0.92, 1))
plt.xlabel('Number of Simulations Run (100 at each iteration)')
plt.ylabel('Percent of Simulations that Best Athlete Won')
plt.title('Number of Times the Best Athlete Won a Medal')
plt.show()