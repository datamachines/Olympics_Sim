#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:00:22 2021

@author: ivy


Olympic simulation:
    
    hold # of athletes and their associated skill level/ latent quality constant
    n_sims = 100
    draw distribution for # the best athlete wins
    in each of the different tournament structures
    
    
Get simulation results:

    What is the distribution of how often the top athlete wins a medal, 
    given a specific tournament structure?
    
"""

from fixed_vars import *

from heat_functions import *
from single_elim_sim import *
from round_robins import *


'''
heat simulation: 
    
    events have prelims, semis, & finals
    top 16 from prelims go to semis
    top 8 from semis go to the finals 
    
this tournament structure appears in the olympics for swimming and track events
    
'''

def run_heat_sims(n_sims, n_athletes, athlete_avg_skill_level, num_ath_per_heat, fastest_athlete_pre_oly):
    did_best_athlete_win = []
    for sim in range(n_sims):
        medalists = run_heat(n_athletes, athlete_avg_skill_level, num_ath_per_heat)
        
        if fastest_athlete_pre_oly in medalists:
            did_best_athlete_win.append(1)
        else:
            did_best_athlete_win.append(0)
                    
    return did_best_athlete_win



''' 
single elimination bracket simulation:
    
    all the athletes get paired up to play a game
    the winner moves onto play again
    the final team/player to make it all the way to the end, without losing a single match, wins the gold
    the runner-up wins silver
    the losers of the quarter final matches get to move into the bronze bracket
    and compete for the bronze medal
    
this tournament structure appears in the olympics for fencing


'''

def run_single_elim_brac_sims(n_sims, n_athletes, athlete_avg_skill_level, best_athlete_pre_oly):
    did_best_athlete_win = []
    for sim in range(n_sims):
        
        # run single elim bracket 
        medalists = run_sin_elim_bracket(n_athletes, athlete_avg_skill_level)
        
        if best_athlete_pre_oly in medalists:
            did_best_athlete_win.append(1)
        else:
            did_best_athlete_win.append(0)
                
    return did_best_athlete_win


'''
round robins simulation: 
    
    the starting # of teams (in this case 32) are broken into groups/pools (8 groups of 4 teams).
    each team then plays every other team in their group (6 games per groups).
    teams get a point for each game won, and the top two teams from each pool move onto a
    single elimination bracket.

this tournament structure appears in the olympics for soccer, basketball, and beach volleyball

'''


def run_roundrobin_sims(n_sims, athlete_avg_skill_level, best_athlete_pre_oly):
    did_best_athlete_win = []
    for sim in range(n_sims):

        # run round robins sim
        medalists = run_roundrobin(list_of_athletes, athlete_avg_skill_level, poolsize)
        
        if best_athlete_pre_oly in medalists:
            did_best_athlete_win.append(1)
        else:
            did_best_athlete_win.append(0)
                
    return did_best_athlete_win

# Running each function and printing the output

# print ("------------------- Heat Simulations -------------------")
# print (run_heat_sims(n_sims, n_athletes, athlete_avg_skill_level, fastest_athlete_pre_oly))
# print ("-------------- Single Elimination Brackets -------------")
# print (run_single_elim_brac_sims(n_sims, n_athletes, athlete_avg_skill_level, best_athlete_pre_oly))
# print ("---------------------- Round Robins ---------------------")
# print (run_roundrobin_sims(n_sims, athlete_avg_skill_level, best_athlete_pre_oly))