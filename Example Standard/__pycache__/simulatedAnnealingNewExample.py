import math
from calculate_ExpectedtimeExample import calculate_Expectedtime
from localsearchExample import SwapSequence
import numpy as np


def SimulatedAnnealing(network, initialSeq, num_Repetitions, initialTemp, coolingRate, maxIterations):
    #SimulatedAnnealing(G, sequence, numOfIteration, 1000, 0.8, 10000)
    currentSeq = initialSeq.copy()
    currentCost = calculate_Expectedtime(network, currentSeq, num_Repetitions)
    bestSeq = currentSeq.copy()
    bestCost = currentCost

    temperature = initialTemp

    iteration = 0
    while iteration < maxIterations:
        swappedSeq, swappedCost = SwapSequence(network, currentSeq, num_Repetitions)

        if swappedCost < currentCost:
            currentCost = swappedCost
            currentSeq = swappedSeq.copy()
            if swappedCost < bestCost:
                bestSeq = swappedSeq.copy()
                bestCost = swappedCost
        else:
            deltaCost = swappedCost - currentCost
            if math.exp(-deltaCost / temperature) > np.random.rand():
                currentCost = swappedCost
                currentSeq = swappedSeq.copy()
        
        temperature *= coolingRate
        iteration += 1


    print("Best sequence: ", bestSeq)
    print("Best Expected Cost: ", bestCost)
    return bestSeq, bestCost

# ... The SwapSequence function remains unchanged ...
