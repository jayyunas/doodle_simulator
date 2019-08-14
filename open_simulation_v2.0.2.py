#!/usr/bin/env python3
#Doodle Poll Simulator
##Jay Yunas
##CS Summer Research Project

##Open Simulation v2.0.2
## number and percent of matches, decreasing upper threshold

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

    if max_index_votes == max_index_utilities:
        return True
    return False
        
def util(times, participants):
    utilities = [[0 for x in range(times)] for y in range(participants)]
    
    for i in range(participants):
        for j in range(times):
            u = round(random(), 2)
            utilities[i][j] = u
            
    return utilities

def vote(utility, thresholds, times, participants):
    votes = [[0 for x in range(times)] for y in range(participants)]
    t_2 = thresholds[1]
    t_1 = thresholds[0]
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
            elif t_1 < utility[i][j] < t_2:
                if popular:
                    votes[i][j] = 1
                elif unpopular:
                    votes[i][j] = 1
                else:
                    votes[i][j] = 0
            else: 
                votes[i][j] = 0

    return votes

def main():
    print("Open Simulation, Number & Percent Matches, Varying Thresholds")
    
    numTimeSlots = 12
    numParticipants = 5

    t = [0.25, 0.75]
    match = []
    no_match = []
    percent_match = []
    percent_no_match = []

    numTrials = int(input("numTrials? "))
    print("Number of Trials:", numTrials)
    
    for j in range(10):
        print(t)
        true = 0

        for i in range(numTrials):
            u = util(numTimeSlots, numParticipants)
            v = vote(u, t, numTimeSlots, numParticipants)
            d = doodle(v, u, numTimeSlots, numParticipants)

            if d:
                true += 1

        t[1] -= 0.05
        match.append(true)
        no_match.append(numTrials-true)
        percent_match.append(round((true/numTrials)*100, 2))
        percent_no_match.append(100-percent_match[j])

    print("\n"+"Number of matches:", match)
    print("Number of non-matches:", no_match)

    print("\n"+"% of matches:", percent_match)
    print("% of non-matches:", percent_no_match, "\n")


main()
