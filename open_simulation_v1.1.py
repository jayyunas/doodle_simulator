#!/usr/bin/env python3
#Doodle Poll Simulator
##Jay Yunas
##CS Summer Research Project

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
    numTimeSlots = 12
    numParticipants = 5
    
    numTrials = int(input("numTrials? "))

    print('\n'+"Voting Threshold Ranges:")
    print("[0, 0.25] -- 0")
    print("(0.25, 0.75] -- depends on popularity")
    print("[0.75, 1] -- 1")

    print("")
    match = []
    no_match = []
    for j in range(10):
        false = 0
        true = 0
        for i in range(numTrials):
            u = util(numTimeSlots, numParticipants)
            v = vote(u, numTimeSlots, numParticipants)
            d = doodle(v, u, numTimeSlots, numParticipants)

            if d:
                true += 1
            else:
                false += 1
        match.append(true)
        no_match.append(false)

    total_match = sum(match)
    avg_match = round(((total_match/numTrials)/numTrials)*numTrials, 2)

    total_no_match = sum(no_match)
    avg_no_match = round(((total_no_match/numTrials)/numTrials)*numTrials, 2)
    
    print("Average Percent of Matches:", str(avg_match) + '%')

    print("")
    
    print("Average Percent of Non-Matches:", str(avg_no_match) + '%')


    

    
main()
