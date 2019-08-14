#Doodle Poll Simulator
##Jay Yunas
##CS Summer Research Project

##v1.4: percent of the time doodle matches OPT
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
    print("Hidden Simulation, Number & Percent Matches")
    
    numTimeSlots = 12
    numParticipants = 5

    numTrials = int(input("How many trials? "))
    print("Number of Trials:", numTrials)

    match = 0
    no_match = 0
    
    for i in range(numTrials):
        t = individual_thresholds(numParticipants)
        u = util(numTimeSlots, numParticipants)
        v = vote(u, t, numTimeSlots, numParticipants)
        d = doodle(v, u, numTimeSlots, numParticipants)

        if d:
            match += 1
        else:
            no_match += 1

    print("\n"+"Number of Matches:", match)
    print("Number of Non-Matches:", no_match)

    avg_match = round((match/numTrials)*100, 2)
    print("\n"+"Average Percent of Matches:", str(avg_match) + '%')

    avg_no_match = round((no_match/numTrials)*100, 2)
    print("Average Percent of Non-Matches:", str(avg_no_match) + '%')
    
main()
