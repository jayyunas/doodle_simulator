#!/usr/bin/env python3
#Doodle Poll Simulator
##Jay Yunas
##CS Summer Research Project

##Open Simulation v1.2
## average and max welfare approximation ratio

from random import *
import math
from array import *

def doodle(vote, utilities, times, participants):
    v = vote
    u = utilities
    col_totals_votes = [sum(x) for x in zip(*v)]
    col_totals_utilities = [sum(x) for x in zip(*u)]

    max_value_votes = max(col_totals_votes)
    max_index_votes = col_totals_votes.index(max_value_votes)

    max_value_utilities = max(col_totals_utilities)
    max_index_utilities = col_totals_utilities.index(max_value_utilities)

    opt = max_value_utilities
    ddl = col_totals_utilities[max_index_votes]

    welfare_approx_ratio = opt/ddl
    
    return welfare_approx_ratio
        
def util(times, participants):
    utilities = [[0 for x in range(times)] for y in range(participants)]
    
    for i in range(participants):
        for j in range(times):
            u = round(random(), 2)
            utilities[i][j] = u
            
    return utilities

def vote(utility, times, participants):
    votes = [[0 for x in range(times)] for y in range(participants)]
    t_2 = .75
    t_1 = .25
    t_global = .5
   

    #have voter 0 vote based on default threshold
    for j in range(times):
        if utility[0][j] > t_global:
            votes[0][j] = 1
        else:
            votes[0][j] = 0
            
    #have i start at 1
    for i in range(1, participants):
        
        for j in range(times):
            popular = False
            unpopular = False
            totals_votes_cur = [sum(x) for x in zip(*votes)]
            if totals_votes_cur[j]/i >= .8:
                popular = True
            if totals_votes_cur[j]/i <= .2:
                unpopular = True

            if utility[i][j] > t_2:
                votes[i][j] = 1
            elif t_1 < utility[i][j] <= t_2:
                if popular or unpopular:
                    votes[i][j] = 1
                else:
                    votes[i][j] = 0
            else: 
                votes[i][j] = 0

    return votes

def main():
    while True:
        print("Open Simulation, Average & Max Welfare Approximation Ratio")

        numTimeSlots = 12
        numParticipants = 5

        numTrials = int(input("numTrials? "))
        print("Number of Trials:", numTrials)

        sum_welfare_ratio = 0
        welfare_ratios = []
        
        for i in range(numTrials):
            u = util(numTimeSlots, numParticipants)
            v = vote(u, numTimeSlots, numParticipants)
            d = doodle(v, u, numTimeSlots, numParticipants)

            sum_welfare_ratio += d
            welfare_ratios.append(d)
        
        avg_welfare_ratio = round(sum_welfare_ratio/numTrials, 2)
        max_welfare_ratio = round(max(welfare_ratios), 2)

        print('\n'+ "Average ratio of OPT/doodle:", avg_welfare_ratio)
        print("Max welfare ratio of OPT/doodle:", max_welfare_ratio, "\n")

    
main()
