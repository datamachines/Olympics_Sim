#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 11:19:03 2021

@author: ivy


heat simulation: 
    events have prelims, semis, & finals
    top 16 from prelims go to semis
    top 8 from semis go to the finals 

"""


import numpy as np
from sim_functions import *
from fixed_vars import *

def run_heat(n_athletes, athlete_avg_skill_level, num_ath_per_heat):
    # generate heats to be timed
    athletes_by_heat = heat_gen(n_athletes, num_ath_per_heat)
    # run preliminary heats      
    prelim_winners = prelim_results(athletes_by_heat, num_ath_per_heat, athlete_avg_skill_level)
    # run semi-final heats
    semi_participants = [] # declared outside of semi_results() because final_results() also needs this array
    semi_winners = semi_results(prelim_winners, num_ath_per_heat, athlete_avg_skill_level, semi_participants)
    # determine final heat results 
    medalists = final_results(semi_winners, semi_participants, athlete_avg_skill_level)
    
    return medalists
    
















