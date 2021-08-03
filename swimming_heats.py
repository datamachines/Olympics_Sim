#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 11:19:03 2021

@author: ivy

Olympic simulation:
    hold # of athletes and their associated skill level/ latent quality constant
    n_sims = 100
    draw distribution for # the best athlete wins
    in each of the different tournament structures

Swimming simulation: 
    Events have prelims, semis, & finals
    top 16 from prelims go to semis
    top 8 from semis go to the finals 

"""


import numpy as np
from sim_functions import *
## set seed for dev, remove it for actual simulation 
# import random
# random.seed(10)

# athletes have a latent quality
n_athletes = 32
athlete_avg_skill_level = np.random.uniform(0, 1, n_athletes)
num_ath_per_heat = 8
# run competition simulation
n_sims = 100
# here, we set up a data structure to hold per-competition statistics we care about
did_fastest_person_win = []
for sim in range(n_sims):

    athletes_by_heat = heat(n_athletes, num_ath_per_heat)
          
    
    prelim_winners = prelim_results(athletes_by_heat, num_ath_per_heat, athlete_avg_skill_level)
    
    semi_participants = []
    
    semi_winners = semi_results(prelim_winners, num_ath_per_heat, athlete_avg_skill_level, semi_participants)
        
    
    # run the finals
    finals_participants = []
    times = []
    for i in range(len(semi_winners)):
        finals_participants.append(semi_winners[i])
        times.append(np.random.normal(athlete_avg_skill_level[semi_winners[i]], .3))
        
    final_result_list = [i for time, i in sorted(zip(times, semi_participants))]
    final_winners = final_result_list[0:3]
        
    if final_winners[0] == 24:
        did_fastest_person_win.append(1)
    else:
        did_fastest_person_win.append(0)
    
    
    
print ("The fastest swimmer won the gold: ", did_fastest_person_win.count(1), " times")
















