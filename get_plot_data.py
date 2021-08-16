#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:00:22 2021

@author: ethan
"""


# import functions from related scripts
from run_sim import *


def get_plot_data(n_sims):
    # arrays to store number of times that the best athlete won a medal in each competition type
    heat_count = []
    single_count = []
    robin_count = []
    # run each set of 100 simulations 100 times
    for sim in range(n_sims):
        # get sample distribution for heat, single elim, and round robins
        did_best_athlete_win_heat = run_heat_sims(n_sims, n_athletes, athlete_avg_skill_level, num_ath_per_heat, fastest_athlete_pre_oly)
        did_best_athlete_win_single = run_single_elim_brac_sims(n_sims, n_athletes, athlete_avg_skill_level, best_athlete_pre_oly)
        did_best_athlete_win_robin = run_roundrobin_sims(n_sims, athlete_avg_skill_level, best_athlete_pre_oly)
        # add new sample distribution to count arrays
        heat_count.append(did_best_athlete_win_heat.count(1))
        single_count.append(did_best_athlete_win_single.count(1))
        robin_count.append(did_best_athlete_win_robin.count(1))
    
    return heat_count, single_count, robin_count


plot_data = get_plot_data(n_sims=100)
print("The avg time the best athlete wins a medal in heats: ", np.mean(plot_data[0]))
print("The avg time the best athlete wins a medal in elimination bracket: ", np.mean(plot_data[1]))
print("The avg time the best athlete wins a medal in round robins: ", np.mean(plot_data[2]))