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

# athletes have a latent quality
n_athletes = 32
# all athletes randomly assigned a skill level between 0 and 1 from a uniform distribution
athlete_avg_skill_level = np.random.uniform(0, 1, n_athletes)
<<<<<<< HEAD

# who is the best player going into the olympics?
highest_latent_quality = max(athlete_avg_skill_level)
best_athlete_pre_oly = list(athlete_avg_skill_level).index(highest_latent_quality)



=======
# set number of athletes in each heat
num_ath_per_heat = 8
# run competition simulation n_sims number of times
n_sims = 100
>>>>>>> 893584d4d7dcac3bbd1519a70008e2f6dc47c160
