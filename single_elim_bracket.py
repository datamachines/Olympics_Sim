#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:52:33 2021

@author: ivy
    
Bracket simulation:
    single elimination style
    fencing uses this structure
"""

import numpy as np
## set seed for dev, remove it for actual simulation 
# import random
# random.seed(10)

# athletes have a latent quality (same as in the other sim)
from fixed_vars import *

totalmatches = n_athletes - 1



games_map = {}
next_players = []

def first_round(n_athletes, athlete_avg_skill_level):
    next_players = []
    for i in range(int(n_athletes / 2)):
        match_players = []
        match_scores = []
        player1_id = i
        player2_id = n_athletes - 1 - i
        match_players.append(player1_id)
        match_players.append(player2_id)
        # print("Ids: ", player1_id, player2_id)
        
        player1_score = np.random.normal(athlete_avg_skill_level[player1_id], .3)
        player2_score = np.random.normal(athlete_avg_skill_level[player2_id], .3)
        match_scores.append(player1_score)
        match_scores.append(player2_score)
        # print("scores: ", player1_score, player2_score)
        
        match_result = [i for score, i in sorted(zip(match_scores, match_players))]
        # higher score wins
        match_winner = match_result[1]
        next_players.append(match_winner)
        # print("Match winner: ", match_winner)
    # print(next_players)
    return next_players

def next_round(next_players, athlete_avg_skill_level): 
    next_round_players = []
    for i in range(int(len(next_players)/2)):
        match_players = []
        match_scores = []
        player1_id = next_players[i]
        player2_id = next_players[len(next_players) - 1 - i]
        match_players.append(player1_id)
        match_players.append(player2_id)
        # print("Ids: ", player1_id, player2_id)
        
        player1_score = np.random.normal(athlete_avg_skill_level[player1_id], .3)
        player2_score = np.random.normal(athlete_avg_skill_level[player2_id], .3)
        match_scores.append(player1_score)
        match_scores.append(player2_score)
        # print("scores: ", player1_score, player2_score)
        
        match_result = [i for score, i in sorted(zip(match_scores, match_players))]
        
        # higher score wins
        match_winner = match_result[1]
        next_round_players.append(match_winner)
        # print("Match winner: ", match_winner)
    # print (next_round_players)
    return next_round_players
    

   




            
            
            
            
            
    
    
    
    