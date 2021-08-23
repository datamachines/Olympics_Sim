# Olympics_sim
Simulate different tournament structures that appear at the Olympic games.

In this repo, there are three Olympic tournament structures being simulated:
1. Heats
2. Single Elimination Brackets
3. Round Robins

Use the plot.py script to generate two plots: a line graph and a density plot. The line graph shows the # of times the athlete with the highest average skill level won a medal per iteration of the simulation. The density plot shows the densities associated with how often the best athlete wins a medal given each tournament structure. 


Plot.py uses get_plot_data.py to generate the data which references run_sim.py to generate simulated data of the tournament structures. 

Run_sim.py references functions defined heat_functions.py to simulate heats,  single_elim_sim.py and bracket_functions.py to simulate single elimination brackets, and round_robins.py	to simulate round robin tournaments. 

Prior to each Olympic simulation, the # of competing athletes and their base average skill levels are held fixed in fixed_vars.py.