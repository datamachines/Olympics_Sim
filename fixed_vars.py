#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 16:21:06 2021

@author: ivy

Olympic simulation fixed variables :
    hold # of athletes and their associated skill level/ latent quality constant
"""


import numpy as np
import random
random.seed(10)

# number of athletes in a competition
n_athletes = 32
list_of_athletes = list(range(n_athletes))

# all athletes have a randomly assigned skill level between 0 and 1 from a uniform distribution
# this represent their latent quality coming into the olympics
athlete_avg_skill_level = np.random.uniform(0, 1, n_athletes)

# specific tournament simulation fixed variables
# fix the number of athletes per heat
num_ath_per_heat = 8

# fixed the poolsize for round robins
poolsize = 4


# who is the best player going into the olympics?
# heat events are usually measuring speed. the best athlete has the fastest time. 
fastest_avg_time = min(athlete_avg_skill_level)
fastest_athlete_pre_oly = list(athlete_avg_skill_level).index(fastest_avg_time)

# bracket and round robin events are usually measuring highest score/ most wins. 
highest_latent_quality = max(athlete_avg_skill_level)
best_athlete_pre_oly = list(athlete_avg_skill_level).index(highest_latent_quality)


