#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday Aug 3 12:28 2021

@author: Ethan

Olympic simulation:
    hold # of athletes and their associated skill level/ latent quality constant
    n_sims = 100
    draw distribution for # the best athlete wins
    in each of the different tournament structures

Swimming simulation: 
    Events have prelims, semis, & finals
    top 16 from prelims go to semis
    top 8 from semis go to the finals 

Simulation functions:


"""

import numpy as np


def heat(n_athletes, num_ath_per_heat):

    # total number of athletes
    list_of_athletes = list(range(n_athletes))

    # number of athletes in each heat
    num_per_heat = num_ath_per_heat

    # prelims = 4 heats
    ath_finished_prelims = []

    # heat 1 
    heat1_participants = np.random.choice(list_of_athletes, size=num_per_heat, replace=False)
    for athlete in heat1_participants:
        ath_finished_prelims.append(athlete)
    
    # heat 2
    heat2_participants = np.random.choice(np.array(list(set(heat1_participants) ^ set(list_of_athletes))),
                                          size=num_per_heat, replace=False)
    for athlete in heat2_participants:
        ath_finished_prelims.append(athlete)
        
    # heat 3 
    heat3_participants = np.random.choice(np.array(list(set(ath_finished_prelims) ^ set(list_of_athletes))),
                                          size=num_per_heat, replace=False)
    for athlete in heat3_participants:
        ath_finished_prelims.append(athlete)
        
    # heat 4 
    heat4_participants = np.random.choice(np.array(list(set(ath_finished_prelims) ^ set(list_of_athletes))),
                                          size=num_per_heat, replace=False)
    for athlete in heat4_participants:
        ath_finished_prelims.append(athlete)

    return ath_finished_prelims

def prelim_results(athletes_by_heat, num_ath_per_heat, athlete_avg_skill_level):
    participants = []
    times = []
    
    # run heat 1
    for i in range(num_ath_per_heat):
        participants.append(athletes_by_heat[i])
        times.append(np.random.normal(athlete_avg_skill_level[athletes_by_heat[i]], .3))
    
    # run heat 2
    for i in range(num_ath_per_heat, (num_ath_per_heat*2)):
        participants.append(athletes_by_heat[i])
        times.append(np.random.normal(athlete_avg_skill_level[athletes_by_heat[i]], .3))
        
    # run heat 3
    for i in range((num_ath_per_heat*2), (num_ath_per_heat*3)):
        participants.append(athletes_by_heat[i])
        times.append(np.random.normal(athlete_avg_skill_level[athletes_by_heat[i]], .3))
        
    # run heat 4
    for i in range((num_ath_per_heat*3), (num_ath_per_heat*4)):
        participants.append(athletes_by_heat[i])
        times.append(np.random.normal(athlete_avg_skill_level[athletes_by_heat[i]], .3))
        
        
    
    # heat participants by times
    prelim_result_list = [i for time, i in sorted(zip(times, participants))]
    prelim_winners = prelim_result_list[0:17]
    
    return prelim_winners

def semi_results(prelim_winners, num_ath_per_heat, athlete_avg_skill_level, semi_participants):
    ath_finished_semi = []
    # split into first and second semi-finals
    semifinals1 = np.random.choice(prelim_winners, size=num_ath_per_heat, replace=False)
    for athlete in semifinals1:
        ath_finished_semi.append(athlete)
        
    semifinals2 = np.random.choice(np.array(list(set(prelim_winners) ^ set(ath_finished_semi))),
                                          size=num_ath_per_heat, replace=False)
    for athlete in semifinals2:
        ath_finished_semi.append(athlete)
        
    # run semi-finals    
    semi_athletes = semi_participants
    times = []
    for i in range(len(semifinals1)):
        semi_athletes.append(semifinals1[i])
        times.append(np.random.normal(athlete_avg_skill_level[semifinals1[i]], .3))
        
    for i in range(len(semifinals2)):
        semi_athletes.append(semifinals2[i])
        times.append(np.random.normal(athlete_avg_skill_level[semifinals2[i]], .3))
    
    semi_result_list = [i for time, i in sorted(zip(times, semi_athletes))]
    semi_winners = semi_result_list[0:8]
    
    return semi_winners