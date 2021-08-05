#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday Aug 3 12:28 2021

@author: Ethan

"""

import numpy as np
from single_elim_bracket import *
from fixed_vars import *

# array to hold results of each round
rounds = []
# counter to be used in for-loop to track the number of rounds
remaining_rounds = 4

# get the first round results
first_result = first_round(n_athletes, athlete_avg_skill_level)
rounds.append(first_result)
# print round 0 results
print ("Round 0 winners:", first_result)

# get results for the remaining rounds
for round_num in range(remaining_rounds):
    next_result = next_round(rounds[round_num], athlete_avg_skill_level)
    rounds.append(next_result)
    if (round_num < 3):
        print ("Round",round_num + 1,"winners:", next_result)

# print final results
print("Round 4 winner:", rounds[len(rounds)-1])


gold_silver_medalists = rounds[len(rounds)-2]
   
 
'''

losers of the 4 quarter final matches move into a new bracket. 
The winner of this bracket wins the bronze.

'''

bronze_rounds = []
bronze_brac_rounds = 2

quarterfinal_winners = rounds[len(rounds)-3]
bronze_starting_bracket = [i for i in set(quarterfinal_winners) ^ set(rounds[len(rounds)-4])]

bronze_rounds.append(bronze_starting_bracket)

for round_num in range(bronze_brac_rounds):
    next_result = next_round(bronze_rounds[round_num], athlete_avg_skill_level)
    print ("round: ", bronze_rounds[round_num], "result: ", next_result)
    bronze_rounds.append(next_result)

bronze_medalist = bronze_rounds[2]
print("Bronze medalist: ", bronze_rounds[2])


top_three_medalists = [i for i in gold_silver_medalists]
for i in bronze_medalist:
    top_three_medalists.append(i)