#Doodle Poll Simulator
##Jay Yunas
##CS Summer Research Project

##v1.5: average and max welfare approximation ratio
## individual thresholds

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

def vote(utility, threshold, times, participants):
    votes = [[0 for x in range(times)] for y in range(participants)]

    for i in range(participants):
        t = threshold[i]
        for j in range(times):
            if utility[i][j] > t:
                votes[i][j] = 1
            else:
                votes[i][j] = 0

    return votes

def individual_thresholds(participants):
    thresholds = []
    for i in range(participants):
        t = (randrange(2, 8, 1))/10
        thresholds.append(t)

    return thresholds

def main():
    print("Hidden Simulation, Average & Max Welfare Approximation Ratio - Individual Thresholds")
    numTimeSlots = 12
    numParticipants = 5

    numTrials = int(input("numTrials? "))
    print("Number of Trials:", numTrials)

    sum_welfare_ratio = 0
    welfare_ratios = []
    
    for i in range(numTrials):
        t = individual_thresholds(numParticipants)
        u = util(numTimeSlots, numParticipants)
        v = vote(u, t, numTimeSlots, numParticipants)
        d = doodle(v, u, numTimeSlots, numParticipants)

        sum_welfare_ratio += d
        welfare_ratios.append(d)
    
    avg_welfare_ratio = round(sum_welfare_ratio/numTrials, 2)
    max_welfare_ratio = round(max(welfare_ratios), 2)

    print('\n'+ "Average ratio of OPT/doodle:", avg_welfare_ratio)
    print("Max welfare ratio of OPT/doodle:", max_welfare_ratio)

main()
