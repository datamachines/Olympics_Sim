# Olympics_sim
Simulate different tournament structures that appear at the Olympic games

In this repo, there are three Olympic tournament structures being simulated:
1. Heats
2. Single Elimination Brackets
3. Round Robins

The # athletes and their athletes average skill level going into the Olympics are held fixed in fixed_vars.py

The plot script generates a line graph of the three simulated tournament structures, showing the # of times the athlete with the highest average skill level won a medal per iteration of the simulation. 

get_plot_data.py uses run_sim.py to generate simulated data of the tournament structures. 

run_sim.py references functions defined heat_functions.py to simulate heats,  single_elim_sim.py and bracket_functions.py to simulate single eliminate brackets, and round_robins.py	to simulate round robin tournaments. 