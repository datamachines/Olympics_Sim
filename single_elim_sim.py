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


