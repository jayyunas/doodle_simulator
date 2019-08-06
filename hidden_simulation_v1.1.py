#Doodle Poll Simulator
##Jay Yunas
##CS Summer Research Project

from random import *
import math
from array import *

#single simulation with individual thresholds

def doodle():
    numTimeSlots = 12
    numParticipants = 5
    t = individual_thresholds(numParticipants)
    u = util(numTimeSlots, numParticipants)
    v = vote(u, t, numTimeSlots, numParticipants)
    
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
        
def util(times, participants):
    utilities = [[0 for x in range(times)] for y in range(participants)]
    
    for i in range(participants):
        for j in range(times):
            u = round(random(), 2)
            utilities[i][j] = u

    voter = 0
    for row in utilities:
        voter += 1
        print("Voter", str(voter) + ":", row)

    print("")
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

    voter = 0
    for row in votes:
        voter += 1
        print("Voter", str(voter) + ":", row)
        
    print("")
    return votes

def individual_thresholds(participants):
    thresholds = []
    for i in range(participants):
        t = (randrange(2, 8, 1))/10
        thresholds.append(t)
    
    print("Individual Thresholds:", thresholds, '\n')
    return thresholds

def main():

    d = doodle()
        
main()
