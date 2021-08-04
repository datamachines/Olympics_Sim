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
from fixed_vars import *
## set seed for dev, remove it for actual simulation 
# import random
# random.seed(10)

# here, we set up a data structure to hold per-competition statistics we care about
did_fastest_person_win = []
for sim in range(n_sims):

    # generate heats to be timed
    athletes_by_heat = heat_gen(n_athletes, num_ath_per_heat)
    # run preliminary heats      
    prelim_winners = prelim_results(athletes_by_heat, num_ath_per_heat, athlete_avg_skill_level)
    # run semi-final heats
    semi_participants = [] # declared outside of semi_results() because final_results() also needs this array
    semi_winners = semi_results(prelim_winners, num_ath_per_heat, athlete_avg_skill_level, semi_participants)
    # determine final heat results 
    final_winners = final_results(semi_winners, semi_participants, athlete_avg_skill_level)

    # tally Gold Medals    
    if final_winners[0] == 24:
        did_fastest_person_win.append(1)
    else:
        did_fastest_person_win.append(0)
    
    
# print results after 100 simulations   
print ("The fastest swimmer won the gold: ", did_fastest_person_win.count(1), " times")
















