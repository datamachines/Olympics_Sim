#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:00:22 2021

@author: ivy

Get simulation results

What is the distribution of how often the top athlete wins a medal, 
given a specific tournament structure?
"""

from fixed_vars import *
from slingle_elim_brack import *
from round_robins import *
from sim_functions import *

n_sims = [] 

 
def run_sims(n_sims, n_athletes, heat_or_group_size, best_athlete_pre_oly):
    did_fastest_person_win = []
    for sim in range(n_sims):
        # tournament = the func pulled from one of the tournament.py files to run a tournament structure
        # each tournament should output the top three finishers (the medal winners)
        top_three = tournament(n_athletes, heat_or_group_size)
        
        if best_athlete_pre_oly in top_three:
            did_fastest_person_win.append(1)
        else:
            did_fastest_person_win.append(0)
                
    return did_fastest_person_win