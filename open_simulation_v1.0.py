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
    popular = False
    unpopular = False
    
    for i in range(participants):
        for j in range(times):
            totals_votes_cur = [sum(x) for x in zip(*votes)]
            if totals_votes_cur[j]/participants >= .8:
                popular = True
            if totals_votes_cur[j]/participants <= .2:
                unpopular = True

            if utility[i][j] > t_2:
                votes[i][j] = 1
            elif t_1 < utility[i][j] < t_2:
                if popular:
                    #print("Time Slot", j+1, "is popular for voter", i+1)
                    votes[i][j] = 1
                elif unpopular:
                    #print("Time Slot", j+1, "is unpopular for voter", i+1)
                    votes[i][j] = 1
                else:
                    votes[i][j] = 0
            else: 
                votes[i][j] = 0
    
    return votes

#removing individual thresholds

def main():
    numTimeSlots = 12
    numParticipants = 5
    global_threshold = 0.5

    

    for j in range(10):
        false = 0
        true = 0
        for i in range(1000):
            u = util(numTimeSlots, numParticipants)
            v = vote(u, numTimeSlots, numParticipants)
            d = doodle(v, u, numTimeSlots, numParticipants)

            if d:
                true += 1
            else:
                false += 1
        print(true/false)
main()
