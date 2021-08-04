#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:33:34 2021

@author: ivy

Olympic tournament strucutre: round robins 

this structure is used in soccer, basketball, and beach volleyball amongst other olympic sports

the starting # of teams (in this case 32) are broken into groups of 4 (8 groups of 4 teams)
round robins - each team then plays every other team in their group (6 games per groups)
teams get a point for each game won, and the top two teams from each pool move onto a
single elimination bracket.

"""

import numpy as np
from fixed_vars import *
from collections import Counter

list_of_athletes = list(range(n_athletes))

# form groups for the reound robins prelims

def assign_pools(list_of_athletes, poolsize=4):
    pools = []

    pool1 = np.random.choice(list_of_athletes, size=poolsize, replace=False)
    pools.append(list(pool1))
    
    teams_assigned_to_pool = []
    for team in pool1:
        teams_assigned_to_pool.append(team)
        
    remaining_teams_to_assign = list(set(teams_assigned_to_pool) ^ set(list_of_athletes))
    
    for i in list(range(int(len(remaining_teams_to_assign)/poolsize))):
        pool = np.random.choice(np.array(list(set(teams_assigned_to_pool) ^ set(list_of_athletes))),
                                              size=poolsize, replace=False)
        pools.append(list(pool))
        for team in pool:
            teams_assigned_to_pool.append(team)
        
    return pools


pools = assign_pools(list_of_athletes, poolsize=4)


def run_round_robins(pools):
    single_elim_teams = []
    for teams in pools:
        games = list(itertools.combinations(teams, 2))
        # print(games)
        
        pool_winners = []
        for matchup in games: 
            match_players = []
            match_scores = []
            team1 = matchup[0]
            teams2 = matchup[1]
            match_players.append(team1)
            match_players.append(teams2)
            team1_score = np.random.normal(athlete_avg_skill_level[matchup[0]], .3)
            team2_score = np.random.normal(athlete_avg_skill_level[matchup[1]], .3)
            match_scores.append(team1_score)
            match_scores.append(team2_score)
            
            match_result = [i for score, i in sorted(zip(match_scores, match_players))]
            
            match_winner = match_result[1]
            pool_winners.append(match_winner)
            print ("Matchup: ", matchup, "Scores: ", match_scores, "Winner: ", match_winner)
        
        
        # count up the # wins per team in the list of pool_winners
        # so those teams that doesn't win any games, get dropped from the final score list
        pool_teams = list(Counter(pool_winners).keys()) # equals to list(set(pool_winners))
        pool_scores = list(Counter(pool_winners).values()) # counts the elements' frequency
        
        '''
        ISSUE: how do we account for ties (i.e. all 3 teams when 2 games)
        the olympics breaks ties based on the head-to-head scores between the tied teams.
        
        '''
        
        # use sorted(  , reverse=True) to list the scores hightest to lowest 
        pool_result = [i for score, i in sorted(zip(pool_scores, pool_teams), reverse=True)]
        print ("Pool Results: ", pool_result)
        move_onto_single_elim = pool_result[0:2]
        for team in move_onto_single_elim:
            single_elim_teams.append(team)
        
    return single_elim_teams


    
