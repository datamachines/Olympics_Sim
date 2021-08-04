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

# all athletes have a randomly assigned skill level between 0 and 1 from a uniform distribution
# this represent their latent quality coming into the olympics
athlete_avg_skill_level = np.random.uniform(0, 1, n_athletes)

# who is the best player going into the olympics?
highest_latent_quality = max(athlete_avg_skill_level)
best_athlete_pre_oly = list(athlete_avg_skill_level).index(highest_latent_quality)


# set number of athletes in each heat
num_ath_per_heat = 8
