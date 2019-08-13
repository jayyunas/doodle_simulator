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
    numTimeSlots = 12
    numParticipants = 5

    match = []
    no_match = []

    percent_match = []
    percent_no_match = []

    numTrials = int(input("How many trials? "))
    
    true = 0
    false = 0
    
    for i in range(numTrials):
        t = individual_thresholds(numParticipants)
        u = util(numTimeSlots, numParticipants)
        v = vote(u, t, numTimeSlots, numParticipants)
        d = doodle(v, u, numTimeSlots, numParticipants)

        if d:
            true += 1
        else:
            false += 1

    match.append(true)
    no_match.append(false)
    percent_match.append(round((true/numTrials)*100, 2))
    percent_no_match.append(round((false/numTrials)*100, 2))
        
    print('\n'+ "Number of matches:", match,'\n'+"Number of non-matches:", no_match)
    print('\n'+ "% of matches:", percent_match,'\n'+"% of non-matches:", percent_no_match)
    
main()
