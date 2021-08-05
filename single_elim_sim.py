#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday Aug 3 12:28 2021

@author: Ethan

"""

import numpy as np
from single_elim_bracket import *
from fixed_vars import *


def get_gold_sliv_bracket_winners(n_athletes, athlete_avg_skill_level):
    # array to hold results of each round
    rounds = []
    # counter to be used in for-loop to track the number of rounds
    remaining_rounds = 4
    
    # get the first round results
    first_result = first_round(n_athletes, athlete_avg_skill_level)
    rounds.append(first_result)
    # print round 0 results
    # print ("Round 0 winners:", first_result)
    
    # get results for the remaining rounds
    for round_num in range(remaining_rounds):
        next_result = next_round(rounds[round_num], athlete_avg_skill_level)
        rounds.append(next_result)
        # print round results
        # if (round_num < 3):
        #    print ("Round",round_num + 1,"winners:", next_result)
    
    # print final results
    # print("Round 4 winner:", rounds[len(rounds)-1])
    
    quarterfinal_winners = rounds[len(rounds)-3]
    
    gold_silver_medalists = rounds[len(rounds)-2]
    
    return gold_silver_medalists, quarterfinal_winners, rounds
   
 
'''

losers of the 4 quarter final matches move into a new bracket. 
The winner of this bracket wins the bronze.

'''

def get_bronze_bracket_winner(quarterfinal_winners, rounds, athlete_avg_skill_level):
    bronze_rounds = []
    bronze_brac_rounds = 2
    
    # the losers of the quarterfinals go into the bronze bracket
    bronze_starting_bracket = [i for i in set(quarterfinal_winners) ^ set(rounds[len(rounds)-4])]

    bronze_rounds.append(bronze_starting_bracket)
    
    for round_num in range(bronze_brac_rounds):
        next_result = next_round(bronze_rounds[round_num], athlete_avg_skill_level)
        # print ("round: ", bronze_rounds[round_num], "result: ", next_result)
        bronze_rounds.append(next_result)
        
    bronze_medalist = bronze_rounds[2]
    # print("Bronze medalist: ", bronze_rounds[2])
    
    return bronze_medalist


def run_elim_bracket(n_athletes, athlete_avg_skill_level):
    gold_silver_medalists, quarterfinal_winners, rounds = get_gold_sliv_bracket_winners(n_athletes, athlete_avg_skill_level)
    bronze_medalist = get_bronze_bracket_winner(quarterfinal_winners, rounds, athlete_avg_skill_level)
    # return the medal winners 
    # note: the gold and silver medalists aren't necessarily in order
    medalists = [i for i in gold_silver_medalists]
    for i in bronze_medalist:
        medalists.append(i)
        
    return medalists
    
