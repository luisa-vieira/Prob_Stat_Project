# Prob_Stat_Project
This a simulation of Renshaw’s spatial predator-prey model from Exercise 10 of Chapter 7 of the book:
ALLEN, Linda JS. An introduction to stochastic processes with applications to biology. CRC press, 2010.

## Deterministic_model.py 

## Project_v5.py

Runs 50 simulations for the the case in which we have two patches (two preys and two predator populations) and records the proportion of sample paths in which the
prey is extinct, the predators are extinct and in which both populations coexist. 

The simulations are performed for four cases: (i) u = v = 0; (ii) u = 0.001 = v (prey and predator movement rates are equal); (iii) u = 0.001 and v = 0.01 (predator movement > prey movement); (iv) u = 0.01 and v = 0.001 (prey movement > predator movement). The code also returns a  plot to exeplify each of those cases.

## Project_three_patches.py

Same as Project_v5.py but for a case in which there are three patches.
