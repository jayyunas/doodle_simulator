#!/usr/bin/env python3
#Doodle Poll Simulator
##Jay Yunas
##CS Summer Research Project

##Open Simulation v1.0
## single instance

from random import *
import math
from array import *

def doodle(vote, utilities, times, participants):
    v = vote
    u = utilities
    col_totals_votes = [sum(x) for x in zip(*v)]
    col_totals_utilities = [sum(x) for x in zip(*u)]

    print("Total Votes:", col_totals_votes)
    print("Social Welfare:", [round(elem, 2) for elem in col_totals_utilities], '\n')

    max_value_votes = max(col_totals_votes)
    max_index_votes = col_totals_votes.index(max_value_votes)

    max_value_utilities = max(col_totals_utilities)
    max_index_utilities = col_totals_utilities.index(max_value_utilities)

    print("The doodle slot in this poll is slot:", max_index_votes + 1, "with social welfare:", round(col_totals_utilities[max_index_votes], 2))
    print("The socially optimal times slot is:", max_index_utilities + 1, "with social welfare:", round(col_totals_utilities[max_index_utilities], 2)) 

    if max_index_votes == max_index_utilities:
        return True
    return False
        
def util(times, participants):
    utilities = [[0 for x in range(times)] for y in range(participants)]
    
    for i in range(participants):
        for j in range(times):
            u = round(random(), 2)
            utilities[i][j] = u

    print("Utilities:")
    voter = 0
    for row in utilities:
        voter += 1
        print("Voter", str(voter) + ":", row)

    print("")
            
    return utilities

def vote(utility, times, participants):
    votes = [[0 for x in range(times)] for y in range(participants)]
    t_2 = .75
    t_1 = .25
    t_first = .5
   

    #have voter 0 vote based on default threshold
    for j in range(times):
        if utility[0][j] > t_first:
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
                    print("Time Slot", j+1, "is popular for voter", i+1)
                    votes[i][j] = 1
                elif unpopular:
                    print("Time Slot", j+1, "is unpopular for voter", i+1)
                    votes[i][j] = 1
                else:
                    votes[i][j] = 0
            else: 
                votes[i][j] = 0

    print("")
    print("Votes:")
    voter = 0
    for row in votes:
        voter += 1
        print("Voter", str(voter) + ":", row)

    print("")
    return votes

#removed individual thresholds

def main():
    numTimeSlots = 12
    numParticipants = 5

    u = util(numTimeSlots, numParticipants)
    v = vote(u, numTimeSlots, numParticipants)
    d = doodle(v, u, numTimeSlots, numParticipants)
    
main()
