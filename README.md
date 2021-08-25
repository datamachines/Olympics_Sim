# Olympics_sim
Simulate different tournament structures that appear at the Olympic games.

In this repo, there are three Olympic tournament structures being simulated:
1. Heats
2. Single Elimination Brackets
3. Round Robins

The code in this repo simulates the tournament structures and generates two plots (located in /plots) to display the results of the Olympic simulation. 


To run in your own environment:
1. Install numpy, matplotlib, and seaborn
2. clone the repo and run "python plot.py" from inside the repo to generate two new plots in /plots.


To run in a docker container:

We have included the Dockerfile, so all you have to do is create a new directory for the outputs of running your container (/myplots), build and run.

mkdir myplots
docker build --tag dmc_oly:dev .
docker run --rm -v `pwd`/myplots:/dmc/plots dmc_oly:dev python3 plot.py


Explaination of the code and how the simulations are generated:

The plot.py script generates the two plots: a line graph and a density plot. The line graph shows the # of times the athlete with the highest average skill level won a medal per iteration of the simulation. The density plot shows the densities associated with how often the best athlete wins a medal given each tournament structure. 

Plot.py uses get_plot_data.py to generate the data which references run_sim.py to generate simulated data of the tournament structures. 

Run_sim.py references functions defined heat_functions.py to simulate heats,  single_elim_sim.py and bracket_functions.py to simulate single elimination brackets, and round_robins.py	to simulate round robin tournaments. 

Prior to each Olympic simulation, the # of competing athletes and their base average skill levels are held fixed in fixed_vars.py.