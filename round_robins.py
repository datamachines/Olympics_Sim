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

# from fixed_vars import *
from collections import Counter
import itertools
from bracket_functions import *
from single_elim_sim import get_bronze_bracket_winner


# form groups for the round robins prelims
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


def run_round_robins(pools, athlete_avg_skill_level):
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
            # print ("Matchup: ", matchup, "Scores: ", match_scores, "Winner: ", match_winner)
        
        
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
        # print ("Pool Results: ", pool_result)
        move_onto_single_elim = pool_result[0:2]
        for team in move_onto_single_elim:
            single_elim_teams.append(team)
        
    return single_elim_teams


def run_elim_bracket(phase_two_teams, athlete_avg_skill_level):

    rounds = []
    rounds.append(phase_two_teams)
    
    # counter to be used in for-loop to track the number of rounds
    remaining_rounds = 4
    
    for round_num in range(remaining_rounds):
       next_result = next_round(rounds[round_num], athlete_avg_skill_level)
       rounds.append(next_result)
       # print results
       # if (round_num < 3):
       #    print ("Round",round_num + 1,"winners:", next_result)
        
    # print final results
    # print("Round 4 winner:", rounds[len(rounds)-1])
        
    quarterfinal_winners = rounds[len(rounds)-3]
        
    gold_silver_medalists = rounds[len(rounds)-2]
    
    return gold_silver_medalists, quarterfinal_winners, rounds



def run_roundrobin(list_of_athletes, athlete_avg_skill_level, poolsize):
    # create the round robin pools, 8 teams in each pool
    pools = assign_pools(list_of_athletes, poolsize)
    # play round robins and determine who moves onto phase 2: single elimination bracket
    phase_two_teams = run_round_robins(pools, athlete_avg_skill_level)
    # the final two in the single elimination bracket compete for the gold, runner up wins silver
    gold_silver_medalists, quarterfinal_winners, rounds = run_elim_bracket(phase_two_teams, athlete_avg_skill_level)
    # the losers of the quarterfile matches compete in the bronze bracket
    # import get_bronze_bracket_winner function from single_elim_sim.py
    bronze_medalist = get_bronze_bracket_winner(quarterfinal_winners, rounds, athlete_avg_skill_level)
    
    # return the medal winners 
    # note: the gold and silver medalists aren't necessarily in order
    medalists = [i for i in gold_silver_medalists]
    for i in bronze_medalist:
        medalists.append(i)
        
    return medalists
   
    