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
## set seed for dev, remove it for actual simulation 
# import random
# random.seed(10)

# athletes have a latent quality
n_athletes = 32
athlete_avg_skill_level = np.random.uniform(0, 1, n_athletes)

# run competition simulation
n_sims = 100
# here, we set up a data structure to hold per-competition statistics we care about
did_fastest_person_win = []
for sim in range(n_sims):

    # here is an entire competition:
    list_of_athletes = list(range(32))
    
    # prelims = 4 heats
    ath_finished_prelims = []
    
    # heat 1 
    heat1_participants = np.random.choice(list_of_athletes, size=8, replace=False)
    for athlete in heat1_participants:
        ath_finished_prelims.append(athlete)
    
    # heat 2
    heat2_participants = np.random.choice(np.array(list(set(heat1_participants) ^ set(list_of_athletes))),
                                          size=8, replace=False)
    for athlete in heat2_participants:
        ath_finished_prelims.append(athlete)
        
    # heat 3 
    heat3_participants = np.random.choice(np.array(list(set(ath_finished_prelims) ^ set(list_of_athletes))),
                                          size=8, replace=False)
    for athlete in heat3_participants:
        ath_finished_prelims.append(athlete)
        
    # heat 4 
    heat4_participants = np.random.choice(np.array(list(set(ath_finished_prelims) ^ set(list_of_athletes))),
                                          size=8, replace=False)
    for athlete in heat4_participants:
        ath_finished_prelims.append(athlete)
        
    
    
    
    participants = []
    times = []
    
    # run heat 1
    for i in range(len(heat1_participants)):
        participants.append(heat1_participants[i])
        times.append(np.random.normal(athlete_avg_skill_level[heat1_participants[i]], .3))
    
    # run heat 2
    for i in range(len(heat2_participants)):
        participants.append(heat2_participants[i])
        times.append(np.random.normal(athlete_avg_skill_level[heat2_participants[i]], .3))
        
    # run heat 3
    for i in range(len(heat3_participants)):
        participants.append(heat3_participants[i])
        times.append(np.random.normal(athlete_avg_skill_level[heat3_participants[i]], .3))
        
    # run heat 4
    for i in range(len(heat4_participants)):
        participants.append(heat4_participants[i])
        times.append(np.random.normal(athlete_avg_skill_level[heat4_participants[i]], .3))
        
        
    
    # heat participants by times
    prelim_result_list = [i for time, i in sorted(zip(times, participants))]
    prelim_winners = prelim_result_list[0:17]
    
    
    
    # run the "semifinals"
    ath_finished_semi = []
    semifinals1 = np.random.choice(prelim_winners, size=8, replace=False)
    for athlete in semifinals1:
        ath_finished_semi.append(athlete)
        
    semifinals2 = np.random.choice(np.array(list(set(prelim_winners) ^ set(ath_finished_semi))),
                                          size=8, replace=False)
    for athlete in semifinals2:
        ath_finished_semi.append(athlete)
        
        
    semi_participants = []
    times = []
    for i in range(len(semifinals1)):
        semi_participants.append(semifinals1[i])
        times.append(np.random.normal(athlete_avg_skill_level[semifinals1[i]], .3))
        
    for i in range(len(semifinals2)):
        semi_participants.append(semifinals2[i])
        times.append(np.random.normal(athlete_avg_skill_level[semifinals2[i]], .3))
    
    semi_result_list = [i for time, i in sorted(zip(times, semi_participants))]
    semi_winners = semi_result_list[0:8]
        
    
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
















